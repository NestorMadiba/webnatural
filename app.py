import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Consulta Natural", page_icon="🌿", layout="wide")

# Encabezado con estilo
st.markdown("<h1 style='text-align: center; color: green;'>🌿 Consulta de Medicina Natural y Herboristería</h1>", unsafe_allow_html=True)
st.write("Ingrese un síntoma y obtenga recomendaciones de suplementos y plantas medicinales.")

# Sidebar con información
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/6/6b/Herbal_medicine.jpg", use_column_width=True)
st.sidebar.title("ℹ️ Información")
st.sidebar.write("Este sitio ofrece orientación general en medicina natural y herboristería. **No sustituye la consulta médica profesional.**")

# Cargar el Excel
df = pd.read_excel("sintomas.xlsx")

# Campo de entrada
sintoma = st.text_input("🔍 Escriba su síntoma:")

if sintoma:
    resultados = df[df["Síntoma"].str.contains(sintoma, case=False, na=False)]
    if not resultados.empty:
        for _, row in resultados.iterrows():
            st.subheader(f"✅ {row['Síntoma']}")
            st.write(f"**Suplemento dietario:** {row['Suplemento dietario']}")
            st.write(f"**Herboristería:** {row['Herboristería']}")
            st.write("---")
    else:
        st.warning("⚠️ No se encontró información para ese síntoma.")
