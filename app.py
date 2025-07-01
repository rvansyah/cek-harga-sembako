import streamlit as st
import pandas as pd
import os

@st.cache_data
def load_data():
    if not os.path.exists("data/harga_sembako.csv"):
        return None
    return pd.read_csv("data/harga_sembako.csv")

df = load_data()

st.title("Cek Harga Sembako Terkini")

if df is None:
    st.error("Data harga sembako belum tersedia. Silakan upload file data/harga_sembako.csv terlebih dahulu.")
    st.stop()
# ...lanjutkan kode seperti sebelumnya...
