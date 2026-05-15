import streamlit as st

# Configuración básica
st.set_page_config(
    page_title="Gestión Biomédica SPORTMEDS",
    page_icon="🏥",
    layout="wide"
)

# Sidebar
st.sidebar.title("Menú Principal")

modulo = st.sidebar.selectbox(
    "Seleccione un módulo",
    [
        "Inicio",
        "Inventario",
        "Tecnovigilancia",
        "Gestión de riesgos",
        "Mantenimiento"
    ]
)

# Página principal
st.title("Gestión Biomédica SPORTMEDS")

st.write("Sistema de gestión tecnológica biomédica")

# Contenido según módulo
if modulo == "Inicio":
    st.header("Inicio")
    st.write("Dashboard principal del sistema.")

elif modulo == "Inventario":
    st.header("Inventario")
    st.write("Módulo de inventario biomédico.")

elif modulo == "Tecnovigilancia":
    st.header("Tecnovigilancia")
    st.write("Registro de eventos e incidentes.")

elif modulo == "Gestión de riesgos":
    st.header("Gestión de riesgos")

    probabilidad = st.slider("Probabilidad", 1, 5)
    impacto = st.slider("Impacto", 1, 5)

    riesgo = probabilidad * impacto

    st.metric("Nivel de riesgo", riesgo)

elif modulo == "Mantenimiento":
    st.header("Mantenimiento")

    equipo = st.text_input("Equipo biomédico")

    if st.button("Guardar"):
        st.success(f"{equipo} registrado correctamente")
