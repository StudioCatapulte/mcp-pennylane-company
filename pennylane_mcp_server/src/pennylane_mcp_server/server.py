import asyncio
import logging
import os
import time

import httpx
from dotenv import load_dotenv
from mcp.server import Server, NotificationOptions
from mcp.server.models import InitializationOptions
import mcp.server.stdio
import mcp.types as types

# Load environment variables from .env file
load_dotenv()

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# API configuration for Pennylane
PENNYLANE_API_KEY = os.getenv("PENNYLANE_API_KEY")
PENNYLANE_API_BASE_URL = "https://app.pennylane.com/api/external/firm/v1"
# Rate limiting: 4 requests per second, so 1/4 = 0.25 seconds delay between requests.
# For safety, and to account for network latency, we'll use a slightly larger delay.
REQUEST_DELAY = 0.3  # seconds
last_request_time = 0

if not PENNYLANE_API_KEY:
    logger.warning("PENNYLANE_API_KEY environment variable is not set. API calls will likely fail.")

# Create a server instance
# The name should be descriptive and unique for this MCP server.
app = Server("pennylane-expert-comptable-mcp")

# --- Placeholder for API client --- 
async def get_pennylane_client() -> httpx.AsyncClient:
    """Creates and returns an httpx.AsyncClient configured for Pennylane API,
    including basic rate limiting.
    """
    global last_request_time
    current_time = time.time()
    time_since_last_request = current_time - last_request_time

    if time_since_last_request < REQUEST_DELAY:
        sleep_duration = REQUEST_DELAY - time_since_last_request
        logger.debug(f"Rate limiting: sleeping for {sleep_duration:.2f} seconds.")
        await asyncio.sleep(sleep_duration)

    headers = {
        "Authorization": f"Bearer {PENNYLANE_API_KEY}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    
    # Update last_request_time *before* making the request if using a shared client.
    # If creating a new client each time, this is less critical here,
    # but good practice for a shared rate limiter.
    # For this simple case, we'll update it after the client is ready to be used.
    # last_request_time = time.time() # This would be better in a wrapper around client.request

    client = httpx.AsyncClient(base_url=PENNYLANE_API_BASE_URL, headers=headers)
    
    # Monkey patch the client to update last_request_time after each request
    # This is a simplified approach. A more robust solution would involve a custom transport.
    original_request = client.request
    async def rate_limited_request(*args, **kwargs):
        global last_request_time
        # Ensure delay before making the actual request call
        # This double check might be redundant if get_pennylane_client is always called before requests
        # but adds robustness.
        now = time.time()
        if now - last_request_time < REQUEST_DELAY:
             await asyncio.sleep(REQUEST_DELAY - (now - last_request_time))
        
        response = await original_request(*args, **kwargs)
        last_request_time = time.time()
        return response

    client.request = rate_limited_request
    # First call to get_pennylane_client will set the initial last_request_time correctly
    # if no requests happened before.
    if last_request_time == 0: # Initialize if it's the first time
        last_request_time = time.time() - REQUEST_DELAY # Allow immediate first request

    return client

# --- Resource Handlers (Example - to be expanded) --- 
@app.list_resources()
async def list_pennylane_resources() -> list[types.Resource]:
    logger.info("List resources requested.")
    # This is a placeholder. We will implement actual resources later.
    return [
        types.Resource(
            uri="pennylane://info",
            name="Pennylane MCP Information",
            mimeType="text/plain",
            description="Basic information about this Pennylane MCP server."
        )
    ]

@app.read_resource()
async def read_pennylane_resource(uri: types.AnyUrl) -> str:
    logger.info(f"Read resource requested for URI: {uri}")
    if str(uri) == "pennylane://info":
        return "This is a Model Context Protocol server for Pennylane, designed for expert comptables."
    raise types.McpError(types.ErrorCode.InvalidRequest, f"Unknown resource URI: {uri}")

# --- Tool Handlers (To be implemented based on plan.md) --- 
@app.list_tools()
async def list_pennylane_tools() -> list[types.Tool]:
    logger.info("List tools requested.")
    # Note on return types: Currently, most tools return a simple StringSchema
    # representing the JSON data. For enhanced LLM interaction, these could be
    # expanded to detailed ObjectSchemas mirroring the Pennylane API responses,
    # allowing the LLM to understand the structure of the returned data directly.
    return [
        types.Tool(
            name="list_companies",
            description="Retrieves a paginated list of companies associated with the authenticated firm. Useful for getting an overview of accessible companies.",
            arguments=types.ObjectSchema(
                properties={
                    "page": types.IntegerSchema(description="The page number for pagination (1-indexed). If not provided, the API typically defaults to the first page.", nullable=True),
                    "per_page": types.IntegerSchema(description="Number of companies to return per page. Accepted values are between 1 and 1000. If not provided, the API typically defaults to 20.", nullable=True)
                }
            ),
            returns=types.ObjectSchema(
                properties={
                    "companies_data": types.StringSchema(description="JSON string containing a list of company objects and pagination details (total_pages, current_page, total_items, per_page).")
                }
            )
        ),
        types.Tool(
            name="show_company_details",
            description="Fetches detailed information for a specific company using its unique Pennylane identifier.",
            arguments=types.ObjectSchema(
                required=["company_id"],
                properties={
                    "company_id": types.IntegerSchema(description="The unique Pennylane identifier for the company.")
                }
            ),
            returns=types.ObjectSchema(
                properties={
                    "company_data": types.StringSchema(description="JSON string containing the detailed information of the specified company (e.g., name, siren, address).")
                }
            )
        ),
        types.Tool(
            name="list_dms_files",
            description="Lists files from the Document Management System (DMS) for a given company. Supports cursor-based pagination and filtering by file ID.",
            arguments=types.ObjectSchema(
                required=["company_id"],
                properties={
                    "company_id": types.IntegerSchema(description="The unique Pennylane identifier for the company whose DMS files are to be listed."),
                    "cursor": types.StringSchema(description="An opaque cursor string for fetching the next set of results. Leave empty for the first request. Obtained from a previous response's 'next_cursor' field.", nullable=True),
                    "limit": types.IntegerSchema(description="Number of DMS files to return per request. Must be between 1 and 100. Defaults to 20 if not specified.", nullable=True),
                    "filter_id_operation": types.StringSchema(description="Filter operation for the file ID. Supported operations: 'eq' (equal), 'lt' (less than), 'lteq' (less than or equal), 'gt' (greater than), 'gteq' (greater than or equal), 'in', 'not_in'.", nullable=True),
                    "filter_id_value": types.AnySchema(description="Value for the file ID filter. For 'in'/'not_in', this would be an array of integers, but currently simplified to a single integer for other operations.", nullable=True)
                }
            ),
            returns=types.ObjectSchema(
                properties={
                    "dms_files_data": types.StringSchema(description="JSON string containing a list of DMS file objects (id, name, path, url, created_at, updated_at) and pagination cursors (has_more, next_cursor).")
                }
            )
        ),
        types.Tool(
            name="get_dms_file_changes",
            description="Retrieves a log of change events (insert, update, delete) for DMS files of a specific company. Supports cursor-based pagination and filtering by start date. Note: Changes are retained for the last 4 weeks.",
            arguments=types.ObjectSchema(
                required=["company_id"],
                properties={
                    "company_id": types.IntegerSchema(description="The unique Pennylane identifier for the company."),
                    "cursor": types.StringSchema(description="An opaque cursor string for fetching the next set of results. Leave empty for the first request. Cannot be used with 'start_date'.", nullable=True),
                    "limit": types.IntegerSchema(description="Number of change events to return per request. Must be between 1 and 1000. Defaults to 20 if not specified.", nullable=True),
                    "start_date": types.StringSchema(description="Filter changes from this specific date and time (RFC3339 format, e.g., 'YYYY-MM-DDTHH:MM:SSZ'). Cannot be used with 'cursor'. Events older than 4 weeks may not be available.", nullable=True)
                }
            ),
            returns=types.ObjectSchema(
                properties={
                    "dms_changes_data": types.StringSchema(description="JSON string containing a list of DMS file change event objects and pagination cursors.")
                }
            )
        ),
        types.Tool(
            name="list_fiscal_years",
            description="Fetches a paginated list of fiscal years for a specific company, including their start date, end date, and status.",
            arguments=types.ObjectSchema(
                required=["company_id"],
                properties={
                    "company_id": types.IntegerSchema(description="The unique Pennylane identifier for the company."),
                    "page": types.IntegerSchema(description="The page number for pagination (1-indexed).", nullable=True),
                    "per_page": types.IntegerSchema(description="Number of fiscal years to return per page. Accepted values are between 1 and 100. Defaults to 20.", nullable=True)
                }
            ),
            returns=types.ObjectSchema(
                properties={
                    "fiscal_years_data": types.StringSchema(description="JSON string containing a list of fiscal year objects (start, finish, status) and pagination details.")
                }
            )
        ),
        types.Tool(
            name="get_trial_balance",
            description="Retrieves the trial balance (balance des comptes) for a company over a specified period. Can include auxiliary accounts and supports pagination.",
            arguments=types.ObjectSchema(
                required=["company_id", "period_start", "period_end"],
                properties={
                    "company_id": types.IntegerSchema(description="The unique Pennylane identifier for the company."),
                    "period_start": types.StringSchema(description="Start date of the period for the trial balance (format: YYYY-MM-DD)."),
                    "period_end": types.StringSchema(description="End date of the period for the trial balance (format: YYYY-MM-DD)."),
                    "is_auxiliary": types.BooleanSchema(description="Set to true to include auxiliary accounts in the trial balance. Defaults to false if not provided.", nullable=True),
                    "page": types.IntegerSchema(description="The page number for pagination (1-indexed).", nullable=True),
                    "per_page": types.IntegerSchema(description="Number of trial balance items to return per page. Accepted values are between 1 and 1000. Defaults to 500.", nullable=True)
                }
            ),
            returns=types.ObjectSchema(
                properties={
                    "trial_balance_data": types.StringSchema(description="JSON string containing the list of trial balance items (ledger account number, label, debits, credits) and pagination details.")
                }
            )
        ),
        types.Tool(
            name="create_analytical_ledger_export",
            description="Initiates an asynchronous export of the Analytical General Ledger for a company over a specified period. The result indicates the export has started; use 'get_analytical_ledger_export_status' to check progress and get the download URL.",
            arguments=types.ObjectSchema(
                required=["company_id", "period_start", "period_end"],
                properties={
                    "company_id": types.IntegerSchema(description="The unique Pennylane identifier for the company."),
                    "period_start": types.StringSchema(description="Start date of the period to export (format: YYYY-MM-DD)."),
                    "period_end": types.StringSchema(description="End date of the period to export (format: YYYY-MM-DD)."),
                    "mode": types.StringSchema(description="The mode of the export. Determines if the export is in lines or in columns. Defaults to 'in_line' if not provided.", nullable=True, enum=["in_line", "in_column"])
                }
            ),
            returns=types.ObjectSchema(
                properties={
                    "export_initiation_data": types.StringSchema(description="JSON string containing details of the initiated export, including its 'id' (needed for status checks), 'status' ('pending', 'ready', or 'error'), 'created_at', and 'updated_at'.")
                }
            )
        ),
        types.Tool(
            name="get_analytical_ledger_export_status",
            description="Retrieves the current status and, if completed, the download URL for a previously initiated Analytical General Ledger export. The download URL is valid for 30 minutes.",
            arguments=types.ObjectSchema(
                required=["company_id", "export_id"],
                properties={
                    "company_id": types.IntegerSchema(description="The unique Pennylane identifier for the company."),
                    "export_id": types.IntegerSchema(description="The unique identifier of the export, obtained when the export was created using 'create_analytical_ledger_export'.")
                }
            ),
            returns=types.ObjectSchema(
                properties={
                    "export_status_data": types.StringSchema(description="JSON string containing the export's 'id', 'status' ('pending', 'done', or 'error'), 'file_url' (if 'done', null otherwise), 'created_at', and 'updated_at'.")
                }
            )
        ),
        types.Tool(
            name="create_fec_export",
            description="Initiates an asynchronous FEC (Fichier des Écritures Comptables) export for a company over a specified period. The result indicates the export has started; use 'get_fec_export_status' to check progress and get the download URL.",
            arguments=types.ObjectSchema(
                required=["company_id", "period_start", "period_end"],
                properties={
                    "company_id": types.IntegerSchema(description="The unique Pennylane identifier for the company."),
                    "period_start": types.StringSchema(description="Start date of the period for the FEC export (format: YYYY-MM-DD)."),
                    "period_end": types.StringSchema(description="End date of the period for the FEC export (format: YYYY-MM-DD).")
                }
            ),
            returns=types.ObjectSchema(
                properties={
                    "export_initiation_data": types.StringSchema(description="JSON string containing details of the initiated FEC export, including its 'id' (needed for status checks), 'status' ('pending', 'ready', or 'error'), 'created_at', and 'updated_at'.")
                }
            )
        ),
        types.Tool(
            name="get_fec_export_status",
            description="Retrieves the current status and, if completed, the download URL for a previously initiated FEC export. The download URL is valid for 30 minutes.",
            arguments=types.ObjectSchema(
                required=["company_id", "export_id"],
                properties={
                    "company_id": types.IntegerSchema(description="The unique Pennylane identifier for the company."),
                    "export_id": types.IntegerSchema(description="The unique identifier of the FEC export, obtained when the export was created using 'create_fec_export'.")
                }
            ),
            returns=types.ObjectSchema(
                properties={
                    "export_status_data": types.StringSchema(description="JSON string containing the FEC export's 'id', 'status' ('pending', 'done', or 'error'), 'file_url' (if 'done', null otherwise), 'created_at', and 'updated_at'.")
                }
            )
        )
    ]

@app.call_tool()
async def call_pennylane_tool(name: str, arguments: dict | None = None) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    logger.info(f"Call tool requested: {name} with arguments: {arguments}")
    arguments = arguments or {}

    if name == "list_companies":
        page = arguments.get("page")
        per_page = arguments.get("per_page")
        
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page

        try:
            async with await get_pennylane_client() as client:
                response = await client.get("/companies", params=params)
                response.raise_for_status() # Raise an exception for HTTP errors 4xx/5xx
                companies_data = response.json()
                # For now, returning as a JSON string within TextContent
                # Ideally, this would be a more structured response, possibly using EmbeddedResource
                # if the data is complex or needs to be referenced later.
                return [types.TextContent(text=f"Successfully listed companies: {companies_data}")]
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error calling Pennylane API for list_companies: {e.response.status_code} - {e.response.text}")
            # Propagate a structured error to the MCP client
            raise types.McpError(types.ErrorCode.UpstreamError, f"Pennylane API error: {e.response.status_code} - {e.response.text}") from e
        except httpx.RequestError as e:
            logger.error(f"Request error calling Pennylane API for list_companies: {e}")
            raise types.McpError(types.ErrorCode.UpstreamError, f"Could not connect to Pennylane API: {e}") from e
        except Exception as e:
            logger.error(f"Unexpected error in list_companies tool: {e}", exc_info=True)
            raise types.McpError(types.ErrorCode.InternalError, f"An unexpected error occurred: {str(e)}") from e

    elif name == "show_company_details":
        company_id = arguments.get("company_id")
        if company_id is None:
            raise types.McpError(types.ErrorCode.InvalidParams, "Missing required argument: company_id")

        try:
            async with await get_pennylane_client() as client:
                response = await client.get(f"/companies/{company_id}")
                response.raise_for_status()
                company_data = response.json()
                return [types.TextContent(text=f"Successfully retrieved company details: {company_data}")]
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error calling Pennylane API for show_company_details: {e.response.status_code} - {e.response.text}")
            if e.response.status_code == 404:
                raise types.McpError(types.ErrorCode.NotFound, f"Company with ID {company_id} not found.") from e
            raise types.McpError(types.ErrorCode.UpstreamError, f"Pennylane API error: {e.response.status_code} - {e.response.text}") from e
        except httpx.RequestError as e:
            logger.error(f"Request error calling Pennylane API for show_company_details: {e}")
            raise types.McpError(types.ErrorCode.UpstreamError, f"Could not connect to Pennylane API: {e}") from e
        except Exception as e:
            logger.error(f"Unexpected error in show_company_details tool: {e}", exc_info=True)
            raise types.McpError(types.ErrorCode.InternalError, f"An unexpected error occurred: {str(e)}") from e

    elif name == "list_dms_files":
        company_id = arguments.get("company_id")
        if company_id is None:
            raise types.McpError(types.ErrorCode.InvalidParams, "Missing required argument: company_id")

        params = {}
        cursor = arguments.get("cursor")
        limit = arguments.get("limit")
        filter_id_op = arguments.get("filter_id_operation")
        filter_id_val = arguments.get("filter_id_value")

        if cursor:
            params["cursor"] = cursor
        if limit is not None:
            params["limit"] = limit
        
        # Basic filter construction: id[op]=value
        # Pennylane API: filter[id][eq]=value
        # This is a simplified version. A more robust implementation would handle various ops and potentially multiple filters.
        if filter_id_op and filter_id_val is not None:
            params[f"filter[id][{filter_id_op}]"] = filter_id_val
            
        try:
            async with await get_pennylane_client() as client:
                response = await client.get(f"/companies/{company_id}/dms/files", params=params)
                response.raise_for_status()
                dms_files_data = response.json()
                return [types.TextContent(text=f"Successfully listed DMS files: {dms_files_data}")]
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error calling Pennylane API for list_dms_files: {e.response.status_code} - {e.response.text}")
            if e.response.status_code == 404:
                raise types.McpError(types.ErrorCode.NotFound, f"Company with ID {company_id} not found or DMS files endpoint not found for it.") from e
            raise types.McpError(types.ErrorCode.UpstreamError, f"Pennylane API error: {e.response.status_code} - {e.response.text}") from e
        except httpx.RequestError as e:
            logger.error(f"Request error calling Pennylane API for list_dms_files: {e}")
            raise types.McpError(types.ErrorCode.UpstreamError, f"Could not connect to Pennylane API: {e}") from e
        except Exception as e:
            logger.error(f"Unexpected error in list_dms_files tool: {e}", exc_info=True)
            raise types.McpError(types.ErrorCode.InternalError, f"An unexpected error occurred: {str(e)}") from e

    elif name == "get_dms_file_changes":
        company_id = arguments.get("company_id")
        if company_id is None:
            raise types.McpError(types.ErrorCode.InvalidParams, "Missing required argument: company_id")

        params = {}
        cursor = arguments.get("cursor")
        limit = arguments.get("limit")
        start_date = arguments.get("start_date")

        if cursor:
            params["cursor"] = cursor
        if limit is not None:
            params["limit"] = limit
        if start_date:
            params["start_date"] = start_date
            if cursor: # API constraint: Cannot use both start_date and cursor
                raise types.McpError(types.ErrorCode.InvalidParams, "Cannot use both 'start_date' and 'cursor' parameters simultaneously.")

        try:
            async with await get_pennylane_client() as client:
                response = await client.get(f"/companies/{company_id}/changelogs/dms_files", params=params)
                response.raise_for_status()
                dms_changes_data = response.json()
                return [types.TextContent(text=f"Successfully retrieved DMS file changes: {dms_changes_data}")]
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error calling Pennylane API for get_dms_file_changes: {e.response.status_code} - {e.response.text}")
            if e.response.status_code == 404:
                raise types.McpError(types.ErrorCode.NotFound, f"Company with ID {company_id} not found or changelog endpoint not found.") from e
            if e.response.status_code == 422: # Unprocessable entity, e.g., start_date too old
                 raise types.McpError(types.ErrorCode.InvalidParams, f"Unprocessable request for DMS file changes (e.g., start_date too old or invalid): {e.response.text}") from e
            if e.response.status_code == 400: # Bad request, e.g. using cursor and start_date
                 raise types.McpError(types.ErrorCode.InvalidParams, f"Bad request for DMS file changes (e.g. using cursor and start_date together): {e.response.text}") from e
            raise types.McpError(types.ErrorCode.UpstreamError, f"Pennylane API error: {e.response.status_code} - {e.response.text}") from e
        except httpx.RequestError as e:
            logger.error(f"Request error calling Pennylane API for get_dms_file_changes: {e}")
            raise types.McpError(types.ErrorCode.UpstreamError, f"Could not connect to Pennylane API: {e}") from e
        except Exception as e:
            logger.error(f"Unexpected error in get_dms_file_changes tool: {e}", exc_info=True)
            raise types.McpError(types.ErrorCode.InternalError, f"An unexpected error occurred: {str(e)}") from e

    elif name == "list_fiscal_years":
        company_id = arguments.get("company_id")
        if company_id is None:
            raise types.McpError(types.ErrorCode.InvalidParams, "Missing required argument: company_id")

        params = {}
        page = arguments.get("page")
        per_page = arguments.get("per_page")

        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page

        try:
            async with await get_pennylane_client() as client:
                response = await client.get(f"/companies/{company_id}/fiscal_years", params=params)
                response.raise_for_status()
                fiscal_years_data = response.json()
                return [types.TextContent(text=f"Successfully listed fiscal years: {fiscal_years_data}")]
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error calling Pennylane API for list_fiscal_years: {e.response.status_code} - {e.response.text}")
            if e.response.status_code == 404:
                raise types.McpError(types.ErrorCode.NotFound, f"Company with ID {company_id} not found or fiscal years endpoint not found.") from e
            raise types.McpError(types.ErrorCode.UpstreamError, f"Pennylane API error: {e.response.status_code} - {e.response.text}") from e
        except httpx.RequestError as e:
            logger.error(f"Request error calling Pennylane API for list_fiscal_years: {e}")
            raise types.McpError(types.ErrorCode.UpstreamError, f"Could not connect to Pennylane API: {e}") from e
        except Exception as e:
            logger.error(f"Unexpected error in list_fiscal_years tool: {e}", exc_info=True)
            raise types.McpError(types.ErrorCode.InternalError, f"An unexpected error occurred: {str(e)}") from e

    elif name == "get_trial_balance":
        company_id = arguments.get("company_id")
        period_start = arguments.get("period_start")
        period_end = arguments.get("period_end")

        if not all([company_id, period_start, period_end]):
            raise types.McpError(types.ErrorCode.InvalidParams, "Missing one or more required arguments: company_id, period_start, period_end")

        params = {
            "period_start": period_start,
            "period_end": period_end
        }
        is_auxiliary = arguments.get("is_auxiliary")
        page = arguments.get("page")
        per_page = arguments.get("per_page")

        if is_auxiliary is not None:
            params["is_auxiliary"] = is_auxiliary
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page

        try:
            async with await get_pennylane_client() as client:
                response = await client.get(f"/companies/{company_id}/trial_balance", params=params)
                response.raise_for_status()
                trial_balance_data = response.json()
                return [types.TextContent(text=f"Successfully retrieved trial balance: {trial_balance_data}")]
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error calling Pennylane API for get_trial_balance: {e.response.status_code} - {e.response.text}")
            if e.response.status_code == 404:
                raise types.McpError(types.ErrorCode.NotFound, f"Company with ID {company_id} not found or trial balance endpoint not found.") from e
            if e.response.status_code == 422: # Unprocessable Entity
                raise types.McpError(types.ErrorCode.InvalidParams, f"Unprocessable request for trial balance (e.g., invalid period): {e.response.text}") from e
            raise types.McpError(types.ErrorCode.UpstreamError, f"Pennylane API error: {e.response.status_code} - {e.response.text}") from e
        except httpx.RequestError as e:
            logger.error(f"Request error calling Pennylane API for get_trial_balance: {e}")
            raise types.McpError(types.ErrorCode.UpstreamError, f"Could not connect to Pennylane API: {e}") from e
        except Exception as e:
            logger.error(f"Unexpected error in get_trial_balance tool: {e}", exc_info=True)
            raise types.McpError(types.ErrorCode.InternalError, f"An unexpected error occurred: {str(e)}") from e

    elif name == "create_analytical_ledger_export":
        company_id = arguments.get("company_id")
        period_start = arguments.get("period_start")
        period_end = arguments.get("period_end")

        if not all([company_id, period_start, period_end]):
            raise types.McpError(types.ErrorCode.InvalidParams, "Missing one or more required arguments: company_id, period_start, period_end")

        payload = {
            "period_start": period_start,
            "period_end": period_end
        }
        mode = arguments.get("mode")
        if mode:
            payload["mode"] = mode

        try:
            async with await get_pennylane_client() as client:
                response = await client.post(f"/companies/{company_id}/exports/analytical_general_ledgers", json=payload)
                response.raise_for_status() # Successful creation is usually 201
                export_init_data = response.json()
                return [types.TextContent(text=f"Successfully initiated Analytical General Ledger export: {export_init_data}")]
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error calling Pennylane API for create_analytical_ledger_export: {e.response.status_code} - {e.response.text}")
            if e.response.status_code == 404:
                raise types.McpError(types.ErrorCode.NotFound, f"Company with ID {company_id} not found or export endpoint not found.") from e
            if e.response.status_code == 400: # Bad Request by API for invalid parameters
                 raise types.McpError(types.ErrorCode.InvalidParams, f"Invalid parameters for creating Analytical General Ledger export: {e.response.text}") from e
            # Add other specific error code handling if known (e.g., 422)
            raise types.McpError(types.ErrorCode.UpstreamError, f"Pennylane API error: {e.response.status_code} - {e.response.text}") from e
        except httpx.RequestError as e:
            logger.error(f"Request error calling Pennylane API for create_analytical_ledger_export: {e}")
            raise types.McpError(types.ErrorCode.UpstreamError, f"Could not connect to Pennylane API: {e}") from e
        except Exception as e:
            logger.error(f"Unexpected error in create_analytical_ledger_export tool: {e}", exc_info=True)
            raise types.McpError(types.ErrorCode.InternalError, f"An unexpected error occurred: {str(e)}") from e

    elif name == "get_analytical_ledger_export_status":
        company_id = arguments.get("company_id")
        export_id = arguments.get("export_id")

        if not all([company_id, export_id]):
            raise types.McpError(types.ErrorCode.InvalidParams, "Missing one or more required arguments: company_id, export_id")

        try:
            async with await get_pennylane_client() as client:
                response = await client.get(f"/companies/{company_id}/exports/analytical_general_ledgers/{export_id}")
                response.raise_for_status()
                export_status_data = response.json()
                return [types.TextContent(text=f"Successfully retrieved Analytical General Ledger export status: {export_status_data}")]
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error calling Pennylane API for get_analytical_ledger_export_status: {e.response.status_code} - {e.response.text}")
            if e.response.status_code == 404:
                raise types.McpError(types.ErrorCode.NotFound, f"Company ID {company_id} or Export ID {export_id} not found.") from e
            # Add other specific error code handling if known
            raise types.McpError(types.ErrorCode.UpstreamError, f"Pennylane API error: {e.response.status_code} - {e.response.text}") from e
        except httpx.RequestError as e:
            logger.error(f"Request error calling Pennylane API for get_analytical_ledger_export_status: {e}")
            raise types.McpError(types.ErrorCode.UpstreamError, f"Could not connect to Pennylane API: {e}") from e
        except Exception as e:
            logger.error(f"Unexpected error in get_analytical_ledger_export_status tool: {e}", exc_info=True)
            raise types.McpError(types.ErrorCode.InternalError, f"An unexpected error occurred: {str(e)}") from e

    elif name == "create_fec_export":
        company_id = arguments.get("company_id")
        period_start = arguments.get("period_start")
        period_end = arguments.get("period_end")

        if not all([company_id, period_start, period_end]):
            raise types.McpError(types.ErrorCode.InvalidParams, "Missing one or more required arguments: company_id, period_start, period_end")

        payload = {
            "period_start": period_start,
            "period_end": period_end
        }

        try:
            async with await get_pennylane_client() as client:
                response = await client.post(f"/companies/{company_id}/exports/fecs", json=payload)
                response.raise_for_status() # Successful creation is usually 201
                export_init_data = response.json()
                return [types.TextContent(text=f"Successfully initiated FEC export: {export_init_data}")]
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error calling Pennylane API for create_fec_export: {e.response.status_code} - {e.response.text}")
            if e.response.status_code == 404:
                raise types.McpError(types.ErrorCode.NotFound, f"Company with ID {company_id} not found or FEC export endpoint not found.") from e
            if e.response.status_code == 400: # Bad Request by API for invalid parameters
                 raise types.McpError(types.ErrorCode.InvalidParams, f"Invalid parameters for creating FEC export: {e.response.text}") from e
            # Add other specific error code handling if known (e.g., 422 for invalid period)
            raise types.McpError(types.ErrorCode.UpstreamError, f"Pennylane API error: {e.response.status_code} - {e.response.text}") from e
        except httpx.RequestError as e:
            logger.error(f"Request error calling Pennylane API for create_fec_export: {e}")
            raise types.McpError(types.ErrorCode.UpstreamError, f"Could not connect to Pennylane API: {e}") from e
        except Exception as e:
            logger.error(f"Unexpected error in create_fec_export tool: {e}", exc_info=True)
            raise types.McpError(types.ErrorCode.InternalError, f"An unexpected error occurred: {str(e)}") from e

    elif name == "get_fec_export_status":
        company_id = arguments.get("company_id")
        export_id = arguments.get("export_id")

        if not all([company_id, export_id]):
            raise types.McpError(types.ErrorCode.InvalidParams, "Missing one or more required arguments: company_id, export_id")

        try:
            async with await get_pennylane_client() as client:
                response = await client.get(f"/companies/{company_id}/exports/fecs/{export_id}")
                response.raise_for_status()
                export_status_data = response.json()
                return [types.TextContent(text=f"Successfully retrieved FEC export status: {export_status_data}")]
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error calling Pennylane API for get_fec_export_status: {e.response.status_code} - {e.response.text}")
            if e.response.status_code == 404:
                raise types.McpError(types.ErrorCode.NotFound, f"Company ID {company_id} or FEC Export ID {export_id} not found.") from e
            raise types.McpError(types.ErrorCode.UpstreamError, f"Pennylane API error: {e.response.status_code} - {e.response.text}") from e
        except httpx.RequestError as e:
            logger.error(f"Request error calling Pennylane API for get_fec_export_status: {e}")
            raise types.McpError(types.ErrorCode.UpstreamError, f"Could not connect to Pennylane API: {e}") from e
        except Exception as e:
            logger.error(f"Unexpected error in get_fec_export_status tool: {e}", exc_info=True)
            raise types.McpError(types.ErrorCode.InternalError, f"An unexpected error occurred: {str(e)}") from e

    raise types.McpError(types.ErrorCode.MethodNotFound, f"Tool '{name}' not implemented yet.")

# --- Main function to run the server ---
async def main_async():
    logger.info("Starting Pennylane MCP server...")
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        # Capabilities will be expanded as we implement features
        capabilities = app.get_capabilities(
            notification_options=NotificationOptions(),
            experimental_capabilities={}
        )
        # Ensure all required capabilities like 'resources' and 'tools' are declared
        # based on the implemented handlers.
        if not capabilities.resources:
            capabilities.resources = types.ResourceProviderCapabilities()
        if not capabilities.tools:
            capabilities.tools = types.ToolProviderCapabilities()

        await app.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name=app.name, # Use the name defined in Server()
                server_version="0.1.0",
                capabilities=capabilities
            )
        )
    logger.info("Pennylane MCP server stopped.")

def main():
    try:
        asyncio.run(main_async())
    except KeyboardInterrupt:
        logger.info("Server shutdown requested by user.")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}", exc_info=True) 