import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
import pandas as pd
from streamlit.components.v1 import html

# Page 1: Main Page
def about_page():
    st.title("Welcome to Aquawatch 💧")
    st.subheader("The Algae Bloom Toxicity Detection App")
    st.text("This web app detects the toxicity level of algae in water based on images.")
    st.text("Please see below for examples of the 3 tiers of toxins.")


    # Display images of the 3 tiers
    col1, col2, col3 = st.columns(3)
    col1.image("data/no_advisory.jpg", caption='No Advisory', use_column_width=True)
    col2.image("data/warning.jpg", caption='Caution', use_column_width=True)
    col3.image("data/danger.jpg", caption='Danger', use_column_width=True)

    st.text("We classified the tiers based on the following categorization:")

    data = {
        "Category": ["No advisory", "Caution", "Danger"],
        "Description": [
            "Total Microcystins: <0.8μg/L",
            "Total Microcystins: 0.8μg/L to <20μg/L",
            "Total Microcystins: ≥20μg/L"
        ]
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Create a table
    st.table(df)

# Page 2: Mission and Impact
def mission_page():

    # Add a banner with an image to your Streamlit page
    st.image("data/danger_banner.png", use_column_width=True, width=None)

    # Problem and Motivation
    st.title("Problem and Motivation")

    problem_text = 'The AquaWatch project addresses the critical issue of identifying harmful algae and predicting toxicity levels in water bodies. Harmful algal blooms pose significant threats to aquatic ecosystems and public health. Motivated by the need for an effective solution, AquaWatch employs advanced image classification techniques to discern various algae species and assess potential environmental risks. The project aims to contribute to water quality monitoring and enhance early warning systems.'

    # Display the problem text using st.markdown
    st.markdown(problem_text)   
    
    # Displaying Mission
    st.title("Our Mission")
    
    mission_text = 'Our aim is to develop an image classification model designed to detect harmful algae in water bodies. By creating this model, we are dedicated to reducing the impact of harmful algae exposure, which can result in irritations and health issues. Our goal is to safeguard habitats, preserve water quality, and enhance the overall safety of recreational activities.'

    # Display the mission text using st.markdown
    st.markdown(mission_text)

    # Data Source and Data Approach
    st.title('Data Source & Approach')

    source_text = 'The project draws from diverse datasets, including Harmful Algal Bloom Datasets, Clear Lake Cyanotoxin Issues, Harmful Cyanobacterial Bloom Advisories in Wyoming Waters, and Algal Bloom Sampling Status in Florida Water. Leveraging these datasets, AquaWatch utilizes a two-stepped multi-binary ResNet model for image classification. The model is trained to initially classify algae as non-advisory or advisory and subsequently categorize advisory algae into caution or danger. The approach involves extensive exploratory data analysis (EDA), feature engineering, and the exploration of various model architectures. Feature engineering involves preprocessing and augmenting images, including resizing, pixel normalization, rotation, shifting, flipping, and adjustments to brightness and contrast.'

    # Display the mission text using st.markdown
    st.markdown(source_text)
    

# Page 3: Detection Page
def submit_image():
    st.title("Algae Bloom Toxicity Detection")
    st.text("Upload an image to detect the toxicity level of algae.")

    uploaded_file = st.file_uploader("Please upload your image here")
    st.text("Please ensure that you upload an image capturing only the water body.")
    st.text("Avoiding reflections on the water will lead to better identification of algae toxicity levels.")

    if uploaded_file is not None:
        # Show the uploaded image
        img = Image.open(uploaded_file)
        st.image(img, caption='Uploaded Image.', use_column_width=True)

# Page 4: Team Page
def team_page():
    st.title("Meet the Team!")
    
    # Add text content using st.markdown
    st.markdown(
        """
        <div style="padding: 10px; background-color: #6C9556; color: white; text-align: center; font-size: 20px;">
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Image paths
    image_paths = ["team/sally.png", "team/jonathan.png", "team/lynda.png", "team/jasmine.png"]
    
    # Multi-line captions for each image
    captions = [
        "<strong>Sally Fang</strong><br><span style='font-size: 13px;'>xinfang00@berkeley.edu</span>",
        "<strong>Jonathan Phan</strong><br><span style='font-size: 13px;'>jonathanphan@berkeley.edu</span>",
        "<strong>Lynda Solis Chavez</strong><br><span style='font-size: 13px;'>lsolischavez@berkeley.edu</span>",
        "<strong>Jasmine Teo</strong><br><span style='font-size: 13px;'>teoyinyin@berkeley.edu</span>"
    ]
    
    # Set the font size for the captions using HTML
    font_size = "20px"  # Adjust the size as needed
    
    # Create columns for each image and caption
    col1, col2, col3, col4 = st.columns(4)
    
    # Display images and captions in columns
    for i in range(4):
        with col1 if i == 0 else col2 if i == 1 else col3 if i == 2 else col4:
            st.image(image_paths[i], use_column_width=True)
            st.markdown(f"<p style='font-size:{font_size}; text-align: center;'>{captions[i]}</p>", unsafe_allow_html=True)


# Sidebar with links to switch between pages
selected_page = st.sidebar.radio("Select Page", ["Home", "About", "Submit Image", "Contact Us"])

# Display the selected page
if selected_page == "Home":
    about_page()
elif selected_page == "About":
    mission_page()    
elif selected_page == "Submit Image":
    submit_image()
elif selected_page == "Contact Us":
    team_page()