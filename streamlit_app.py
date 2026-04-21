import streamlit as st
import os
import subprocess
import sys

st.set_page_config(page_title="MCP工具箱", layout="wide")

st.title("🛠️ MCP工具箱 - 文件系统与计算器")

# 初始化
if "server_process" not in st.session_state:
    st.session_state.server_process = None

# 侧边栏
with st.sidebar:
    st.header("控制面板")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("▶️ 启动MCP服务器", use_container_width=True):
            try:
                process = subprocess.Popen(
                    [sys.executable, "mcp_server.py"],
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0
                )
                st.session_state.server_process = process
                st.success("✅ MCP服务器已启动")
                st.rerun()
            except Exception as e:
                st.error(f"启动失败: {e}")

    with col2:
        if st.button("⏹️ 停止MCP服务器", use_container_width=True):
            if st.session_state.server_process:
                st.session_state.server_process.terminate()
                st.session_state.server_process = None
                st.success("服务器已停止")
                st.rerun()

    if st.session_state.server_process:
        st.success("状态: 🟢 运行中")
    else:
        st.warning("状态: 🔴 未启动")

# 计算器
st.header("🧮 计算器")
col1, col2, col3 = st.columns(3)
with col1:
    a = st.number_input("数字 A", value=10.0)
with col2:
    op = st.selectbox("运算符", ["+", "-", "*", "/"])
with col3:
    b = st.number_input("数字 B", value=5.0)

if st.button("计算", type="primary"):
    if st.session_state.server_process:
        # 模拟MCP调用
        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = a / b if b != 0 else "除数不能为0"
        st.success(f"### {a} {op} {b} = {result}")
    else:
        st.warning("请先启动MCP服务器")

# 文件系统
st.header("📁 文件系统")
if st.button("获取桌面文件列表"):
    if st.session_state.server_process:
        desktop = os.path.expanduser("~/Desktop")
        if os.path.exists(desktop):
            files = os.listdir(desktop)
            st.write(f"找到 {len(files)} 个文件/文件夹：")
            for f in files[:20]:
                st.write(f"- {f}")
        else:
            st.info("桌面路径不存在")
    else:
        st.warning("请先启动MCP服务器")

st.markdown("---")
st.caption("MCP协议演示 - 客户端通过stdio与服务器通信")