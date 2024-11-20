import streamlit as st

def create_sidebar():
    st.sidebar.title("Settings")
    temperature = st.sidebar.slider("Select Temperature", 0.0, 1.0, 0.25, 0.05)
    return temperature
