import streamlit as st
import pandas as pd
from datetime import datetime
from PIL import Image
import plotly.express as px
import main
import classification as cl
import matplotlib.pyplot as plt
import numpy as np
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

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #00a4eb; /* Blue background for the sidebar */
        color: white; /* White text color */
        font-size: 16px; /* Adjust sidebar text size */
        padding: 20px; /* Add some padding */
    }

    /* Adjust elements inside the sidebar */
    [data-testid="stSidebar"] .sidebar-content {
        overflow: auto; /* Allow scrolling if content overflows */
    }

    /* Reset sidebar search bar (if mistakenly activated) */
    input[type="search"] {
        appearance: none;
        -webkit-appearance: none;
        outline: none;
    }

    /* General app content styling */
    [data-testid="stAppViewContainer"] {
        background-color: #b3d9ff; /* Light blue background */
        padding: 10px;
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
        
    }


   /* Floating emojis container */
    .emoji-container {
    position: fixed;
    z-index: 0;
    pointer-events: none;
    width: 100vw; /* Full viewport width */
    height: 100vh; /* Full viewport height */
    overflow: hidden; /* Ensures anything outside is clipped */
    }
    .emoji {
        position: absolute;
        font-size: 0.8rem;
        opacity: 0.8;
    }

    /* Circular motion animations */
    @keyframes circle {
        0% { transform: rotate(0deg) translateX(50px) rotate(0deg); }
        25% { transform: rotate(90deg) translateX(50px) rotate(-90deg); }
        50% { transform: rotate(180deg) translateX(50px) rotate(-180deg); }
        75% { transform: rotate(270deg) translateX(50px) rotate(-270deg); }
        100% { transform: rotate(360deg) translateX(50px) rotate(-360deg); }
    }
    @keyframes circle-large {
        0% { transform: rotate(0deg) translateX(100px) rotate(0deg); }
        25% { transform: rotate(90deg) translateX(100px) rotate(-90deg); }
        50% { transform: rotate(180deg) translateX(100px) rotate(-180deg); }
        75% { transform: rotate(270deg) translateX(100px) rotate(-270deg); }
        100% { transform: rotate(360deg) translateX(100px) rotate(-360deg); }
    }

    /* Triangular motion animations */
    @keyframes triangle {
        0% { transform: translate(0px, 0px); }
        33% { transform: translate(80px, 0px); }
        66% { transform: translate(40px, -69.28px); }
        100% { transform: translate(0px, 0px); }
    }
    @keyframes triangle-large {
        0% { transform: translate(0px, 0px); }
        33% { transform: translate(120px, 0px); }
        66% { transform: translate(60px, -103.92px); }
        100% { transform: translate(0px, 0px); }
    }

    /* Square motion animations */
    @keyframes square {
        0% { transform: translate(0px, 0px); }
        25% { transform: translate(80px, 0px); }
        50% { transform: translate(80px, 80px); }
        75% { transform: translate(0px, 80px); }
        100% { transform: translate(0px, 0px); }
    }
    @keyframes square-large {
        0% { transform: translate(0px, 0px); }
        25% { transform: translate(120px, 0px); }
        50% { transform: translate(120px, 120px); }
        75% { transform: translate(0px, 120px); }
        100% { transform: translate(0px, 0px); }
    }

    /* Assign animations to emojis */
    .emoji:nth-child(1) { animation: circle 6s infinite linear; }
    .emoji:nth-child(2) { animation: circle-large 8s infinite linear; }
    .emoji:nth-child(3) { animation: triangle 7s infinite ease-in-out; }
    .emoji:nth-child(4) { animation: triangle-large 9s infinite ease-in-out; }
    .emoji:nth-child(5) { animation: square 6s infinite ease-in-out; }
    .emoji:nth-child(6) { animation: square-large 10s infinite ease-in-out; }
    .emoji:nth-child(7) { animation: circle 8s infinite linear; }
    .emoji:nth-child(8) { animation: triangle 10s infinite ease-in-out; }
    .emoji:nth-child(9) { animation: square-large 11s infinite ease-in-out; }
    .emoji:nth-child(10) { animation: circle-large 9s infinite linear; }
    .emoji:nth-child(11) { animation: square 7s infinite ease-in-out; }
    .emoji:nth-child(12) { animation: triangle-large 12s infinite ease-in-out; }
    .emoji:nth-child(13) { animation: circle 6s infinite linear; }
    .emoji:nth-child(14) { animation: triangle 9s infinite ease-in-out; }
    .emoji:nth-child(15) { animation: square-large 10s infinite ease-in-out; }
    .emoji:nth-child(16) { animation: circle-large 11s infinite linear; }
    .emoji:nth-child(17) { animation: square 8s infinite ease-in-out; }
    .emoji:nth-child(18) { animation: triangle-large 13s infinite ease-in-out; }
    </style>

    <div class="emoji-container">
        <div class="emoji" style="left: 30%; top: 70%;">🍎</div>
        <div class="emoji" style="left: 15%; top: 60%;">🍌</div>
        <div class="emoji" style="left: 10%; top: 65%;">🍇</div>
        <div class="emoji" style="left: 10%; top: 70%;">🍉</div>
        <div class="emoji" style="left: 30%; top: 60%;">🍒</div>
        <div class="emoji" style="left: 20%; top: 55%;">🍓</div>
        <div class="emoji" style="left: 35%; top: 70%;">🍑</div>
        <div class="emoji" style="left: 10%; top: 70%;">🍍</div>
        <div class="emoji" style="left: 10%; top: 70%;">🥝</div>
        <div class="emoji" style="left: 30%; top: 65%;">🥭</div>
        <div class="emoji" style="left: 30%; top: 65%;">🍏</div>
        <div class="emoji" style="left: 30%; top: 65%;">🍐</div>
        <div class="emoji" style="left: 10%; top: 80%;">🍋</div>
        <div class="emoji" style="left: 5%; top: 65%;">🍊</div>
        <div class="emoji" style="left: 20%; top: 65%;">🍋</div>
        <div class="emoji" style="left: 30%; top: 75%;">🥭</div>
        <div class="emoji" style="left: 5%; top: 75%;">🍏</div>
        <div class="emoji" style="left: 35%; top: 75%;">🍐</div>
    </div>
    """,
    unsafe_allow_html=True
)

#Title
st.markdown(
    """
    <style>
    .centered-title-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 10vh; /* Full screen height */
        width: 100%; /* Full screen width */
        position: relative;
    }

    .title-box {
        text-align: center;
        font-size: 1.5rem; /* Increased font size */
        font-weight: bold;
        color: #4CAF50;
        background: rgba(76, 175, 80, 0.1); /* Light green background */
        padding: 30px 50px; /* Padding for the rectangle */
        border-radius: 15px; /* Rounded corners */
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2); /* Subtle shadow */
    }
    </style>

    <div class="centered-title-container">
        <div class="title-box">
            Welcome to Fruity Food Tracker!
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Sidebar navigation
page = st.sidebar.selectbox("Navigate", ["Home", "Register Food", "Tracked Items"])

