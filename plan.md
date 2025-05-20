# Pennylane MCP Development Plan

## 1. Project Setup & Initial Configuration

*   **1.1. Define Core MCP Structure:** Based on the (yet to be fully reviewed) `model-context-protocol.md`, establish the foundational directory structure and essential configuration files for the MCP.
*   **1.2. Environment Setup:**
    *   Set up a virtual environment.
    *   Install necessary base libraries (e.g., `requests` for API calls, potentially a linting/formatting tool).
*   **1.3. API Client Scaffolding:**
    *   Create a basic Python client or module to handle requests to the Pennylane API.
    *   Implement secure handling of API credentials (Bearer token).
    *   Implement a mechanism to respect the 4 requests/second rate limit.

## 2. Tool/Function Implementation (Based on Pennylane API)

For each major Pennylane API entity/endpoint group, develop corresponding tools/functions within the MCP. Each tool should:
    *   Take relevant parameters (e.g., company ID, date ranges).
    *   Call the appropriate Pennylane API endpoint.
    *   Handle API responses, including success and error cases (4xx, 5xx).
    *   Format the data into a user-friendly and Claude-consumable format.
    *   Provide clear explanations of its actions and results.

*   **2.1. Companies:**
    *   `list_companies`: Implement tool to call `GET /companies`.
        *   Handle pagination (`page`, `per_page`).
    *   `show_company_details`: Implement tool to call `GET /companies/{id}`.
*   **2.2. DMS Files:**
    *   `list_dms_files`: Implement tool to call `GET /companies/{company_id}/dms/files`.
        *   Handle cursor-based pagination (`cursor`, `limit`).
        *   Handle filtering (`filter` by `id`).
    *   `get_dms_file_changes`: Implement tool to call `GET /companies/{company_id}/changelogs/dms_files`.
        *   Handle cursor-based pagination, `start_date`, and `limit`.
*   **2.3. Fiscal Years:**
    *   `list_fiscal_years`: Implement tool to call `GET /companies/{company_id}/fiscal_years`.
        *   Handle pagination.
*   **2.4. Trial Balance:**
    *   `get_trial_balance`: Implement tool to call `GET /companies/{company_id}/trial_balance`.
        *   Handle `period_start`, `period_end`, `is_auxiliary`, and pagination.
*   **2.5. Exports (Analytical General Ledger & FEC):**
    *   This will likely involve a two-step process for each export type: initiating the export and then checking its status/retrieving it.
    *   **2.5.1. Analytical General Ledger:**
        *   `create_analytical_ledger_export`: Tool for `POST /companies/{company_id}/exports/analytical_general_ledgers`.
            *   Parameters: `period_start`, `period_end`, `mode`.
        *   `get_analytical_ledger_export_status`: Tool for `GET /companies/{company_id}/exports/analytical_general_ledgers/{id}`.
            *   Handle polling for `status: done` and retrieving `file_url`.
    *   **2.5.2. FEC Exports:**
        *   `create_fec_export`: Tool for `POST /companies/{company_id}/exports/fecs`.
            *   Parameters: `period_start`, `period_end`.
        *   `get_fec_export_status`: Tool for `GET /companies/{company_id}/exports/fecs/{id}`.
            *   Handle polling for `status: done` and retrieving `file_url`.
*   **2.6. General API Utility:**
    *   Implement handling for scopes and ensure tools request/utilize appropriate scopes.

## 3. MCP Integration with Claude

*   **3.1. Prompt Engineering:**
    *   Design prompts that clearly instruct Claude on how to use the developed tools.
    *   Consider the "expert comptable" user persona: prompts should allow for natural language queries that accountants would use.
    *   Examples: "Liste les entreprises disponibles.", "Montre-moi les détails de l'entreprise X.", "Génère le FEC pour la société Y pour l'année 2023."
*   **3.2. Context Management:**
    *   Ensure the MCP provides sufficient context to Claude from API responses.
    *   Summarize or simplify complex API responses if necessary, while retaining essential information.
*   **3.3. Error Handling for Claude:**
    *   Translate API errors into understandable messages for Claude and, subsequently, the end-user.

## 4. Testing and Refinement

*   **4.1. Unit Tests:** Write unit tests for each individual tool/function to verify:
    *   Correct API call formation.
    *   Proper handling of API responses (success and errors).
    *   Data transformation logic.
*   **4.2. Integration Tests:**
    *   Test the end-to-end flow: user query -> Claude understanding -> MCP tool execution -> Pennylane API -> response to user.
    *   Test with various scenarios an "expert comptable" might encounter.
*   **4.3. User Acceptance Testing (Simulated):**
    *   Simulate queries from an "expert comptable" persona to evaluate usability and effectiveness.
*   **4.4. Refinement based on `model-context-protocol.md`:** Once the `model-context-protocol.md` is successfully read and understood, revisit all aspects of the plan and implementation to ensure full compliance and leverage any specific features or requirements of the protocol.

## 5. Documentation

*   **5.1. MCP Tool Documentation:** Document each tool, its parameters, expected output, and the Pennylane API endpoint it interacts with. This is crucial for Claude's understanding and effective use.
*   **5.2. User Guide (for "expert comptable"):** High-level guide on how to interact with the Pennylane MCP via Claude, with example queries.
*   **5.3. Developer Notes:** Document any complex logic, assumptions, or API specifics encountered.

## 6. Deployment and Maintenance

*   **6.1. Packaging:** Package the MCP as per the `model-context-protocol.md` guidelines.
*   **6.2. Versioning:** Implement a versioning strategy for the MCP.
*   **6.3. Monitoring and Updates:** Plan for monitoring the MCP's performance and updating it if the Pennylane API changes.

## Key Considerations / Potential Challenges:

*   **Rate Limiting:** Robustly implement request throttling or queuing to stay within the 4 requests/second limit.
*   **Asynchronous Operations (Exports):** Exports are asynchronous. The MCP will need to handle initiating an export and then polling for its completion. This might involve a stateful component or clear instructions for Claude on how to manage this flow (e.g., "I've started the export. Ask me for the status in a few moments using its ID: [export_id]").
*   **Error Propagation:** Clearly communicating API errors or MCP internal errors back to Claude and then to the user in an understandable way.
*   **Data Volume:** Some API responses might be large (e.g., trial balances, DMS file lists). The MCP might need to summarize or paginate data effectively for Claude.
*   **Authentication Token Management:** Securely store and refresh the Pennylane API token if necessary.
*   **`model-context-protocol.md` Adherence:** This plan is somewhat generic without full insight into this protocol. Significant adjustments may be needed.

This plan provides a structured approach. The next immediate step should be to resolve the issue reading `model-context-protocol.md` as it will heavily influence the specifics of the MCP implementation.
