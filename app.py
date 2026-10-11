import streamlit as st
import pandas as pd
import plotly.express as px
import gdown
import os

st.set_page_config(
    page_title="Dashboard Combustible",
    layout="wide"
)

# ID del archivo de Google Drive
FILE_ID = "1WMNKVyZCXGln4D8gTH107JsksH85OIg3"

# Descargar Excel
url = f"https://drive.google.com/uc?id={FILE_ID}"

archivo = "data.xlsx"

if not os.path.exists(archivo):
    gdown.download(url, archivo, quiet=False)

# Leer Excel
xls = pd.ExcelFile(archivo)

st.sidebar.title("Hojas disponibles")

hoja = st.sidebar.selectbox(
    "Seleccionar hoja",
    xls.sheet_names
)

df = pd.read_excel(archivo, sheet_name=hoja)

st.title("🚛 Dashboard de Combustible")

st.write("Vista previa de datos")

st.dataframe(df)

st.subheader("Información general")

col1, col2 = st.columns(2)

col1.metric("Registros", len(df))
col2.metric("Columnas", len(df.columns))

st.subheader("Columnas disponibles")

st.write(list(df.columns))
