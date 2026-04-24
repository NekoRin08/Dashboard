import streamlit as st
import pandas as pd
import plotly.express as px

# Ambil Data
def load_data():
    df = pd.read_csv("dataset\covid_19_indonesia_time_series_all.csv")
    return df

def fldt(df, year=None):
    if year:
        df = df[df['Date'].astype(str).str.contains(str(year))]
    return df

# Fungsi Select Year
def slyr():
    return st.sidebar.selectbox(
    "Pilih Tahun 📅", 
    options=[None, 2020, 2021, 2022], 
    format_func=lambda x: "Semua Tahun" if x is None else str(x)
)

def show_data(df):
    selected_columns = ['Location'] + list(df.loc[:, 'New Cases' : 'Total Recovered'].columns)
    df_selected = df[selected_columns]
    st.subheader
    st.dataframe (df_selected.head(10))

# def show_data():
    #df = load_data()
    #st.subheader("📌 Data COVID-19 Indonesia")
    #st.dataframe(df.head(10))
# Menampilkan statistik deskriptif dataset 
    #st.subheader("📕 Statistik Deskriptif Dataset")
    #st.write(df.describe()) # Menampilkan statistik deskriptif

#Total Kasus
def totus (df):
    total_kasus = df['Total Cases'].sum()
    return total_kasus

#Total Death
def toted(df):
    total_kematian = df['Total Deaths'].sum()
    return total_kematian

#Total Sembuh
def todry(df):
    total_sembuh = df['Total Recovered'].sum()
    return total_sembuh

def klm(df) :
    ks = totus(df)
    dd = toted(df)
    sb = todry(df)

    col1, col2, col3, = st.columns(3)
    col1.metric(label="Total Kasus 📈", value=f"{ks/1000:.1f}K", border= True)
    col2.metric(label="Total Kematian 💀", value=f"{dd/1000:.1f}K", border = True)
    col3.metric(label="Total Sembuh 💃", value=f"{sb/1000:.1f}K", border = True)

def pct1 (df):
    #Pemanggilan Data
    total_mati = toted(df)
    total_sumbuh = todry(df)

    #dataframe
    data = {
        'Status' : ['Meninggal', 'Sembuh'],
        'Jumlah' : [total_mati, total_sumbuh]
    }

    fig = px.pie(
        data,
        names = 'Status',
        values = 'Jumlah',
        title = 'Perbandingan Total kematian VS Total Sembuh',
        hole = 0.5,
        color_discrete_sequence= ['#4de89f', '#ff6459']
    )

    st.plotly_chart(fig, use_container_width=True)