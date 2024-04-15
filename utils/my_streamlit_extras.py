import pickle

import pandas as pd
from streamlit_extras.stylable_container import stylable_container
import streamlit as st
import utils.objects.graphs as gu
from utils.objects import widgets
from data import get_data

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


@st.cache_data
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
            ###########################
            #temperature_variability_1
            ###########################
            st.markdown(my_obj['results']['temperature_variability_1'])

            st.plotly_chart(gu.fig_box_temp_circles(), use_container_width=True)

            ###########################
            # temperature_variability_2
            ###########################
            st.markdown(my_obj['results']['temperature_variability_2'])
            selection_circles = widgets.multiselect_circles()
            st.plotly_chart(gu.get_fig_spectral_analysis(selection_circles), use_container_width=True)

        with st.container():
            st.markdown(my_obj['results']['soul_energy_output'])

            bar_mode = widgets.radio_energy_barplot_mode()
            st.plotly_chart(gu.get_fig_barplot_e_sources(bar_mode),
                            use_container_width=True)

        with st.container():
            st.markdown(my_obj['results']['environmental_impact'])

            heatmap_data = get_data.get_data_heatmap_creature_counts(
                rows=30, cols=9, measurement_time=10, mode='read')

            measurement_day = widgets.slider_measurement_day(
                heatmap_data)

            st.plotly_chart(
                gu.get_fig_heatmap(heatmap_data[measurement_day - 1]),
                use_container_width=True)
