import pandas as pd
from streamlit_extras.stylable_container import stylable_container
import streamlit as st
import utils.objects.graphs as gu

stylable_container_css = [
    """
    {
        background-color: rgba(139, 0, 0, 0.8); /* Dark red with transparency */
        border: 2px solid #DAA520; /* Golden border */
        border-radius: 0.5rem;
        padding-left: 20px;
        padding-right: 20px;
        margin: 20px;
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
    """
]


def extra_container(text):
    css = stylable_container_css
    with stylable_container(
            key="container_with_border",
            css_styles=css,
    ):
        st.markdown(text)


def results_container(my_obj):
    css = stylable_container_css

    with stylable_container(
            key="container_with_border",
            css_styles=css):
        st.markdown(my_obj['results']['title'])

        with st.container():
            st.markdown(my_obj['results']['temperature_variability'])


            circle_options=['1st', '2nd', '3rd', '4th', '5th','6th', '7th', '8th', '9th']
            all = st.checkbox("Select all circles", value=True)
            if all:
                selection_circles = st.multiselect("Filter: Circles of Hell:",
                                                         circle_options, circle_options)
            else:
                selection_circles = st.multiselect("Filter: Circles of Hell:",
                                                         circle_options)


            st.plotly_chart(gu.fig_box_temp_circles(selection_circles), use_container_width=True)
            st.plotly_chart(gu.get_fig_spectral_analysis(selection_circles), use_container_width=True)

        with st.container():
            st.markdown(my_obj['results']['soul_energy_output'])

        with st.container():
            st.markdown(my_obj['results']['environmental_impact'])
            st.plotly_chart(gu.get_fig_heatmap(), use_container_width=True)
