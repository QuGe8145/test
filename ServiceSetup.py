"""
模块名称：ServiceSetup.py
作者：曲歌
创建日期：2025年12月15日
描述：MCP 服务器的搭建(MCP 服务器的核心是定义工具)
版本：1.0.0
"""
from fastmcp import FastMCP

# 创建 MCP 服务器实例
mcp = FastMCP("MathTools")


@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    """添加两个数字"""
    return a + b


@mcp.tool()
def multiply_numbers(a: float, b: float) -> float:
    """乘两个数字"""
    return a * b


@mcp.tool()
def exponentiate(base: float, exp: float) -> float:
    """计算基数的指数幂"""
    return base ** exp

if __name__ == "__main__":
    # 启动服务器，可以选择 stdio 或 http
    # 对于 stdio：
    # mcp.run(transport="stdio")
    # 对于 Streamable HTTP：mcp.run(transport="http", host="0.0.0.0", port=8000)
    mcp.run(transport="http", host="0.0.0.0", port=8000)  # 示例使用 HTTP
