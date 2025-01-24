# Comprensión de los datos - Descripción de los datos

## Análisis Exploratorio de los Datos

La Exploración Inicial de los Datos en la fase de Comprensión de los Datos del modelo CRISP-DM tiene como objetivo obtener una visión general de los datos para identificar características clave, patrones iniciales, y posibles problemas que puedan afectar el análisis posterior. Esta actividad se centra en conocer la estructura, calidad y propiedades básicas de los datos.

Entre las actividades a realizar se encuentra la inspección preliminar de: número de registros (filas), número y tipo de atributos (columnas) y la relación entre las tablas y conjuntos de datos recolectados hasta ahora.


### 1. Comprensión de la estructura de los datos

Antes de realizar cualquier análisis profundo, es importante comprender cómo están organizados los datos:

- Formato y tipo de archivo: Identificar si los datos están en archivos como CSV, Excel, JSON, bases de datos SQL o en formatos no estructurados como texto o imágenes.
- Dimensiones: Conocer el número de filas (registros) y columnas (atributos).
- Tipos de datos: Verificar los tipos de datos (numéricos, categóricos, booleanos, fechas, etc.) de cada columna. Esto permite detectar posibles inconsistencias (por ejemplo, fechas almacenadas como texto).

### 2. Resumen estadístico básico

En esta etapa, la generación de estadísticas descriptivas para cada variable ayuda a identificar patrones iniciales y posibles anomalías:
- Para variables numéricas:
- Media, mediana, mínimo, máximo, desviación estándar.
- Rango y percentiles.
- Para variables categóricas:
- Distribución de frecuencia.
- Proporción de cada categoría.

[Ejemplo 1 Analisis de la etructura de los datos y resumen estadístico](./excercise/exercise-1-EDA.ipynb)


## Detección de valores faltantes

El objetivo es identificar la presencia de valores nulos o faltantes en uestros datos, ya que pueden indicar problemas de la calidad de l los datos que deben ser resueltos. Por lo tanto realizaremos la siguientes actividades:

- Determinar cuántos valores están faltando en cada columna.
- Evaluar el impacto de los valores faltantes: ¿Son críticos para el análisis? ¿Es necesario imputarlos o eliminarlos?

[Ejemplo 2](./excercise/exercise-2-clean.ipynb)

## Identificación de valores atípicos

Los valores atípicos (outliers) pueden distorsionar el análisis si no se manejan adecuadamente. Por lo que, en esta actividad es necesario realizar la identificiación de valores atípicos, a partir de los siguientes pasos incluyen:

- Detectar valores extremos usando métodos estadísticos como:
- Rango intercuartílico (IQR).
- Análisis visual con boxplots.
- Determinar si los outliers son errores o datos legítimos.

[Ejemplo 3](./excercise/exercise-3-outlier.ipynb)


## Relación entre las variables

Explorar cómo se relacionan las variables entre sí ayuda a comprender la estructura de los datos y puede revelar patrones útiles:

Correlaciones:
- Para variables numéricas, calcular la correlación de Pearson o Spearman.
- Identificar relaciones lineales o no lineales.

Cruce de variables categóricas:
- Examinar tablas de contingencia para ver distribuciones conjuntas.

[Ejemplo 4](./excercise/exercise-4-correlation.ipynb)

## Visualización inicial de los datos

Generar visualizaciones es una forma poderosa de identificar patrones y problemas en los datos:

Distribución de datos:
- Histogramas para variables numéricas.
- Gráficos de barras para variables categóricas.

Relaciones entre variables:
- Diagramas de dispersión para pares de variables numéricas.
- Mapas de calor para matrices de correlación.


[Ejemplo 5]()
<!--
## Transformación, filtración y ordenamiento de datos

Ta transformación de datos consiste en convertir un dato en otro dato utilizando algún tipo de proceso transformativo.

La reestructuración de datos tiene que ver con ver tu conjunto de datos desde diferentes perspectivas.

La transformación es muy útil para limpiar nuestro dataset y para dejarlo preparado para futuros análisis estadísticos, mientras que la reestructuración nos ayuda a entender mejor nuestro conjunto de datos y extraer información valiosa que pueda ser luego analizada o visualizada.


[Ejemplo 3](./excercise/exercise-3-transform.ipynb)

>