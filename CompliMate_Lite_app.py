import streamlit as st
from PIL import Image
import base64
from CompliMate_Lite import CompliMateLite  # import backend

# --- CONFIGURATION ---
BOT_NAME = "CompliMate Lite"
BOT_LOGO = "bot_logo.png"  # Path to your bot logo
BACKGROUND_IMAGE = "background.png"  # Path to your background image
OVERLAY_IMAGE = "overlay.png"  # Path to your overlay image

# --- FUNCTIONS ---
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def set_background(image_file):
    encoded = get_base64(image_file)
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        font-family: 'Segoe UI', sans-serif;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def chat_bubble(message, sender="user"):
    if sender == "user":
        bubble = f"""
        <div style="text-align:right;">
            <div style="
                display:inline-block;
                background-color:#d1f7c4;
                padding:12px 18px;
                border-radius:20px;
                margin:5px;
                max-width:70%;
                box-shadow: 1px 1px 5px rgba(0,0,0,0.1);
                ">
                {message}
            </div>
        </div>
        """
    else:
        bubble = f"""
        <div style="text-align:left; display:flex; align-items:flex-start; margin:5px;">
            <img src="data:image/png;base64,{get_base64(BOT_LOGO)}" width="35" height="35" style="border-radius:50%; margin-right:10px; border:1px solid #ccc;">
            <div style="
                background-color:rgba(255,255,255,0.9);
                padding:12px 18px;
                border-radius:20px;
                max-width:70%;
                box-shadow: 1px 1px 5px rgba(0,0,0,0.1);
                ">
                <b style="color:#1a4d2e;">{BOT_NAME}:</b> {message}
            </div>
        </div>
        """
    st.markdown(bubble, unsafe_allow_html=True)

# --- PAGE CONFIG ---
st.set_page_config(page_title=BOT_NAME, layout="wide")
set_background(BACKGROUND_IMAGE)

# Initialize backend once
if "complimate_lite" not in st.session_state:
    st.session_state.complimate_lite = CompliMateLite()

# --- OVERLAY IMAGE ---
st.markdown(
    f"""
    <div style="position:fixed; top:65px; right:10px; z-index:1;">
        <img src="data:image/png;base64,{get_base64(OVERLAY_IMAGE)}" width="100">
    </div>
    """,
    unsafe_allow_html=True
)

# --- HEADER ---
st.markdown(
    f"""
    <div style="text-align:center; margin-top:20px;">
        <h1 style='
            color:white; 
            font-size:3rem; 
            font-weight:bold; 
            margin-bottom:0px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.4);
        '>
            {BOT_NAME}
        </h1>
        <p style='
            color:white; 
            font-size:1.2rem; 
            margin-top:5px; 
            text-align:left;
            display:inline-block;
        '>
            Your Compliance Companion
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# --- SIDEBAR ---
with st.sidebar:
    st.header("⚡Quick Start")
    topic = st.selectbox("Choose Role:", ["retail","non-retail"])
    st.markdown("---")
    st.info("Please select your role to tailor the compliance experience. This will help me provide more relevant information and guidance based on your specific needs.")

# --- CHAT INTERFACE ---
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "sender": "bot",
        "message": "Hello! 👋 I’m CompliMate Lite, your trusted compliance assistant.<br />"
                   "Enter keywords or phrases related to topics you want to explore. "
                   "I'll assist you in navigating the landscape effectively😊"
    }]

# Display chat bubbles
for msg in st.session_state.messages:
    chat_bubble(msg["message"], sender=msg["sender"])

# User input
query = st.text_input("Your query:", key="user_input")

if query:
    # Add user message
    st.session_state.messages.append({"sender": "user", "message": query})

    # Get backend answer
    bot_result = st.session_state.complimate_lite.query(query, user_role=topic)

    #Prepend custom intro message
    intro_msg="Here are the relevant sections based on your query:\n\n"
    bot_result=intro_msg + bot_result
    
    # Add bot message
    st.session_state.messages.append({"sender": "bot", "message": bot_result})

    # Clear input so it won't re-trigger
    del st.session_state["user_input"]

    st.rerun()
