import streamlit as st


st.set_page_config(page_title='About', page_icon=':droplet:', layout='wide')

# Add a banner with an image to your Streamlit page
st.image("app/data/danger_banner.png", use_column_width=True, width=None)

col1, col2 = st.columns(2)

with col1:
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

with col2:
    # Data Source and Data Approach
    st.title('Data Source & Approach')

    source_text = 'The project draws from diverse datasets, including Harmful Algal Bloom Datasets, Clear Lake Cyanotoxin Issues, Harmful Cyanobacterial Bloom Advisories in Wyoming Waters, and Algal Bloom Sampling Status in Florida Water. Leveraging these datasets, AquaWatch utilizes a two-stepped multi-binary ResNet model for image classification. The model is trained to initially classify algae as non-advisory or advisory and subsequently categorize advisory algae into caution or danger. The approach involves extensive exploratory data analysis (EDA), feature engineering, and the exploration of various model architectures. Feature engineering involves preprocessing and augmenting images, including resizing, pixel normalization, rotation, shifting, flipping, and adjustments to brightness and contrast.'

    # Display the mission text using st.markdown
    st.markdown(source_text)
    
    st.subheader('Data Source Links')
    # Dataset links:
    cayuga_url = "http://www.communityscience.org/monitoring-partnerships/harmful-algal-bloom-monitoring/harmful-algal-bloom-datasets/"
    cayuga_text = "Cayuga Lake"
    Clear_url = "https://www.facebook.com/ClearLakeWaterQuality/photos"
    Clear_text = "Clear Lake"
    Wyoming_url = "https://wdeq.maps.arcgis.com/apps/Shortlist/index.html?appid=342d22d86d0048819b8dfa61dd3ff061"
    Wyoming_text = "Wyoming Waters"
    Florida_url = "https://floridadep.gov/AlgalBloom"
    Florida_text = "Florida Waters"
    st.markdown(f"[{cayuga_text}]({cayuga_url})")
    st.markdown(f"[{Clear_text}]({Clear_url})")
    st.markdown(f"[{Wyoming_text}]({Wyoming_url})")
    st.markdown(f"[{Florida_text}]({Florida_url})")
