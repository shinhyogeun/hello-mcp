# hello-mcp

KAF 「MCP Server 생성 → Git 소스 빌드」 로 올려 보는 최소 MCP 서버.

- 전송: Streamable HTTP, 경로 `/mcp`, 포트 8000
- 도구: `add` · `greet` · `now_kst`

로컬 실행: `docker build -t hello-mcp . && docker run -p 8000:8000 hello-mcp`
