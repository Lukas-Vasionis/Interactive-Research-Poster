import streamlit as st

def multiselect_circles():
    circle_options = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th']
    all = st.checkbox("Select all circles", value=True)
    if all:
        selection_circles = st.multiselect("Filter: Circles of Hell:",
                                           circle_options, circle_options)
    else:
        selection_circles = st.multiselect("Filter: Circles of Hell:",
                                           circle_options)
    return selection_circles