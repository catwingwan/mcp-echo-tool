from mcp.tool import Tool
from mcp.server import Server
from mcp.types import Input, Output


@Tool(name="echo", description="Echoes back what the user says.")
def echo_tool(input: Input) -> Output:
    return Output(text=f"You said: {input.text}")

if __name__ == "__main__":
    # Start HTTP server on port 5000
    Server.register(echo_tool).run_http(port=5000)