# Initialize session state for food data
if "food_data" not in st.session_state:
    st.session_state.food_data = pd.DataFrame(columns=["Timestamp", "Food Item", "Group"])

# Home Page
if page == "Home":
    st.markdown(
    """
    <style>
    .centered-message-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 35vh; /* Full screen height */
        width: 100%; /* Full screen width */
        position: relative;
    }

    .message-box {
        text-align: center;
        font-size: 1rem;
        font-weight: 400;
        line-height: 2;
        color: #097969;
        background: rgba(9, 121, 105, 0.1); /* Light green background */
        padding: 20px;
        border-radius: 15px; /* Rounded corners */
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2); /* Subtle shadow */
    }
    </style>

    <div class="centered-message-container">
        <div class="message-box">
            Welcome to the Food Tracker App!<br>
            This app allows you to:<br>
            Capture food images using your camera.<br>
            Register food items into groups (e.g., Proteins, Grains).<br>
            Track and visualize your registered food items.<br>
            Upload food images directly from your device.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Register Food Page
if page == "Register Food":
    st.header("Register Food Item")
    food_image = st.camera_input("Take a picture of the food item:")
    uploaded_image = st.file_uploader("Upload an image file", type=["jpg", "jpeg", "png"])

    if food_image or uploaded_image:
        image = Image.open(food_image or uploaded_image)
        st.image(image, caption="Uploaded Food Image")
        st.session_state["uploaded_image"] = image
        data = main.run_model(image)
         

    # Initialize session state for the to-do list
    if "todo_list" not in st.session_state:
        st.session_state.todo_list = []

    # Title
    st.title("To-Do List App")

    # Add a new task
    with st.form("Add Task"):
        new_task = st.text_input("Enter a task", placeholder="e.g., Buy groceries")
        submitted = st.form_submit_button("Add Task")
        if submitted:
            if new_task:
                st.session_state.todo_list.append(new_task)
                st.success(f"Task '{new_task}' added!")
            else:
                st.warning("Task cannot be empty.")

    # Display the current to-do list
    st.subheader("Your To-Do List")
    if st.session_state.todo_list:
        for index, task in enumerate(st.session_state.todo_list):
            # Display each task with a "Remove" button
            col1, col2 = st.columns([0.8, 0.2])
            with col1:
                st.write(f"{index + 1}. {task}")
            with col2:
                if st.button("Remove", key=f"remove-{index}"):
                    st.session_state.todo_list.pop(index)
                    st.experimental_rerun()  # Refresh the page to update the list
    else:
        st.info("Your to-do list is empty!")

    # Footer
    st.markdown("---")
    st.write("Simple to-do list app using Streamlit.")


    if st.button("Register Food"):
        try:   
            cal = cl.Calculations()
            cal.load_results('results.json')
            labels = 'Vegetable','Protein','Grain'
            sizes = cal.classify(data)

            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            st.pyplot(fig1)
            cal.save_results('results.json')
        except NameError:
            pass

    if st.button('Reset'):
        reset = cl.Calculations()
        reset.resetJson('results.json')

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