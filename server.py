from fastmcp import FastMCP

mcp = FastMCP("Echo Tool")

@mcp.tool()
def echo(message: str) -> str:
    """Echoes back what the user says."""
    return f"You said: {message}"

if __name__ == "__main__":
    mcp.run()
