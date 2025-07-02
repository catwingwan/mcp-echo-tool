from mcp import Tool, Input, Output
from mcp.server import Server
import echo_tool
import summarizer_tool

echo = Tool(
    name="echo",
    description="Repeats your message",
    inputs={"message": Input(type="string")},
    outputs={"result": Output(type="string")},
    run=echo_tool.run
)

summarizer = Tool(
    name="summarize",
    description="Summarizes a block of text",
    inputs={"text": Input(type="string")},
    outputs={"summary": Output(type="string")},
    run=summarizer_tool.run
)

mcp = Server(tools=[echo, summarizer])

# IMPORTANT: Set streamable transport for Render
mcp.run(transport="streamable-http", host="0.0.0.0", port=8000)
