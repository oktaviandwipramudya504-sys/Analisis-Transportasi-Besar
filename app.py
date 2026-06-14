import streamlit as st
import pandas as pd
import plotly.express as px

# Konfigurasi Halaman
st.set_page_config(page_title="Dashboard Transportasi", layout="wide")

# Judul dan Deskripsi
st.title("📊 Analisis Data Transportasi Modern")
st.markdown("""
Dashboard interaktif ini menyajikan insight data transportasi, 
meliputi performa rute dan pengaruh kondisi cuaca terhadap jumlah penumpang.
""")

# Membaca data
@st.cache_data  # Optimasi agar data tidak dibaca ulang terus-menerus
def load_data():
    return pd.read_csv('transportation_large_data.csv')

df = load_data()

# Layout Dashboard
col1, col2 = st.columns(2)

with col1:
    st.subheader("Performa Penumpang per Rute")
    fig1 = px.bar(
        df.groupby('route_id')['passenger_count'].sum().reset_index(), 
        x='route_id', y='passenger_count', color='route_id',
        template="plotly_dark",
        title="Total Penumpang per Rute"
    )
    st.plotly_chart(fig1, width='stretch')

with col2:
    st.subheader("Dampak Cuaca terhadap Penumpang")
    fig2 = px.box(
        df, x='weather_condition', y='passenger_count', color='weather_condition',
        template="plotly_dark",
        title="Distribusi Penumpang per Cuaca"
    )
    st.plotly_chart(fig2, width='stretch')

# Tambahan: Statistik Ringkas
st.divider()
st.subheader("Ringkasan Statistik")
st.dataframe(df.describe(), width=1000)