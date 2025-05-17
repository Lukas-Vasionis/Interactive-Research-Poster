import pickle
from pprint import pprint

import streamlit as st
from utils.objects.text import text_elements
import utils.objects.graphs as gu
import utils.transformations as ut
import utils.my_streamlit_extras as ste
import utils.objects.css as custom_css

# Setting poster display size
st.set_page_config(layout="wide")
# Setting background image
ut.set_png_as_page_bg('img/background_cropped.svg')


# Poster sections are put into 2 columns (columns are not visible in mobile version)
col1, col2 = st.columns(2)
with col1:
    # """
    # Each section is put into containers of two types results_container(), descriptions_container().
    # Both of them are derived from stylable_container of streamlit_extras.stylable_container module. This stylable
    # container is composed of text elements and graph objects. these types of containers are defined as functions
    # in utils.my_streamlit_extras()
    # """

    ste.descriptions_container(text_elements['abstract'],key_id='abstract')
    ste.descriptions_container(text_elements['indroduction'],key_id='indroduction')
    ste.results_container(text_elements)

with col2:
    ste.descriptions_container(text_elements['materials_methods'],key_id='materials_methods')
    ste.descriptions_container(text_elements['conclusion'],key_id='conclusion')
    ste.descriptions_container(text_elements['discussion'],key_id='discussion')
    ste.descriptions_container(text_elements['acknowledgements'],key_id='acknowledgements')
    ste.descriptions_container(text_elements['message'],key_id='message')


