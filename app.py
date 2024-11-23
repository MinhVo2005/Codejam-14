import streamlit as st
import pandas as pd
from datetime import datetime
from PIL import Image
import plotly.express as px
#Size ajustor

st.markdown(
    """
    <style>
    /* Base font size for the entire app */
    html, body, [class*="stMarkdown"], [class*="stTitle"], [class*="stHeader"], [class*="stText"] {
        font-size: 18px; /* Adjust this value to globally increase text size */
    }
    
    /* Increase size of headings */
    h1 {
        font-size: 2.5rem !important;
    }
    h2 {
        font-size: 2rem !important;
    }
    h3 {
        font-size: 1.75rem !important;
    }

    /* Sidebar text size */
    .sidebar .sidebar-content, .css-1d391kg { 
        font-size: 18px !important;
    }

    /* Button text size */
    .stButton button {
        font-size: 18px !important; /* Ensure buttons have larger text */
    }

    /* Increase font size in dataframes or tables */
    .stDataFrame, .stTable {
        font-size: 16px !important; /* Adjust for table content */
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Consolidated CSS
st.markdown(
    """
    <style>
    /* Main container and background */
    [data-testid="stAppViewContainer"] {
        min-height: 100vh;
        background-color: #b3d9ff;
        background-size: cover;
        background-attachment: fixed;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #00a4eb;
        color: white;
        font-size: 16px;
        max-height: 100vh;
        overflow-y: auto;
    }

    /* Main content styling */
    [data-testid="stAppViewContainer"] .main {
        background: rgba(255, 255, 255, 0.85);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
    }

    /* Fonts and text styles */
    @import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@300;400;700&display=swap');
    html, body, [data-testid="stAppViewContainer"] * {
        font-family: 'Comic Neue';
        font-size: 100% !important;
    }

    /* Title styling */
    h1 {
        font-size: 800px !important;
        text-align: center;
        background: black;
        -webkit-background-clip: text;
        color: transparent;
    }

    /* Floating emojis */
    .emoji-container {
        position: fixed;
        z-index: 0;
        pointer-events: none;
        width: 100%;
        height: 100%;
        overflow: hidden;
    }
    .emoji {
        position: absolute;
        font-size: 24px;
        animation: float 10s infinite ease-in-out;
    }
    @keyframes float {
        0% { transform: translate(0, 0); opacity: 0.5; }
        25% { transform: translate(-30px, 20px); opacity: 1; }
        50% { transform: translate(30px, -20px); opacity: 0.8; }
        75% { transform: translate(-20px, -30px); opacity: 1; }
        100% { transform: translate(0, 0); opacity: 0.5; }
    }
    </style>
    <div class="emoji-container">
        <div class="emoji" style="left: 5%; top: 10%;">🍎</div>
        <div class="emoji" style="left: 20%; top: 20%;">🍌</div>
        <div class="emoji" style="left: 35%; top: 30%;">🍇</div>
        <div class="emoji" style="left: 50%; top: 40%;">🍉</div>
        <div class="emoji" style="left: 65%; top: 50%;">🍒</div>
        <div class="emoji" style="left: 30%; top: 10%;">🍓</div>
        <div class="emoji" style="left: 15%; top: 70%;">🍑</div>
        <div class="emoji" style="left: 30%; top: 80%;">🍍</div>
        <div class="emoji" style="left: 10%; top: 10%;">🥝</div>
        <div class="emoji" style="left: 30%; top: 10%;">🥑</div>
        <div class="emoji" style="left: 5%; top: 10%;">🍎</div>
        <div class="emoji" style="left: 20%; top: 20%;">🍌</div>
        <div class="emoji" style="left: 35%; top: 30%;">🍇</div>
        <div class="emoji" style="left: 50%; top: 40%;">🍉</div>
        <div class="emoji" style="left: 65%; top: 50%;">🍒</div>
        <div class="emoji" style="left: 30%; top: 10%;">🍓</div>
        <div class="emoji" style="left: 15%; top: 70%;">🍑</div>
        <div class="emoji" style="left: 30%; top: 80%;">🍍</div>
        <div class="emoji" style="left: 10%; top: 10%;">🥝</div>
        <div class="emoji" style="left: 50%; top: 20%;">🥑</div>
        <div class="emoji" style="left: 70%; top: 30%;">🍏</div>
        <div class="emoji" style="left: 80%; top: 40%;">🍐</div>
        <div class="emoji" style="left: 40%; top: 60%;">🍋</div>
        <div class="emoji" style="left: 10%; top: 90%;">🍊</div>
        <div class="emoji" style="left: 25%; top: 15%;">🍍</div>
        <div class="emoji" style="left: 75%; top: 20%;">🥭</div>
        <div class="emoji" style="left: 5%; top: 10%;">🍎</div>
        <div class="emoji" style="left: 20%; top: 20%;">🍌</div>
        <div class="emoji" style="left: 35%; top: 30%;">🍇</div>
        <div class="emoji" style="left: 5%; top: 40%;">🍉</div>
        <div class="emoji" style="left: 6.5%; top: 50%;">🍒</div>
        <div class="emoji" style="left: 30%; top: 10%;">🍓</div>
        <div class="emoji" style="left: 1.5%; top: 70%;">🍑</div>
        <div class="emoji" style="left: 20%; top: 80%;">🍍</div>
        <div class="emoji" style="left: 1%; top: 10%;">🥝</div>
        <div class="emoji" style="left: 5%; top: 20%;">🥑</div>
        <div class="emoji" style="left: 70%; top: 30%;">🍏</div>
        <div class="emoji" style="left: 8%; top: 40%;">🍐</div>
        <div class="emoji" style="left: 33%; top: 60%;">🍋</div>
        <div class="emoji" style="left: 10%; top: 90%;">🍊</div>
        <div class="emoji" style="left: 35%; top: 15%;">🍍</div>
        <div class="emoji" style="left: 72%; top: 20%;">🥭</div>
    </div>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("<h1>Welcome to Fruity Food Tracker!</h1>",
             unsafe_allow_html=True)

# Sidebar navigation
page = st.sidebar.selectbox("Navigate", ["Home", "Register Food", "Tracked Items"])

# Initialize session state for food data
if "food_data" not in st.session_state:
    st.session_state.food_data = pd.DataFrame(columns=["Timestamp", "Food Item", "Group"])

# Home Page
if page == "Home":
    st.write("""
    Welcome to the Food Tracker App! This app allows you to:
    - Capture food images using your camera.
    - Register food items into groups (e.g., Proteins, Grains).
    - Track and visualize your registered food items.
    - Upload food images directly from your device.
    """)

# Register Food Page
elif page == "Register Food":
    st.header("Register Food Item")
    food_image = st.camera_input("Take a picture of the food item:")
    uploaded_image = st.file_uploader("Upload an image file", type=["jpg", "jpeg", "png"])

    if food_image or uploaded_image:
        image = Image.open(food_image or uploaded_image)
        st.image(image, caption="Uploaded Food Image")
        st.session_state["uploaded_image"] = image


        

    food_name = st.text_input("Food Name", placeholder="Enter the name of the food item")
    food_group = st.selectbox("Select Alimentary Group", ["Proteins", "Grains", "Dairy", "Fruits & Veggies"])

    if st.button("Register Food"):
        if food_name and food_group:
            st.session_state.food_data = pd.concat(
                [st.session_state.food_data, pd.DataFrame({
                    "Timestamp": [datetime.now()],
                    "Food Item": [food_name],
                    "Group": [food_group]
                })], ignore_index=True)
            st.success(f"Registered {food_name} under {food_group} group!")
        else:
            st.error("Please provide both the food name and group.")

# Tracked Items Page
elif page == "Tracked Items":
    st.header("Tracked Food Items")
    if not st.session_state.food_data.empty:
        st.dataframe(st.session_state.food_data)
        st.download_button(
            "Download Food Data",
            data=st.session_state.food_data.to_csv(index=False),
            file_name="food_data.csv",
            mime="text/csv",
        )
        group_counts = st.session_state.food_data["Group"].value_counts().reset_index()
        fig = px.pie(
            group_counts.rename(columns={"index": "Group", "Group": "Count"}),
            names="Group",
            values="Count",
            title="Distribution of Alimentary Groups",
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No food items registered yet.")
