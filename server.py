from fastmcp import FastMCP

mcp = FastMCP("Echo Tool")

@mcp.tool()
def echo(message: str) -> str:
    """Echoes back what the user says."""
    return f"You said: {message}"

if __name__ == "__main__":
    # Run the HTTP server on Render's expected port
    import os
    port = int(os.environ.get("PORT", 10000))
    mcp.run_http(port=port)
