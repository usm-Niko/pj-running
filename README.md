# 🏃‍♂️ Análisis de Rendimiento en Entrenamientos de Running

## 1. Problema y Pregunta
El objetivo de este proyecto es determinar qué factores del entorno físico impactan en el desgaste y rendimiento de un corredor aficionado.
**Pregunta Analítica:** ¿Cómo influyen los cambios de elevación (X) en el ritmo promedio y la frecuencia cardíaca (Y) durante entrenamientos de intervalos cortos registrados recientemente (T)?

## 2. Descripción del Dataset e Instrucciones para obtenerlo
Utilizamos el dataset "Running races from Strava", el cual contiene miles de registros reales de actividades de corredores (distancia, tiempo, desnivel positivo, frecuencia cardíaca, etc.).

**Obtención de los datos:**
1. Ingresar a Kaggle: `https://www.kaggle.com/datasets/olegoaer/running-races-strava`
2. Descargar el archivo `.zip` y extraer el documento `.csv`.
3. Renombrar el archivo a `raw-data-kaggle.csv` y ubicarlo dentro de la ruta `data/raw/` de este repositorio.

## 3. Estructura del Repositorio
```text
pj-running/
├── app/
│   ├── app.py
│   └── pages/
│       ├── 1_Exploracion.py
│       └── 2_Pregunta.py
├── data/
│   └── raw/
├── notebooks/
│   └── 02_eda.ipynb
├── README.md
└── requirements.txt