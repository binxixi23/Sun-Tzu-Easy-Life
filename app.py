import streamlit as st
import json
import os
from main import SunTzuEasyLife
from streamlit_mermaid import st_mermaid

# 🏛️ Cấu hình giao diện Web
st.set_page_config(
    page_title="Sun Tzu_Easy_Life: Digital Sovereign",
    page_icon="🏛️",
    layout="wide"
)

# 🧠 Khởi tạo Quân sư (Dùng cache để không phải load lại mỗi lần chat)
@st.cache_resource
def init_agent():
    return SunTzuEasyLife()

agent = init_agent()

# --- GIAO DIỆN BÊN TRÁI (SIDEBAR) ---
with st.sidebar:
    st.image("https://icons8.com", width=100)
    st.title("Học Viện Quân Sự Số")
    st.markdown("""
    **Sun Tzu_Easy_Life** biến binh pháp cổ xưa thành giải pháp hiện đại cho:
    - 💰 Tài chính & Làm ăn
    - 🎭 Chính trị & Giao tiếp
    - ❤️ Tình cảm & Gia đình
    - 🌿 Sức khỏe & Quy luật
    """)
    if st.button("Xóa lịch sử trận đánh"):
        st.session_state.messages = []
        st.rerun()

# --- GIAO DIỆN CHÍNH (MAIN CHAT) ---
st.title("🏛️ Sun Tzu_Easy_Life: Digital Sovereign")
st.caption("Hãy trình bày thế trận của bạn, Quân sư đang đợi lệnh.")

# Khởi tạo lịch sử tin nhắn
if "messages" not in st.session_state:
    st.session_state.messages = []

# Hiển thị các tin nhắn cũ
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "visual" in message:
            st_mermaid(message["visual"])

# Ô nhập liệu cho khách hàng
if prompt := st.chat_input("Nhập vấn đề của bạn tại đây..."):
    # 1. Hiển thị tin nhắn của khách
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Quân sư lập kế
    with st.chat_message("assistant"):
        with st.spinner("Quân sư đang đọc binh pháp và phân tích thế trận..."):
            result = agent.execute_command(prompt)
            
            if "Shortcut_Advice" in result:
                response = result["Shortcut_Advice"]
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            else:
                # Trình bày kế sách AI
                ai_counsel = result.get("Sun_Tzu_Counsel", "Không thể kết nối bộ não AI.")
                closing = result.get("Sage_Closing", "")
                theater = result.get("Theater", "GENERAL")

                full_response = f"**THẾ TRẬN:** {theater}\n\n{ai_counsel}\n\n---\n*💡 Lời bình: {closing}*"
                st.markdown(full_response)
                
                # Vẽ sơ đồ Mermaid (Lấy mã từ AI response nếu có, hoặc dùng visualizer cũ)
                # Ở đây chúng ta lấy sơ đồ từ visualizer_agent đã tích hợp trong result
                mermaid_code = result.get("Visual_Map", "").replace("```mermaid", "").replace("```", "")
                if mermaid_code:
                    st_mermaid(mermaid_code)
                
                # Lưu vào lịch sử
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": full_response,
                    "visual": mermaid_code
                })
