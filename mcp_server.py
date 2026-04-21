import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("FileSystem")  # 服务名称


@mcp.tool()
def get_desktop_files() -> list:
    """获取当前用户的桌面文件列表"""
    # 修复：使用 ~/Desktop 而不是 /Desktop（/Desktop在Windows/Mac上不存在）
    return os.listdir(os.path.expanduser("~/Desktop"))


@mcp.tool()
def calculator(a: float, b: float, operator: str) -> float:
    """执行基础数学运算（支持+-*/）

    Args:
        a: 第一个数字
        b: 第二个数字
        operator: 运算符，必须是'+', '-', '*', '/'之一
    """
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            raise ValueError("除数不能为零")
        return a / b
    else:
        raise ValueError("无效运算符")


if __name__ == "__main__":
    mcp.run(transport='stdio')  # 使用标准输入输出通信