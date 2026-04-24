import streamlit as st
from data import *

def judul():
    st.title("📗 Dashboard COVID-19")
    st.write("Selamat datang di Dashboard interaktif")

st.sidebar.title("Navigasi")
menu = st.sidebar.radio("Pilih Halaman", ["Home", "Halaman Data"])

if menu == "Home":
    judul()

    year = slyr()

    df = load_data()
    df_filtered = fldt(df, year)

    klm(df_filtered)
    pct1(df_filtered)

elif menu == "Halaman Data":
    judul()

    year = slyr()

    df = load_data()
    df_filtered = fldt(df, year)

    show_data(df_filtered)