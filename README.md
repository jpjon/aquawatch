# AquaWatch:Detecting Toxicity Levels of Algae Bloom

## Overview

AquaWatch is an image classification project that aims to identify harmful algae and predict toxicity levels in water bodies. Our approach involves the development of an advanced image classification model trained on a diverse dataset, encompassing various algae species and environmental conditions. This ensures robust performance across different scenarios.

## Datasets

We utilized the following datasets:

1. **Harmful Algal Bloom Datasets**
2. **Clear Lake Cyanotoxin Issues**
3. **Harmful Cyanobacterial Bloom (HCB) Advisories in Wyoming Waters**
4. **Algal Bloom Sampling Status in Florida Water**

## Project Structure

- **app:** Contains relevant files for our app deployment through Streamlit.
- **attempts:** Contains two previous attempts to build mask CNNs for algae detection.
- **EDA:** Exploratory Data Analysis showcasing the distribution of our dataset.
- **extract:** APIs demonstrating how we extracted images from different sources.
- **final_model:** Contains the final model used for this project, which is a 2-steped multi-binary ResNet model. The first model classifies whether the algae is non-advisory or advisory, and the second step further classifies it into either caution or danger. This section also includes our feature engineering steps, such as preprocessing and augmenting the images.
- **HOG + LBP:** Contains our exploration of the HOG + LBP feature for our dataset, along with t-SNE plots.
- **preliminary_models:** Baseline models initially explored for the project.

## Model Architecture and Feature Engineering

Our final model utilizes a 2-steped multi-binary ResNet architecture. In the first step, the model classifies algae as non-advisory or advisory. In the second step, it further classifies advisory algae into either caution or danger. Feature engineering steps involve preprocessing and augmenting images, including resizing to 224 by 224 pixels, pixel normalization, rotation, shifting, flipping, and adjusting brightness and contrast.

## Getting Started

To run the Streamlit app locally, navigate to the `app` directory and use the following command:

```bash
streamlit run app.py

