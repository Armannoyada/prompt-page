import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import os

from image_processing import detect_disease ,preprocess_image 
import time
st.set_page_config(page_title="Multi-Plant Disease Detector", layout="wide")

# Custom CSS for the nav bar


hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
   
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

  
col1, col2, col3 = st.columns([4, 4, 1])

with col2:
    st.image("ai_logo-removebg-preview.png", width=100)
    

# Function to simulate word-by-word text generation
def generate_text_effect(text, delay=0.001):
    placeholder = st.empty()
    words = text.split()
    full_text = ""
    
    for word in words:
        full_text += word + " "
        placeholder.markdown(f"**{full_text.strip()}**")
        time.sleep(delay)  # Adjust the delay for typing speed

# Example function that generates the cure message with a typing effect
def show_cure_with_effect(cure):
    st.write("Recommended Cure:")
    generate_text_effect(cure, delay=0.2)


# List of plants
PLANTS = [
    "Apple",  "Corn",   
    "Potato", "Rice",  "Sugar_Cane",
     "Wheat"
]

def load_image(image_file):
    return Image.open(image_file)

def home_page():
    col1, col2, col3 = st.columns([2.7, 4, 1])

    with col2:
        st.header("Welcome to PlantDDA")
    st.write("Select a plant to detect diseases:")

    cols = st.columns(3)
    for idx, plant in enumerate(PLANTS):
        with cols[idx % 3]:
            st.image(f"{/plant.lower()}.jpg", width=300)
            if st.button(f"Detect {plant} Diseases"):
                st.session_state.page = "Plant Detection"
                st.session_state.selected_plant = plant
                st.rerun()

def plant_detection_page():
    if 'selected_plant' not in st.session_state:
        st.warning("Please select a plant from the home page.")
        if st.button("Go to Home"):
            st.session_state.page = "Home"
            st.rerun()
        return

    plant = st.session_state.selected_plant
    st.subheader(f"{plant} Disease Detection")

    image_file = st.file_uploader("Upload an image", type=['jpg', 'png', 'jpeg'])
    
    if image_file is not None:
        image = load_image(image_file)
        st.image(image, caption="Uploaded Image", width=500)
        
        if st.button("Detect Disease"):
            processed_image = preprocess_image(image)
            disease, confidence, cure = detect_disease(processed_image, plant)
            
            st.success(f"Detected Disease: {disease}")
            st.info(f"Confidence: {confidence:.2f}%")
            show_cure_with_effect(cure)
    if st.button("Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

def main():
    if 'page' not in st.session_state:
        st.session_state.page = "Home"

    if st.session_state.page == "Home":
        home_page()
    elif st.session_state.page == "Plant Detection":
        plant_detection_page()

if __name__ == "__main__":
    main()
