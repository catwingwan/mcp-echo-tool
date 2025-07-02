from fastmcp import FastMCP
import os

mcp = FastMCP("Echo Tool")

@mcp.tool()
def echo(message: str) -> str:
    """Echoes back what the user says."""
    return f"You said: {message}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    # Use HTTP transport so Render can expose a public URL
    # mcp.run(transport="http", host="0.0.0.0", port=port) ## old
    mcp.run(transport="streamable-http", host="0.0.0.0", port=port)


