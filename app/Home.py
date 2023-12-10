import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(page_title='AquaWatch Algae Detection Tool', page_icon=':droplet:', layout='wide')

st.title("Welcome to Aquawatch 💧")
st.subheader("The Algae Bloom Toxicity Detection App")
st.text("This web app detects the toxicity level of algae in water based on images.")
st.text("Please see below for examples of the 3 tiers of toxins.")

# Display images of the 3 tiers
col1, col2, col3 = st.columns(3)
col1.image("app/data/no_advisory.jpg", caption='No Advisory', use_column_width=True)
col2.image("app/data/warning.jpg", caption='Caution', use_column_width=True)
col3.image("app/data/danger.jpg", caption='Danger', use_column_width=True)

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