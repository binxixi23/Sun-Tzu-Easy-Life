import streamlit as st
import json
from main import SunTzuEasyLife
from streamlit_mermaid import st_mermaid

# Page Configuration
st.set_page_config(page_title="Sun Tzu Easy Life", page_icon="🏛️", layout="wide")

# Initialize the Agent (cached so it doesn't reload every time)
@st.cache_resource
def load_agent():
    return SunTzuEasyLife()

agent = load_agent()

# Sidebar - Digital Military Academy Info
with st.sidebar:
    st.title("🏛️ Academy Command")
    st.info("Applying ancient strategy to modern life.")
    if st.button("Clear Battle History"):
        st.session_state.messages = []
        st.rerun()

st.title("Sun Tzu_Easy_Life: Digital Sovereign")
st.markdown("---")

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "visual" in message:
            st_mermaid(message["visual"])

# User Input
if prompt := st.chat_input("State your conflict, Commander..."):
    # Display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Agent Processing
    with st.chat_message("assistant"):
        with st.spinner("The General is analyzing the terrain..."):
            result = agent.execute_command(prompt)
            
            if "Shortcut_Advice" in result:
                response_text = result["Shortcut_Advice"]
                st.markdown(response_text)
                st.session_state.messages.append({"role": "assistant", "content": response_text})
            else:
                # Beautifully format the strategic response
                response_text = f"""
### 🎭 Theater: {result['Theater']}
**Strategic Pillar:** {result['General_Strategy']}

**Tactical Maneuver:** {result['Tactical_Maneuver']}

---
**💡 Live Intel:** {", ".join(result['Live_Signals']) if result['Live_Signals'] else "No news detected."}

**🧠 Experience:** {result['Past_Experience']}

---
*"{result['Sage_Closing']}"*
                """
                st.markdown(response_text)
                
                # Display Mermaid Chart
                mermaid_code = result['Visual_Map'].replace("```mermaid", "").replace("```", "")
                st_mermaid(mermaid_code)
                
                # Save to history
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": response_text,
                    "visual": mermaid_code
                })
