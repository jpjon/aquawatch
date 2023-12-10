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

# LinkedIn profile URLs for each individual
linkedin_urls = [
    "https://www.linkedin.com/in/sallyfang",
    "https://www.linkedin.com/in/jonathanphan",
    "https://www.linkedin.com/in/lyndasolischavez",
    "https://www.linkedin.com/in/jasmineteo"
]

# URL of the LinkedIn logo image
linkedin_logo_url = "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" 

# Multi-line captions for each image
captions = [
    f"<div style='display: flex; align-items: center;'><a href='{linkedin_urls[0]}' target='_blank'><img src='{linkedin_logo_url}' style='width:20px; margin-right:10px'/></a><div><strong>Sally Fang</strong><br><span style='font-size: 13px;'>xinfang00@berkeley.edu</span></div></div>",
    f"<div style='display: flex; align-items: center;'><a href='{linkedin_urls[1]}' target='_blank'><img src='{linkedin_logo_url}' style='width:20px; margin-right:10px'/></a><div><strong>Jonathan Phan</strong><br><span style='font-size: 13px;'>jonathanphan@berkeley.edu</span></div></div>",
    f"<div style='display: flex; align-items: center;'><a href='{linkedin_urls[2]}' target='_blank'><img src='{linkedin_logo_url}' style='width:20px; margin-right:10px'/></a><div><strong>Lynda Solis Chavez</strong><br><span style='font-size: 13px;'>lsolischavez@berkeley.edu</span></div></div>",
    f"<div style='display: flex; align-items: center;'><a href='{linkedin_urls[3]}' target='_blank'><img src='{linkedin_logo_url}' style='width:20px; margin-right:10px'/></a><div><strong>Jasmine Teo</strong><br><span style='font-size: 13px;'>teoyinyin@berkeley.edu</span></div></div>"
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
