import streamlit as st
from utils.objects.text import text_elements
import utils.objects.graphs as gu
import utils.transformations as ut
import utils.my_streamlit_extras as ste

st.set_page_config(layout="wide")
ut.set_png_as_page_bg('img/background_cropped.svg')

ste.extra_container(text_elements['abstract'])
gu.fig_sp_line()
col1, col2 = st.columns(2)
with col1:
    ste.extra_container(text_elements['indroduction'])
    ste.extra_container(text_elements['materials_methods'])
    ste.extra_container(text_elements['discussion'])
    ste.extra_container(text_elements['conclusion'])
    ste.extra_container(text_elements['acknowledgements'])
with col2:
    ste.extra_container(text_elements['results'])
    # Mock Data for Temperature Variability


