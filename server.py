from modelcontextprotocol import Tool, Input, Output, Server
import echo_tool
import summarizer_tool

echo = Tool(
    name="echo",
    description="Repeats your message",
    inputs={"message": Input(type="string")},
    outputs={"result": Output(type="string")},
    run=echo_tool.run
)

summarize = Tool(
    name="summarize",
    description="Summarizes a block of text",
    inputs={"text": Input(type="string")},
    outputs={"summary": Output(type="string")},
    run=summarizer_tool.run
)

server = Server(tools=[echo, summarize])
server.run(transport="streamable-http", host="0.0.0.0", port=8000)
