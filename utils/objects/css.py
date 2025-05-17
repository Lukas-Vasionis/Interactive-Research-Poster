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

# CSS styling options for elements within containers
stylable_container_css = [
    """
    {
        background-color: rgba(139, 0, 0, 0.8); /* Dark red with transparency */
        border: 2px solid #DAA520; /* Golden border */
        border-radius: 0.5rem;
        padding-left: 20px;
        padding-right: 20px;
        margin: 10px;
        color: white; /* Assuming white text for readability */
    }
    """,
    """
    h1, h2, h3, h4, h5, h6 {
        color: #DAA520; /* Golden color for headers */
    }
    """,
    """
    .stMarkdown {
        padding-left: 40px;
        padding-right: 40px;
        padding-bottom: 20px;
        padding-top: 1px;
    }
    """,
    """
    .stMultiSelect div[data-baseweb="select"] > div:first-child {
        background-color: rgba(139, 0, 0, 0.8); /* Dark red with transparency */
        color: white; /* Text color */
        border-color: #DAA520; /* Golden border */
        }
    div[class="stSlider"] {
        padding-left: 40px;
        padding-right: 40px;
        padding-bottom: 5px;
        padding-top: 1px;
        }
    """
]