import pickle

import pandas as pd
# from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.stylable_container import stylable_container

import streamlit as st
from utils.objects import graphs as gu
from utils.objects import widgets
from utils.objects.css import stylable_container_css
from data import get_data

# Caching decorator for optimisation
def descriptions_container(text, key_id):
    css = stylable_container_css
    with stylable_container(
            key=f"container_with_border-{key_id}",
            css_styles=css,
    ):
        st.markdown(text)


def results_container(my_obj):
    """
    Function intakes my_obj which is dict "text_elements" in utils.objects.text
    Then takes subset of its key "results" which is also a dict with sub-sections of "Results" section
    Args:
        my_obj: utils.objects.text.text_elemtns

    Returns: execution of streamlit elements

    """
    css = stylable_container_css

    with stylable_container(
            key="container_with_border-2",
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
            ###########################
            # Bar plot: Soul energy output
            ###########################
            st.markdown(my_obj['results']['soul_energy_output'])
            # adding widget for selecting barmode
            bar_mode = widgets.radio_energy_barplot_mode()
            st.plotly_chart(gu.get_fig_barplot_e_sources(bar_mode),
                            use_container_width=True)

        with st.container():
            ###########################
            # Heatmap: population measurements of local creatures
            ###########################
            st.markdown(my_obj['results']['environmental_impact'])

            heatmap_data = get_data.get_data_heatmap_creature_counts(
                rows=30, cols=9, measurement_time=10, mode='read')

            measurement_day = widgets.slider_measurement_day(
                heatmap_data)

            st.plotly_chart(
                gu.get_fig_heatmap(heatmap_data[measurement_day - 1]),
                use_container_width=True)
