import streamlit as st
from predict import read_image, predict_1, preprocess

st.set_page_config(page_title='Submit Image', page_icon=':droplet:', layout='wide')

st.title("Algae Bloom Toxicity Detection")
st.text("Upload an image to detect the toxicity level of algae.")

uploaded_file = st.file_uploader("Please upload your image here")
st.text("Please ensure that you upload an image capturing only the water body.")
st.text("Avoiding reflections on the water will lead to better identification of algae toxicity levels.")

if uploaded_file is not None:
    # Show the uploaded image
    img = read_image(uploaded_file)
    
    st.image(img, caption='Uploaded Image.', use_column_width=True)
    
    preprocessed_img  = preprocess(img)
    
    prediction = predict_1(preprocessed_img)
    
    st.text(f"This is {prediction}")