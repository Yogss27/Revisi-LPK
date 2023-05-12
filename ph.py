import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="pH Meter App")

st.title("pH Meter App")

st.sidebar.header("Input Parameters")

pH_value = st.sidebar.slider("Select pH value:", 0.0, 14.0, 7.0, 0.1)

st.write("pH value selected:", pH_value)

if pH_value < 7.0:
    st.write("The solution is acidic.")
elif pH_value > 7.0:
    st.write("The solution is basic.")
else:
    st.write("The solution is neutral.")



