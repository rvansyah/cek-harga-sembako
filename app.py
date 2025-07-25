import streamlit as st
import pandas as pd
import os

@st.cache_data
def load_data():
    path = "data/data_harga_sembako.csv"
    if not os.path.exists(path):
        st.error(f"File {path} tidak ditemukan!")
        st.stop()
    return pd.read_csv(path)

df = load_data()

st.title("Cek Harga Sembako Terkini")
st.markdown(
    """
    Aplikasi ini membantu Anda memantau harga sembako (sembilan bahan pokok) di berbagai kota di Indonesia.
    Data diupdate secara berkala.
    """
)

# Pilih kota
kota = st.selectbox("Pilih Kota", sorted(df["Kota"].unique()))

# Filter data berdasarkan kota
df_kota = df[df["Kota"] == kota]

# Tampilkan data harga per tanggal terbaru
tanggal_terbaru = df_kota["Tanggal"].max()
df_terbaru = df_kota[df_kota["Tanggal"] == tanggal_terbaru]

st.subheader(f"Harga Sembako di {kota} per {tanggal_terbaru}")
st.dataframe(
    df_terbaru[["Komoditas", "Harga (Rp/Kg/Liter)"]].reset_index(drop=True),
    use_container_width=True
)

# Grafik tren harga per komoditas
komoditas = st.selectbox("Lihat Tren Harga Komoditas", sorted(df["Komoditas"].unique()))
df_komoditas = df_kota[df_kota["Komoditas"] == komoditas].sort_values("Tanggal")

st.line_chart(
    df_komoditas.set_index("Tanggal")["Harga (Rp/Kg/Liter)"],
    use_container_width=True
)

st.caption("Sumber data: Data internal (dummy). Anda dapat mengintegrasikan API harga pangan nasional untuk data real-time.")
