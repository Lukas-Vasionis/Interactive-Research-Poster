import streamlit as st
def load_custom_css():
    # Define the custom CSS
    custom_css = """
    <style>
        /* Styling for multiselect widget */
        .stSelectbox .css-2b097c-container, .stMultiSelect .css-2b097c-container {
            background-color: rgba(139, 0, 0, 0.8); /* Dark red with transparency */
            color: white; /* Text color */
            border: 2px solid #DAA520; /* Golden border */
        }

        /* Color of the selected option in dropdown */
        .stSelectbox .css-1uccc91-singleValue, .stMultiSelect .css-1uccc91-singleValue {
            color: white; /* Text color */
        }

        /* Styling for checkboxes */
        .stCheckbox label[data-baseweb="checkbox"] {
            color: white; /* Text color */
        }

        .stCheckbox input:checked ~ div {
            background-color: #DAA520 !important; /* Golden background for checked */
            border-color: #DAA520; /* Golden border */
        }

        /* Hover effects for checkboxes */
        .stCheckbox input:hover ~ div {
            border-color: #DAA520; /* Golden border */
        }
    </style>
    """
    # Inject custom CSS with markdown
    st.markdown(custom_css, unsafe_allow_html=True)