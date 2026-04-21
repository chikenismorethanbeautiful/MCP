import subprocess
import sys
import os
import webbrowser
import time


def main():
    # 检查是否安装了streamlit
    try:
        import streamlit
    except ImportError:
        print("正在安装streamlit...")
        subprocess.run([sys.executable, "-m", "pip", "install", "streamlit", "mcp"])

    # 获取当前目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    app_path = os.path.join(current_dir, "streamlit_app.py")

    # 启动streamlit
    print("启动MCP工具箱...")
    webbrowser.open("http://localhost:8501")

    # 运行streamlit
    subprocess.run([sys.executable, "-m", "streamlit", "run", app_path])


if __name__ == "__main__":
    main()