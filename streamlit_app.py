import streamlit as st
import os
import pandas as pd
from datetime import date

# ---------------------------------------------------
# CONFIGURACIÓN GENERAL
# ---------------------------------------------------
st.set_page_config(
    page_title="Gestión Biomédica SPORTMEDS",
    page_icon="⚕️",
    layout="wide"
)

# ---------------------------------------------------
# ESTILOS PERSONALIZADOS
# ---------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

* { font-family: 'Inter', sans-serif; }

.main {
    background-color: #F5F7FA;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0D2B52 0%, #1a4a8a 100%);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

section[data-testid="stSidebar"] .stSelectbox label {
    color: #a8c6f0 !important;
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

section[data-testid="stSidebar"] hr {
    border-color: rgba(255,255,255,0.2);
}

h1, h2, h3 {
    color: #0D2B52;
}

.metric-card {
    background: white;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 2px 8px rgba(13,43,82,0.08);
    border-left: 4px solid #1a8fd1;
}

.stMetric {
    background: white;
    border-radius: 12px;
    padding: 1rem;
    box-shadow: 0 2px 8px rgba(13,43,82,0.08);
}

.stButton > button {
    background: linear-gradient(135deg, #0D2B52, #1a8fd1);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 0.5rem 1.5rem;
    font-weight: 600;
    transition: opacity 0.2s;
}

.stButton > button:hover {
    opacity: 0.85;
    color: white;
}

.sidebar-logo-container {
    display: flex;
    justify-content: center;
    padding: 1rem 0 0.5rem 0;
}

.version-tag {
    font-size: 0.7rem;
    color: rgba(255,255,255,0.45);
    text-align: center;
    padding-bottom: 0.5rem;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR — LOGO + MENÚ
# ---------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(BASE_DIR, "assets", "logo_sportmeds.png")

with st.sidebar:
    # Logo centrado en la parte superior
    if os.path.exists(logo_path):
        col_logo = st.columns([1, 3, 1])
        with col_logo[1]:
            st.image(logo_path, use_container_width=True)
    else:
        st.markdown(
            "<div style='text-align:center; font-size:1.4rem; font-weight:700;"
            " padding:1rem 0;'>⚕️ SPORTMEDS</div>",
            unsafe_allow_html=True
        )

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("### Menú Principal")

    modulo = st.selectbox(
        "Seleccione un módulo",
        [
            "🏠 Inicio",
            "📦 Inventario",
            "🔍 Tecnovigilancia",
            "⚠️ Gestión de riesgos",
            "🔧 Mantenimiento"
        ]
    )

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(
        "<div class='version-tag'>Sistema de Gestión Biomédica v1.0<br>"
        "© 2025 SPORTMEDS Centro Médico</div>",
        unsafe_allow_html=True
    )

# ---------------------------------------------------
# ENCABEZADO PRINCIPAL
# ---------------------------------------------------
st.title("Gestión Biomédica SPORTMEDS")
st.caption("Sistema integrado de gestión tecnológica biomédica")
st.markdown("---")

# ---------------------------------------------------
# MÓDULO: INICIO
# ---------------------------------------------------
if "Inicio" in modulo:
    st.header("📊 Dashboard principal")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Equipos registrados", "245", "+3 este mes")
    with col2:
        st.metric("Riesgo alto", "18", "-2 vs mes anterior", delta_color="inverse")
    with col3:
        st.metric("Mantenimientos próximos", "12")
    with col4:
        st.metric("Eventos tecnovigilancia", "5", "+1 esta semana", delta_color="inverse")

    st.markdown("---")
    st.subheader("Resumen por servicio")

    data = {
        "Servicio": ["UCI", "Urgencias", "Hospitalización", "Consulta externa"],
        "Equipos": [68, 52, 89, 36],
        "Mantenimientos pendientes": [3, 5, 2, 2],
        "Riesgo alto": [7, 6, 3, 2],
    }
    st.dataframe(pd.DataFrame(data), use_container_width=True)

# ---------------------------------------------------
# MÓDULO: INVENTARIO
# ---------------------------------------------------
elif "Inventario" in modulo:
    st.header("📦 Inventario biomédico")

    with st.form("form_inventario", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            nombre = st.text_input("Nombre del equipo *")
            marca = st.text_input("Marca *")
            modelo = st.text_input("Modelo")
            serie = st.text_input("Número de serie")
        with col2:
            servicio = st.selectbox(
                "Servicio *",
                ["UCI", "Urgencias", "Hospitalización", "Consulta externa"]
            )
            clasificacion = st.selectbox(
                "Clasificación de riesgo (INVIMA)",
                ["Clase I", "Clase IIa", "Clase IIb", "Clase III"]
            )
            fecha_adquisicion = st.date_input("Fecha de adquisición", value=date.today())
            vida_util = st.number_input("Vida útil estimada (años)", min_value=1, max_value=30, value=5)

        observaciones = st.text_area("Observaciones")
        submitted = st.form_submit_button("✅ Registrar equipo")

        if submitted:
            if nombre and marca and servicio:
                st.success(f"✅ **{nombre}** ({marca}) registrado correctamente en el servicio de **{servicio}**.")
            else:
                st.error("Por favor complete los campos obligatorios (*).")

    st.markdown("---")
    st.subheader("Equipos registrados")
    demo_inventario = {
        "Equipo": ["Ventilador Mecánico", "Monitor Multiparámetro", "Desfibrilador", "Bomba de Infusión"],
        "Marca": ["Dräger", "Mindray", "Zoll", "Fresenius"],
        "Servicio": ["UCI", "Urgencias", "UCI", "Hospitalización"],
        "Riesgo": ["Clase III", "Clase IIb", "Clase III", "Clase IIa"],
    }
    st.dataframe(pd.DataFrame(demo_inventario), use_container_width=True)

# ---------------------------------------------------
# MÓDULO: TECNOVIGILANCIA
# ---------------------------------------------------
elif "Tecnovigilancia" in modulo:
    st.header("🔍 Tecnovigilancia")
    st.caption("Registro de eventos e incidentes adversos con dispositivos médicos")

    with st.form("form_tecnovigilancia", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            equipo_tv = st.text_input("Equipo involucrado *")
            fecha_evento = st.date_input("Fecha del evento", value=date.today())
            tipo_evento = st.selectbox(
                "Tipo de evento",
                ["Incidente", "Casi incidente", "Evento adverso serio", "Falla del equipo"]
            )
        with col2:
            reportador = st.text_input("Nombre del reportador")
            cargo = st.text_input("Cargo")
            servicio_tv = st.selectbox(
                "Servicio",
                ["UCI", "Urgencias", "Hospitalización", "Consulta externa"]
            )

        descripcion = st.text_area("Descripción detallada del evento *", height=120)
        accion = st.text_area("Acción inmediata tomada", height=80)
        submitted_tv = st.form_submit_button("📋 Guardar reporte")

        if submitted_tv:
            if equipo_tv and descripcion:
                st.success("✅ Evento de tecnovigilancia registrado correctamente.")
                st.info("📧 Se notificará al coordinador biomédico para seguimiento.")
            else:
                st.error("Complete los campos obligatorios (*).")

# ---------------------------------------------------
# MÓDULO: GESTIÓN DE RIESGOS
# ---------------------------------------------------
elif "Gestión de riesgos" in modulo:
    st.header("⚠️ Gestión de riesgos")

    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("Evaluación de riesgo")
        equipo_riesgo = st.text_input("Equipo a evaluar")
        probabilidad = st.slider("Probabilidad de falla", 1, 5, 3,
                                  help="1=Muy baja, 5=Muy alta")
        impacto = st.slider("Impacto clínico", 1, 5, 3,
                             help="1=Mínimo, 5=Catastrófico")
        detectabilidad = st.slider("Detectabilidad", 1, 5, 3,
                                    help="1=Fácil de detectar, 5=Imposible de detectar")

        npr = probabilidad * impacto * detectabilidad

        if npr <= 10:
            nivel = "🟢 Bajo"
            color = "success"
        elif npr <= 30:
            nivel = "🟡 Medio"
            color = "warning"
        else:
            nivel = "🔴 Alto"
            color = "error"

        st.markdown("---")
        st.metric("NPR (Número de Prioridad de Riesgo)", npr)
        getattr(st, color)(f"Nivel de riesgo: **{nivel}**")

    with col2:
        st.subheader("Matriz de riesgo")
        matriz_data = {
            "": ["Catastrófico (5)", "Serio (4)", "Moderado (3)", "Menor (2)", "Mínimo (1)"],
            "Muy baja (1)": ["Medio", "Bajo", "Bajo", "Bajo", "Bajo"],
            "Baja (2)": ["Alto", "Medio", "Bajo", "Bajo", "Bajo"],
            "Media (3)": ["Alto", "Alto", "Medio", "Bajo", "Bajo"],
            "Alta (4)": ["Alto", "Alto", "Alto", "Medio", "Bajo"],
            "Muy alta (5)": ["Alto", "Alto", "Alto", "Alto", "Medio"],
        }
        st.dataframe(pd.DataFrame(matriz_data).set_index(""), use_container_width=True)

# ---------------------------------------------------
# MÓDULO: MANTENIMIENTO
# ---------------------------------------------------
elif "Mantenimiento" in modulo:
    st.header("🔧 Mantenimiento preventivo y correctivo")

    tab1, tab2 = st.tabs(["Programar mantenimiento", "Historial"])

    with tab1:
        with st.form("form_mantenimiento", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                equipo_mant = st.text_input("Equipo biomédico *")
                tipo_mant = st.selectbox(
                    "Tipo de mantenimiento",
                    ["Preventivo", "Correctivo", "Calibración", "Verificación"]
                )
                fecha_prog = st.date_input("Fecha programada", value=date.today())
            with col2:
                tecnico = st.text_input("Técnico responsable")
                prioridad = st.selectbox("Prioridad", ["Alta", "Media", "Baja"])
                costo_est = st.number_input("Costo estimado (COP)", min_value=0, step=10000)

            actividades = st.text_area("Actividades a realizar", height=100)
            submitted_mant = st.form_submit_button("📅 Programar mantenimiento")

            if submitted_mant:
                if equipo_mant:
                    st.success(
                        f"✅ Mantenimiento **{tipo_mant}** programado para **{equipo_mant}** "
                        f"el {fecha_prog.strftime('%d/%m/%Y')}."
                    )
                else:
                    st.error("Ingrese el nombre del equipo.")

    with tab2:
        st.subheader("Historial de mantenimientos")
        historial = {
            "Equipo": ["Ventilador Mecánico", "Monitor Multiparámetro", "Desfibrilador"],
            "Tipo": ["Preventivo", "Correctivo", "Calibración"],
            "Fecha": ["10/04/2025", "22/03/2025", "15/02/2025"],
            "Técnico": ["Juan García", "María López", "Carlos Ruiz"],
            "Estado": ["✅ Completado", "✅ Completado", "✅ Completado"],
        }
        st.dataframe(pd.DataFrame(historial), use_container_width=True)
