"""Example of using the FastMCP client to connect to a Pennylane MCP server via HTTP."""

import asyncio
import logging
from fastmcp import Client

# Configure logging
logging.basicConfig(level=logging.INFO)


async def test_http_connection():
    """Test connection to Pennylane MCP server via Streamable HTTP."""
    
    # Connect to the server running on HTTP
    # Make sure the server is running with:
    # python src/server.py --transport streamable-http --port 9000
    
    server_url = "http://localhost:9000/"
    
    print(f"Connecting to Pennylane MCP server at {server_url}...")
    
    async with Client(server_url) as client:
        print("✅ Connected successfully!")
        
        # Test server info
        print("\n1. Getting server information...")
        result = await client.call_tool("pennylane_server_info")
        print(f"Server info: {result[0].text}")
        
        # List available tools
        print("\n2. Listing available tools...")
        tools = await client.list_tools()
        print(f"Found {len(tools)} tools")
        
        # Show a few tool names
        for i, tool in enumerate(tools[:5]):
            print(f"  - {tool.name}: {tool.description}")
        if len(tools) > 5:
            print(f"  ... and {len(tools) - 5} more")
        
        # Test listing customers
        print("\n3. Testing customer list...")
        try:
            result = await client.call_tool("pennylane_customers_list", {"limit": 5})
            print(f"Customer list result: {result[0].text[:200]}...")
        except Exception as e:
            print(f"Error listing customers: {e}")
        
        # Test listing products
        print("\n4. Testing product list...")
        try:
            result = await client.call_tool("pennylane_products_list", {"limit": 3})
            print(f"Product list result: {result[0].text[:200]}...")
        except Exception as e:
            print(f"Error listing products: {e}")


async def test_health_endpoint():
    """Test the health check endpoint."""
    import httpx
    
    print("\n5. Testing health check endpoint...")
    async with httpx.AsyncClient() as http_client:
        response = await http_client.get("http://localhost:9000/health")
        if response.status_code == 200:
            print(f"✅ Health check passed: {response.json()}")
        else:
            print(f"❌ Health check failed: {response.status_code}")


async def main():
    """Run all tests."""
    print("=" * 60)
    print("Pennylane MCP HTTP Client Example")
    print("=" * 60)
    print("\nMake sure the server is running with:")
    print("  python src/server.py --transport streamable-http --port 9000")
    print("=" * 60)
    
    try:
        await test_http_connection()
        await test_health_endpoint()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nMake sure the server is running in HTTP mode!")


if __name__ == "__main__":
    asyncio.run(main()) 