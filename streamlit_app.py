import streamlit as st

# ---------------------------------------------------
# CONFIGURACIÓN GENERAL
# ---------------------------------------------------

st.set_page_config(
    page_title="Gestión Biomédica SPORTMEDS",
    page_icon="assets/logo_sportmeds.png",
    layout="wide"
)

# ---------------------------------------------------
# ESTILOS PERSONALIZADOS
# ---------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #F5F7FA;
}

section[data-testid="stSidebar"] {
    background-color: #0D2B52;
}

section[data-testid="stSidebar"] * {
    color: white;
}

h1, h2, h3 {
    color: #0D2B52;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.image(
    "assets/logo_sportmeds.png",
    width=180
)

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

# ---------------------------------------------------
# CONTENIDO PRINCIPAL
# ---------------------------------------------------

st.title("Gestión Biomédica SPORTMEDS")

st.write("Sistema de gestión tecnológica biomédica")

# ---------------------------------------------------
# MÓDULOS
# ---------------------------------------------------

if modulo == "Inicio":

    st.header("Dashboard principal")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Equipos registrados",
            "245"
        )

    with col2:
        st.metric(
            "Riesgo alto",
            "18"
        )

    with col3:
        st.metric(
            "Mantenimientos próximos",
            "12"
        )

elif modulo == "Inventario":

    st.header("Inventario biomédico")

    nombre = st.text_input("Nombre del equipo")

    marca = st.text_input("Marca")

    if st.button("Registrar equipo"):
        st.success(f"{nombre} registrado correctamente")

elif modulo == "Tecnovigilancia":

    st.header("Tecnovigilancia")

    evento = st.text_area("Descripción del evento")

    if st.button("Guardar evento"):
        st.success("Evento registrado correctamente")

elif modulo == "Gestión de riesgos":

    st.header("Gestión de riesgos")

    probabilidad = st.slider(
        "Probabilidad",
        1,
        5
    )

    impacto = st.slider(
        "Impacto",
        1,
        5
    )

    riesgo = probabilidad * impacto

    st.metric(
        "Nivel de riesgo",
        riesgo
    )

elif modulo == "Mantenimiento":

    st.header("Mantenimiento preventivo")

    equipo = st.text_input("Equipo biomédico")

    if st.button("Programar mantenimiento"):
        st.success(f"Mantenimiento programado para {equipo}")
