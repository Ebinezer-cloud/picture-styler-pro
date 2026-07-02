import streamlit as st

import config

from utils.image_loader import load_image
from utils.image_converter import cv_to_pil
from utils.download import image_to_bytes

from styles import (
    pencil,
    cartoon,
    oil,
    bw,
    watercolor,
    hdr,
    sepia
)

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title=config.APP_NAME,
    page_icon=config.APP_ICON,
    layout=config.LAYOUT
)

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

st.sidebar.title("🎨 Image Stylizer Pro")

effect = st.sidebar.selectbox(
    "Choose Effect",
    config.EFFECTS
)

st.sidebar.markdown("---")
st.sidebar.write("Upload an image and choose an artistic effect.")

# ---------------------------------------------------
# Main Page
# ---------------------------------------------------

st.title("🎨 Image Stylizer Pro")
st.write("Transform your photos into beautiful artistic images.")

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=config.SUPPORTED_FORMATS
)

# ---------------------------------------------------
# Image Processing
# ---------------------------------------------------

if uploaded_file is not None:

    pil_image, cv_image = load_image(uploaded_file)

    if effect == "Original":
        processed = cv_image

    elif effect == "Pencil Sketch":
        processed = pencil.apply(cv_image)

    elif effect == "Cartoon":
        processed = cartoon.apply(cv_image)

    elif effect == "Oil Painting":
        processed = oil.apply(cv_image)

    elif effect == "Black & White":
        processed = bw.apply(cv_image)

    elif effect == "Watercolor":
        processed = watercolor.apply(cv_image)

    elif effect == "HDR":
        processed = hdr.apply(cv_image)

    elif effect == "Sepia":
        processed = sepia.apply(cv_image)

    else:
        processed = cv_image

    processed_pil = cv_to_pil(processed)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(
            pil_image,
            use_container_width=True
        )

    with col2:
        st.subheader(effect)
        st.image(
            processed_pil,
            use_container_width=True
        )

    st.download_button(
        label="📥 Download Image",
        data=image_to_bytes(processed_pil),
        file_name="stylized_image.png",
        mime="image/png"
    )