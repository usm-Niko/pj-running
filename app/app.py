import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="App Running", layout="wide")

st.title("🏃‍♂️ Análisis de Rendimiento en Entrenamientos de Running")

st.header("1. Contexto del Proyecto")
st.markdown("""
El objetivo es determinar qué factores del entorno físico impactan en el desgaste y rendimiento de un corredor aficionado durante entrenamientos explosivos.

**Pregunta Analítica:**
¿Cómo influyen los cambios de elevación (X) en el ritmo promedio y la frecuencia cardíaca (Y) durante entrenamientos de intervalos cortos registrados recientemente (T)?
""")

st.header("2. Nuestros Datos y Limpieza")
st.markdown("""
Utilizamos el dataset "Running races from Strava". Para asegurar la calidad del análisis, tomamos las siguientes decisiones de limpieza:
* **Filtro de Alcance:** Se aislaron únicamente los entrenamientos cortos (menores a 30 minutos).
* **Valores Faltantes:** Se encontraron más de 18.000 registros sin frecuencia cardíaca (`average heart rate`), los cuales fueron eliminados por ser esenciales para nuestra variable Y.
* **Valores Atípicos:** Se calculó el ritmo (Pace) y se descartaron registros con ritmos irreales (menores a 2 min/km o mayores a 10 min/km).

Tras la limpieza, contamos con una muestra robusta de **más de 4.400 observaciones** para analizar.
""")

# Cargar y mostrar los datos
df = pd.read_csv('data/raw/raw-data-kaggle.csv', sep=';')
df_cortos = df[df['elapsed time (s)'] <= 1800].copy()
df_clean = df_cortos.dropna(subset=['average heart rate (bpm)']).copy()
df_clean['pace_min_km'] = (df_clean['elapsed time (s)'] / 60) / (df_clean['distance (m)'] / 1000)
df_clean = df_clean[(df_clean['pace_min_km'] >= 2) & (df_clean['pace_min_km'] <= 10)]

# Mostramos una muestra de la tabla en la app
st.dataframe(df_clean.head())