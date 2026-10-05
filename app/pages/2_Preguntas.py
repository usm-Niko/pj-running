import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Pregunta Analítica", layout="wide")
st.title("🎯 Impacto de la Elevación (X) en el Esfuerzo (Y)")

# Carga y limpieza de datos
df = pd.read_csv('data/raw/raw-data-kaggle.csv', sep=';')
df_clean = df[df['elapsed time (s)'] <= 1800].dropna(subset=['average heart rate (bpm)']).copy()
df_clean['pace_min_km'] = (df_clean['elapsed time (s)'] / 60) / (df_clean['distance (m)'] / 1000)
df_clean = df_clean[(df_clean['pace_min_km'] >= 2) & (df_clean['pace_min_km'] <= 10)]

fig_dispersion = px.scatter(df_clean, x='elevation gain (m)', y='average heart rate (bpm)', 
                            color='pace_min_km', opacity=0.6,
                            labels={'elevation gain (m)': 'Desnivel Positivo (m)', 
                                    'average heart rate (bpm)': 'Pulsaciones (lpm)',
                                    'pace_min_km': 'Ritmo'})
st.plotly_chart(fig_dispersion, use_container_width=True)

st.info("""
**📝 Interpretación de los Resultados:**
En entrenamientos cortos (menores a 30 minutos), la altimetría del terreno no parece ser el factor principal del desgaste cardiovascular. Como vemos por el color de los puntos, los ritmos más rápidos (tonos oscuros) tienden a concentrar las frecuencias cardíacas más altas, incluso en terrenos completamente planos. Esto sugiere que la intensidad del intervalo (el ritmo) predomina sobre el entorno físico (las subidas) a la hora de elevar las pulsaciones.
""")