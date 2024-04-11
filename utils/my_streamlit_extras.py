from streamlit_extras.stylable_container import stylable_container
import streamlit as st

def extra_container(text):
    css = [
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
        """]
    with stylable_container(
        key="container_with_border",
        css_styles=css,
    ):
        st.markdown(text)


def results_container(my_obj):
    css = [
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
        """]
    with stylable_container(
            key="container_with_border",
            css_styles=css):
        st.markdown(my_obj['results']['title'])

        with st.container():
            c1, c2 = st.columns(2)
            c1.markdown(my_obj['results']['temperature_variability'])
            # c2.plotly_chart()

        with st.container():
            c1, c2 = st.columns(2)
            c1.markdown(my_obj['results']['wind_patterns'])
            # c2.plotly_chart()

        with st.container():
            c1, c2 = st.columns(2)
            c1.markdown(my_obj['results']['soul_energy_output'])
            # c2.plotly_chart()

        with st.container():
            c1, c2 = st.columns(2)
            c1.markdown(my_obj['results']['environmental_impact'])
            # c2.plotly_chart()