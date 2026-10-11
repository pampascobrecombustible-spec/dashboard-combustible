import streamlit as st
import pandas as pd
import plotly.express as px
import gdown
import os

st.set_page_config(
    page_title="Dashboard Combustible creado por Evelyn H.-MPC Octubre 2026",
    page_icon="⛽",
    layout="wide"
)

# -----------------------------
# DESCARGAR EXCEL DESDE DRIVE
# -----------------------------
FILE_ID = "1WMNKVyZCXGln4D8gTH107JsksH85OIg3"

url = f"https://drive.google.com/uc?id={FILE_ID}"

archivo = "data.xlsx"

if not os.path.exists(archivo):
    gdown.download(url, archivo, quiet=False)

# -----------------------------
# LEER EXCEL
# -----------------------------
xls = pd.ExcelFile(archivo)

st.sidebar.title("Filtros")

hoja = st.sidebar.selectbox(
    "Hoja",
    xls.sheet_names
)

df = pd.read_excel(archivo, sheet_name=hoja)

# -----------------------------
# LIMPIEZA
# -----------------------------
df.columns = df.columns.str.strip()

# -----------------------------
# TITULO
# -----------------------------
st.title("⛽ Dashboard de Combustible")

# -----------------------------
# KPI
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Registros",
    len(df)
)

col2.metric(
    "Columnas",
    len(df.columns)
)

if "VEHICULO/-EQUIPO" in df.columns:
    col3.metric(
        "Equipos",
        df["VEHICULO/-EQUIPO"].nunique()
    )

if "EMPRESA-USUARIA" in df.columns:
    col4.metric(
        "Empresas",
        df["EMPRESA-USUARIA"].nunique()
    )

st.divider()

# -----------------------------
# TABLA
# -----------------------------
with st.expander("Ver datos"):
    st.dataframe(
        df,
        use_container_width=True
    )

# -----------------------------
# GRAFICO EMPRESA
# -----------------------------
if "EMPRESA-USUARIA" in df.columns:

    empresa = (
        df["EMPRESA-USUARIA"]
        .value_counts()
        .reset_index()
    )

    empresa.columns = ["Empresa", "Registros"]

    fig = px.bar(
        empresa.head(10),
        x="Empresa",
        y="Registros",
        title="Top Empresas"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -----------------------------
# GRAFICO AREA
# -----------------------------
if "AREA-SPONSOR" in df.columns:

    area = (
        df["AREA-SPONSOR"]
        .value_counts()
        .reset_index()
    )

    area.columns = ["Area", "Registros"]

    fig2 = px.bar(
        area,
        x="Area",
        y="Registros",
        title="Consumo por Área"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# -----------------------------
# TOP EQUIPOS
# -----------------------------
if "VEHICULO/-EQUIPO" in df.columns:

    equipos = (
        df["VEHICULO/-EQUIPO"]
        .value_counts()
        .head(15)
        .reset_index()
    )

    equipos.columns = [
        "Equipo",
        "Abastecimientos"
    ]

    fig3 = px.bar(
        equipos,
        x="Equipo",
        y="Abastecimientos",
        title="Top 15 Equipos"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )
