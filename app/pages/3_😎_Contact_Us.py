import streamlit as st 

st.set_page_config(page_title='Contact', page_icon=':droplet:', layout='wide')

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
image_paths = ["app/team/sally.png", "app/team/jonathan.png", "app/team/lynda.png", "app/team/jasmine.png"]

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
