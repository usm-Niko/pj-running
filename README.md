# pj-running
# Análisis de Rendimiento en Entrenamientos de Running por Intervalos

## Integrantes
* Nicolás Espinoza

## Descripción breve del problema
El entrenamiento de running moderno se apoya fuertemente en la recolección de datos mediante smartwatches. Sin embargo, muchos corredores aficionados tienen dificultades para interpretar cómo factores externos e internos (específicamente la altimetría del terreno) impactan directamente en su rendimiento durante sesiones explosivas. El problema central consiste en determinar qué variables del entorno físico generan un mayor impacto en el desgaste (frecuencia cardíaca) y el desempeño (ritmo) durante este tipo específico de entrenamientos.

## Motivación
Ayudar a los deportistas a planificar de manera más eficiente e inteligente sus rutas de entrenamiento, comprendiendo de antemano cómo el desnivel del terreno afectará su esfuerzo físico y su capacidad de recuperación en sesiones de alta intensidad.

## Pregunta inicial
¿Cómo influyen los cambios de elevación (altimetría) (X) en el ritmo promedio y la frecuencia cardíaca (Y) durante entrenamientos de intervalos cortos de aproximadamente 20 minutos registrados recientemente (T)?

## Alcance
* **Unidad de análisis:** Sesiones individuales de entrenamiento corto enfocado en intervalos.
* **Inclusiones:** Métricas directas de rendimiento (pace/ritmo, pulsaciones) y variables del entorno (desnivel acumulado).
* **Exclusiones:** Se descartan maratones, carreras de resistencia prolongadas (varias horas), datos de nutrición y el desgaste del calzado deportivo.

## Fuente del dataset
Se utilizará un dataset público extraído de Kaggle (por definir específicamente entre variantes de *Strava Runner Data* o *Apple Health Workout Export*) que contenga registros de actividades deportivas individuales tabuladas.

## Breve descripción de los datos
El conjunto de datos representará sesiones de entrenamiento y contendrá suficiente riqueza para construir representaciones visuales, incluyendo:
* **Variables numéricas:** Distancia, frecuencia cardíaca promedio y máxima, ritmo (pace), desnivel positivo/negativo.
* **Información temporal:** Duración de la sesión, fecha y hora de inicio.
* **Variables categóricas:** Tipo de terreno o clima (si está disponible en la fuente).

## Estructura general del repositorio
El repositorio seguirá la siguiente estructura inicial sugerida para mantener el trabajo ordenado y reproducible:

```text
proyecto-visualizacion/
|
|-- data/
|   |-- raw/          # datos originales sin modificar
|   '-- processed/    # datos generados luego de limpieza y transformación
|
|-- notebooks/
|   '-- 01_exploracion.ipynb  # exploración, limpieza, análisis y pruebas
|
|-- src/              # funciones o código reutilizable
|
|-- figures/          # gráficos y recursos visuales
|
|-- app/              # aplicación Streamlit o componentes del producto final
|
|-- README.md         # documentación principal del proyecto
|
'-- .gitignore        # archivos que no deben almacenarse en GitHub