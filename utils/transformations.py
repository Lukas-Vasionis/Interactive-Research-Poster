import streamlit as st
import base64


def set_png_as_page_bg(bin_file):
    """
    Sets background image for the app
    Args:
        bin_file: image in svg format

    Returns: add background image to the st app

    """
    def get_base64_of_bin_file():
        with open(bin_file, 'rb') as f:
            data = f.read()
            encoded_string = base64.b64encode(data).decode()
        return f"data:image/svg+xml;base64,{encoded_string}"

    bin_str = get_base64_of_bin_file()
    bg_image = f"""
    <style>
    .stApp {{
        background-image: url("{bin_str}");
        background-size: cover;
    }}
    </style>
    """
    st.markdown(bg_image, unsafe_allow_html=True)
    return
