import streamlit as st
from predict import read_image, predict_1, preprocess, predict_2

st.set_page_config(page_title='Submit Image', page_icon=':droplet:', layout='wide')

st.title("Algae Bloom Toxicity Detection")

st.text("Upload an image to detect the toxicity level of algae.")

uploaded_file = st.file_uploader("Please upload your image here")

st.text("Please ensure that you upload an image capturing only the water body.")
st.text("Avoiding reflections on the water will lead to better identification of algae toxicity levels.")

if uploaded_file is not None:
    # Show the uploaded image
    with st.spinner('Wait for it...'):
        
        img = read_image(uploaded_file)
        
        st.image(img, caption='Uploaded Image.', width=1000)
        
        preprocessed_img  = preprocess(img)
        
        prediction = predict_1(preprocessed_img)
        
        st.success('Done!')
        
        if prediction[0] == "some algae":
            st.text("Further processing the image...")
            # Run second model here
            prediction2 = predict_2(preprocessed_img)
            
            if prediction2[0] == "Dangerous":
                predication_val = round((prediction[1][0] * prediction2[1][0])  * 100, 2)
            
                st.header("Results:")
                st.subheader("Dangerous: Total Microcystin: >20 &micro;g/L")
                st.markdown(f"Assuming this is a well-captured algae image with no reflection, our model classified the algae as <span style='font-size: 20px;'><b>Dangerous</b></span> with a probability of <span style='font-size: 20px;'><b>{predication_val}%</b></span>", unsafe_allow_html=True)
                st.subheader("What does this mean?")
                st.markdown("<span style='font-size: 20px;'><b>Dangerous</b></span> means that harmful algae is present at extreme conditions, at this time. For your safety, avoid all contact with the water. Do not let your pets come near and drink the water or eat the algae. This area should be closed off to public access.", unsafe_allow_html=True)
            else:
                predication_val = round((prediction[1][0] * prediction2[1][0])  * 100, 2)
                st.header("Results:")
                st.subheader("Caution: Total Microcystin: 0.80 &micro;g/L to 20 &micro;g/L")
                st.markdown(f"Assuming this is a well-captured algae image with no reflection, our model classified the algae as <span style='font-size: 20px;'><b>Caution</b></span> with a probability of <span style='font-size: 20px;'><b>{predication_val}%</b></span>", unsafe_allow_html=True)
                st.subheader("What does this mean?")
                st.markdown("<span style='font-size: 20px;'><b>Caution</b></span> means that harmful algae is expected or present, at this time. For your safety, avoid all contact with the water. Do not let pets come near and drink the water or eat the algae. If fishing, thoroughly clean the fish.", unsafe_allow_html=True)
        # No advisory
        else:
            predication_val = round(prediction[1][0] * 100, 2)
            st.header("Results:")
            st.subheader("No Advisory: Total Microcystin: <0.8 &micro;g/L")
            st.markdown(f"Assuming this is a well-captured algae image with no reflection, our model classified the algae as <span style='font-size: 20px;'><b>No Advisory</b></span> with a probability of <span style='font-size: 20px;'><b>{predication_val}%</b></span>", unsafe_allow_html=True)
            st.subheader("What does this mean?")
            st.markdown("<span style='font-size: 20px;'><b>No Advisory</b></span> means that harmful algae is not present in the water, at this time. No specific precautions or restrictions are advised at this level. It is important to note that these conditions may change with time.", unsafe_allow_html=True)