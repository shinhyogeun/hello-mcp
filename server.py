"""KAF Git 소스 빌드용 최소 MCP 서버 — Streamable HTTP, 포트 8000, 경로 /mcp."""
from datetime import datetime, timezone, timedelta

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("hello-mcp", host="0.0.0.0", port=8000, stateless_http=True)


@mcp.tool()
def add(a: float, b: float) -> float:
    """두 숫자를 더한다."""
    return a + b


@mcp.tool()
def greet(name: str) -> str:
    """이름을 받아 인사말을 돌려준다."""
    return f"안녕하세요, {name}님!"


@mcp.tool()
def now_kst() -> str:
    """지금 한국 시각을 ISO 형식으로 돌려준다."""
    return datetime.now(timezone(timedelta(hours=9))).isoformat(timespec="seconds")


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
