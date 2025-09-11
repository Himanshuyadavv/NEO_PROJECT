import streamlit as st
from utils.rag_utils import SimpleRAG

# Page setup
st.set_page_config(page_title="NeoStats Chatbot", page_icon="🤖", layout="wide")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "rag" not in st.session_state:
    st.session_state.rag = None
if "mode" not in st.session_state:
    st.session_state.mode = "concise"

# Dark theme colors (fixed)
colors = {
    "bg": "#1a1a1a",
    "text": "#ffffff",
    "primary": "#9b59b6",
    "secondary": "#34495e",
    "success": "#27ae60",
    "warning": "#f39c12",
    "error": "#e74c3c",
    "user_msg_bg": "#2c3e50",
    "user_msg_text": "#3498db",
    "bot_msg_bg": "#2c3e50",
    "bot_msg_text": "#9b59b6",
    "border": "#34495e",
    "sidebar_bg": "#2c3e50",
    "sidebar_text": "#ffffff"
}

# Apply global CSS
st.markdown(f"""
<style>
    .stApp {{
        background-color: {colors['bg']} !important;
    }}
    * {{
        color: {colors['text']} !important;
    }}
    .stButton>button {{
        color: white !important;
    }}
    .user-message {{
        background-color: {colors['user_msg_bg']} !important;
        color: {colors['user_msg_text']} !important;
        padding: 12px;
        border-radius: 10px;
        margin: 8px 0;
        border-left: 4px solid {colors['primary']} !important;
    }}
    .bot-message {{
        background-color: {colors['bot_msg_bg']} !important;
        color: {colors['bot_msg_text']} !important;
        padding: 12px;
        border-radius: 10px;
        margin: 8px 0;
        border-left: 4px solid {colors['primary']} !important;
    }}
    .theme-indicator {{
        background-color: {colors['secondary']} !important;
        color: {colors['text']} !important;
        padding: 5px 10px;
        border-radius: 15px;
        font-size: 12px;
        display: inline-block;
        margin: 5px;
        border: 1px solid {colors['border']} !important;
    }}
</style>
""", unsafe_allow_html=True)

# Sidebar content
with st.sidebar:
    st.header("⚙️ Settings")

    # Response mode
    st.subheader("Response Mode")
    mode_col1, mode_col2 = st.columns(2)
    with mode_col1:
        if st.button("📋 Concise", use_container_width=True, 
                    type="primary" if st.session_state.mode == "concise" else "secondary"):
            st.session_state.mode = "concise"
            st.rerun()
    with mode_col2:
        if st.button("📊 Detailed", use_container_width=True,
                    type="primary" if st.session_state.mode == "detailed" else "secondary"):
            st.session_state.mode = "detailed"
            st.rerun()
    
    # Current mode indicator
    mode_text = "📋 Concise" if st.session_state.mode == "concise" else "📊 Detailed"
    st.info(f"**Current Mode:** {mode_text}")
    
    # File upload
    st.subheader("📁 Upload Document")
    uploaded_file = st.file_uploader("Choose TXT file", type=["txt"], label_visibility="collapsed")
    
    if uploaded_file is not None:
        try:
            content = uploaded_file.read().decode("utf-8")
            documents = [line.strip() for line in content.split('\n') if line.strip()]
            
            if documents:
                st.session_state.rag = SimpleRAG(documents)
                st.success(f"✅ File loaded! ({len(documents)} lines)")
            else:
                st.warning("⚠️ File is empty")
                
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

    # Status information
    if st.session_state.rag:
        st.success("✅ Document ready for questions")
    else:
        st.warning("⏳ Waiting for document upload")

    # Debug info
    with st.expander("Debug Info"):
        st.write(f"Mode: {st.session_state.mode}")
        st.write(f"Messages: {len(st.session_state.messages)}")
        st.write(f"RAG loaded: {st.session_state.rag is not None}")

# Main content area
st.title("🤖 NeoStats AI Chatbot")
st.caption(f"Chat with your documents • Dark Theme • {mode_text}")

# Theme indicator
st.markdown(f"""
<div class="theme-indicator">
    Theme: Dark • Mode: {mode_text}
</div>
""", unsafe_allow_html=True)

# Chat container
chat_container = st.container()

with chat_container:
    if st.session_state.messages:
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.markdown(f"""
                <div class="user-message">
                    <strong>👤 You:</strong><br>
                    {message["content"]}
                </div>
                """, unsafe_allow_html=True)
            else:
                mode_icon = "📋" if message.get("mode") == "concise" else "📊"
                st.markdown(f"""
                <div class="bot-message">
                    <strong>🤖 Bot ({mode_icon}):</strong><br>
                    {message["content"]}
                </div>
                """, unsafe_allow_html=True)
    else:
        st.info("💡 Upload a document and start asking questions!")

# Chat input
user_input = st.chat_input(
    f"Type your question about the document... ({'Concise' if st.session_state.mode == 'concise' else 'Detailed'} mode)"
)

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    if st.session_state.rag:
        with st.spinner("🤔 Thinking..."):
            response = st.session_state.rag.generate_answer(user_input, st.session_state.mode)
            st.session_state.messages.append({
                "role": "assistant", 
                "content": response,
                "mode": st.session_state.mode
            })
    else:
        st.session_state.messages.append({
            "role": "assistant", 
            "content": "Please upload a TXT file first to ask questions about it.",
            "mode": st.session_state.mode
        })
    
    st.rerun()

# Clear chat
if st.button("🗑️ Clear Chat", use_container_width=True):
    st.session_state.messages = []
    st.rerun()

# Instructions
with st.expander("ℹ️ How to use"):
    st.markdown("""
    **Getting Started:**
    1. **Upload a TXT file** in the sidebar
    2. **Select response mode**: Concise or Detailed
    3. **Ask questions** about your document
    
    **Response Modes:**
    - 📋 **Concise**: Brief, direct answers
    - 📊 **Detailed**: Comprehensive explanations
    
    **Theme:** Always dark for optimal readability
    """)
