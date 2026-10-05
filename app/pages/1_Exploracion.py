import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Exploración", layout="wide")
st.title("📊 Análisis Exploratorio General")

# Carga y limpieza de datos
df = pd.read_csv('data/raw/raw-data-kaggle.csv', sep=';')
df_clean = df[df['elapsed time (s)'] <= 1800].dropna(subset=['average heart rate (bpm)']).copy()
df_clean['pace_min_km'] = (df_clean['elapsed time (s)'] / 60) / (df_clean['distance (m)'] / 1000)
df_clean = df_clean[(df_clean['pace_min_km'] >= 2) & (df_clean['pace_min_km'] <= 10)]

# --- EL CONTROL INTERACTIVO OBLIGATORIO ---
st.markdown("### Filtro Interactivo")
filtro_genero = st.selectbox("Filtra los datos por género:", ["Todos", "M", "F"])

# Aplicar el filtro
if filtro_genero != "Todos":
    df_filtrado = df_clean[df_clean['gender'] == filtro_genero]
else:
    df_filtrado = df_clean

st.subheader("1. Distribución del Ritmo (Pace)")
fig1 = px.histogram(df_filtrado, x='pace_min_km', nbins=40, color_discrete_sequence=['#1f77b4'])
st.plotly_chart(fig1, use_container_width=True)

st.subheader("2. Evolución Temporal del Esfuerzo")
df_filtrado['timestamp'] = pd.to_datetime(df_filtrado['timestamp'], format='%d/%m/%Y %H:%M')
df_filtrado['mes'] = df_filtrado['timestamp'].dt.month
df_mensual = df_filtrado.groupby('mes', as_index=False)['average heart rate (bpm)'].mean()

fig2 = px.line(df_mensual, x='mes', y='average heart rate (bpm)', markers=True)
st.plotly_chart(fig2, use_container_width=True)

st.subheader("3. Comparación de Esfuerzo por Género")
fig3 = px.box(df_clean, x='gender', y='average heart rate (bpm)', color='gender')
st.plotly_chart(fig3, use_container_width=True)

st.subheader("4. Mapa de Correlaciones")
columnas_num = ['distance (m)', 'elevation gain (m)', 'average heart rate (bpm)', 'pace_min_km']
matriz_corr = df_clean[columnas_num].corr()
fig4 = px.imshow(matriz_corr, text_auto=True, aspect="auto", color_continuous_scale='Blues')
st.plotly_chart(fig4, use_container_width=True)