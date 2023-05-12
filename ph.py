import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="pH Meter App")

st.title("pH Meter App")

st.sidebar.header("Masukkan Parameter")

pH_value = st.sidebar.slider("Pilih Nilai pH:", 0.0, 14.0, 7.0, 0.1)

st.write("Nilai pH yang dipilih:", pH_value)

if pH_value < 7.0:
    st.write("Senyawa ini Asam.")
elif pH_value > 7.0:
    st.write("Senyawa ini Basa.")
else:
    st.write("Senyawa ini Netral.")



