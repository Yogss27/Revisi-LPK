import streamlit as st
import pandas as pd
import numpy as np

import streamlit as st
import time

progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1, text=progress_text)




st.title(':blue[Penghitung kadar pH]:sunglasses:')

st.sidebar.header("Masukkan Parameter")

pH_value = st.sidebar.slider("Pilih nilai pH:", 0.0, 14.0, 7.0, 0.1)

st.write("Nilai pH yang dipilih:", pH_value)

if pH_value < 7.0:
    st.write("Senyawa ini asam.")
elif pH_value > 7.0:
    st.write("Senyawa ini basa.")
else:
    st.write("Senyawa ini netral.")

import streamlit as st

import time
import streamlit as st

with st.spinner('Tunggu bentar ya.....:kiss:'):
    time.sleep(4)
st.success('Hore selesai:satisfied:', icon="✅")

st.text('Selamat menggunakan aplikasi.')