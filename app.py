from pathlib import Path
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Configuración general de la página
st.set_page_config(
    page_title="Analítica de Ingresos · Potato Inc.",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Rutas relativas seguras desde la raíz del repositorio
BASE_DIR = Path(__file__).resolve().parent
PATH_PREPARADO = BASE_DIR / "src" / "sincronicas" / "datos" / "company_dataset_preparado.csv"
PATH_SUBCAT = BASE_DIR / "src" / "sincronicas" / "reportes" / "tabla_desempeno_subcategorias.csv"
PATH_ANUAL = BASE_DIR / "src" / "sincronicas" / "reportes" / "tabla_evolucion_anual.csv"


@st.cache_data
def cargar_datos():
    df_prep = pd.read_csv(PATH_PREPARADO)
    df_subcat = pd.read_csv(PATH_SUBCAT)
    df_anual = pd.read_csv(PATH_ANUAL)

    # Asegurar columna total anual consolidado si no viene precalculada en el CSV
    if "Total_Anual_MM" not in df_anual.columns:
        df_anual["Total_Anual_MM"] = (
            df_anual["Revenue By Product"] + df_anual["Revenue By Region"]
        ).round(2)
    return df_prep, df_subcat, df_anual


df_prep, df_subcat, df_anual = cargar_datos()

# ==================== BARRA LATERAL ====================
with st.sidebar:
    st.title("📊 Potato Inc.")
    st.caption("Proyecto Integrador III · Analítica de Datos")
    st.markdown("---")
    st.markdown("**Autor:** Jorge Mario Paniagua Saraz")
    st.markdown("**Institución:** IU Digital de Antioquia")
    st.markdown("**Dataset:** `dune123/company_dataset`")
    st.markdown("**Cobertura:** 2015 Q1 – 2023 Q3 (35 trimestres)")
    st.markdown("---")
    st.info(
        "💡 **Navegación:** Utiliza las pestañas superiores para recorrer el "
        "contexto del negocio, las métricas por pregunta y las conclusiones."
    )

# ==================== ENCABEZADO Y KPIs GLOBALES ====================
st.title("Análisis Descriptivo de Ingresos Trimestrales — Potato Inc.")
st.markdown(
    "Diagnóstico financiero consolidado por **Línea de Producto** y **Región Geográfica** "
    "durante el periodo **2015 Q1 – 2023 Q3** (cifras expresadas en **Miles de Millones — MM**)."
)

# Extracción de indicadores clave desde los datos reales
top_prod = df_subcat[df_subcat["Category"] == "Revenue By Product"].iloc[0]
top_reg = df_subcat[df_subcat["Category"] == "Revenue By Region"].iloc[0]
pico_anual = df_anual.loc[df_anual["Total_Anual_MM"].idxmax()]

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(
        label="Registros Procesados",
        value=f"{len(df_prep)} obs.",
        delta="35 trimestres (0 nulos)",
    )
with col2:
    st.metric(
        label="Líder en Producto (Smartphones)",
        value=f"${top_prod['Ingreso_Total_MM']:,.2f} MM",
        delta=f"{top_prod['Participacion_Promedio_Pct']:.2f}% prom. categoría",
    )
with col3:
    st.metric(
        label="Líder en Región (Americas)",
        value=f"${top_reg['Ingreso_Total_MM']:,.2f} MM",
        delta=f"{top_reg['Participacion_Promedio_Pct']:.2f}% prom. categoría",
    )
with col4:
    st.metric(
        label=f"Pico Histórico Anual ({int(pico_anual['Año'])})",
        value=f"${pico_anual['Total_Anual_MM']:,.2f} MM",
        delta="Máximo consolidado",
    )

st.markdown("---")

# ==================== PESTAÑAS DE NAVEGACIÓN ====================
tab1, tab2, tab3, tab4 = st.tabs(
    [
        "1️⃣ Contexto y Datos",
        "2️⃣ Pregunta 1: Subcategorías",
        "3️⃣ Pregunta 2: Evolución Anual",
        "4️⃣ Conclusiones y Limitaciones",
    ]
)

# -------------------- TAB 1: CONTEXTO Y DATOS --------------------
with tab1:
    st.header("Necesidad del Negocio e Identificación del Dataset")

    c_izq, c_der = st.columns(2)
    with c_izq:
        st.subheader("🎯 Planteamiento de la Necesidad")
        st.write(
            "- **Beneficiario:** Gerencia de Finanzas y Vicepresidencia Estratégica de **Potato Inc.**\n"
            "- **Problema:** Ausencia de un marco analítico unificado que compare de forma directa "
            "cómo fluctúan los ingresos trimestrales entre líneas de producto y regiones geográficas.\n"
            "- **Objetivo:** Caracterizar de forma descriptiva la evolución temporal y la distribución "
            "de los ingresos entre 2015 Q1 y 2023 Q3 mediante métricas acumuladas, promedios y participación porcentual."
        )

        st.subheader("❓ Preguntas de Negocio")
        st.info(
            "**Pregunta 1:** ¿Cuáles son las subcategorías con mayor aporte financiero acumulado "
            "y promedio dentro de las dimensiones de Producto y Región?\n\n"
            "**Pregunta 2:** ¿Cómo han evolucionado los ingresos consolidados año tras año entre "
            "la dimensión de Producto y Región durante el periodo 2015 – 2023?"
        )

    with c_der:
        st.subheader("🗂️ Identificación y Enriquecimiento del Dataset")
        st.write(
            "- **Fuente:** Hugging Face Datasets (`dune123/company_dataset`).\n"
            "- **Granularidad:** 350 registros balanceados (175 en `Revenue By Product` y 175 en `Revenue By Region`) "
            "a lo largo de 35 trimestres consecutivos.\n"
            "- **Variables Enriquecidas (AE3):**\n"
            "  1. `Año` (`int`): Año extraído de `Period`.\n"
            "  2. `Trimestre` (`str`): Trimestre (`Q1` a `Q4`).\n"
            "  3. `Valor_Miles_Millones` (`float`): Ingreso escalado dividiendo el valor bruto entre $10^9$.\n"
            "  4. `Participacion_Categoria_Pct` (`float`): Peso porcentual de cada subcategoría dentro de su categoría por trimestre."
        )

    st.subheader("🔍 Explorador del Dataset Preparado (`company_dataset_preparado.csv`)")
    cat_filtro = st.selectbox(
        "Filtrar vista previa por Categoría:",
        options=["Todas"] + sorted(df_prep["Category"].unique().tolist()),
    )
    df_vista = df_prep if cat_filtro == "Todas" else df_prep[df_prep["Category"] == cat_filtro]
    st.dataframe(df_vista, use_container_width=True, height=280)

# -------------------- TAB 2: PREGUNTA 1 --------------------
with tab2:
    st.header("Pregunta 1: Desempeño Acumulado y Promedio por Subcategoría")

    st.markdown(
        "**Definición de métricas utilizadas:**\n"
        "- **Ingreso Total Acumulado (MM):** $\\sum \\text{Valor\\_Miles\\_Millones}$ durante los 35 trimestres (2015 Q1 – 2023 Q3).\n"
        "- **Ingreso Promedio Trimestral (MM):** Media aritmética de los ingresos trimestrales por subcategoría.\n"
        "- **Ingreso Mediano (MM):** Percentil 50 (valor central robusto frente a trimestres atípicos).\n"
        "- **Participación Promedio (%):** Media del indicador $(\\text{Ingreso Subcategoría} / \\text{Total Categoría en el Trimestre}) \\times 100$."
    )

    dim_seleccionada = st.radio(
        "Selecciona la dimensión estratégica a visualizar:",
        options=["Revenue By Product", "Revenue By Region"],
        horizontal=True,
    )

    df_dim = df_subcat[df_subcat["Category"] == dim_seleccionada].sort_values(
        by="Ingreso_Total_MM", ascending=True
    )

    g1, g2 = st.columns([3, 2])
    with g1:
        fig_bar = px.bar(
            df_dim,
            x="Ingreso_Total_MM",
            y="Sub Cat",
            orientation="h",
            text=df_dim["Ingreso_Total_MM"].apply(lambda x: f"${x:,.2f} MM"),
            color="Ingreso_Total_MM",
            color_continuous_scale="Blues",
            title=f"Ingreso Total Acumulado por Subcategoría — {dim_seleccionada} (2015 Q1 – 2023 Q3)",
            labels={
                "Ingreso_Total_MM": "Ingreso Acumulado (Miles de Millones - MM)",
                "Sub Cat": "Subcategoría",
            },
        )
        fig_bar.update_traces(textposition="outside")
        fig_bar.update_layout(showlegend=False, coloraxis_showscale=False, xaxis_range=[0, df_dim["Ingreso_Total_MM"].max() * 1.22])
        st.plotly_chart(fig_bar, use_container_width=True)

    with g2:
        fig_pie = px.pie(
            df_dim,
            values="Ingreso_Total_MM",
            names="Sub Cat",
            hole=0.42,
            title=f"Distribución Porcentual — {dim_seleccionada}",
        )
        fig_pie.update_traces(textposition="inside", textinfo="percent+label")
        st.plotly_chart(fig_pie, use_container_width=True)

    st.subheader("📋 Tabla Consolidada de Resultados por Subcategoría")
    st.dataframe(df_subcat, use_container_width=True)

    st.success(
        "**Interpretación y Apoyo a la Decisión:**\n"
        "- **En Producto:** `Smartphones` lidera con **$7,198.22 MM** acumulados (promedio de **$205.66 MM/trimestre** y **52.31%** de participación promedio), "
        "seguido por `Services` con **$2,392.66 MM** (**18.78%**). Esto muestra una alta dependencia del hardware móvil, pero consolida a `Services` como segunda fuente clave de ingresos.\n"
        "- **En Región:** `Americas` encabeza la facturación con **$6,379.47 MM** (**43.24%** de participación), seguida por `Europe` (**$3,466.22 MM**, **23.07%**) y `Greater China` (**$2,725.24 MM**, **18.96%**).\n"
        "- **Decisión que apoya:** Priorizar estrategias de retención y venta cruzada (*cross-selling*) de servicios en los mercados de `Americas` y `Europe`, donde se concentra más del 66% de la facturación geográfica."
    )

# -------------------- TAB 3: PREGUNTA 2 --------------------
with tab3:
    st.header("Pregunta 2: Evolución Anual y Trimestral de los Ingresos (2015 – 2023)")

    st.markdown(
        "**Definición de métricas utilizadas:**\n"
        "- **Ingreso Anual por Categoría (MM):** Suma de `Valor_Miles_Millones` agrupada por `Año` y `Category`.\n"
        "- **Nota de cobertura:** Los años 2015 a 2022 contienen 4 trimestres completos (`Q1–Q4`), mientras que **2023 incluye hasta `Q3`** (3 trimestres)."
    )

    df_anual_melt = df_anual.melt(
        id_vars=["Año"],
        value_vars=["Revenue By Product", "Revenue By Region"],
        var_name="Categoría",
        value_name="Ingreso_MM",
    )

    fig_linea = px.line(
        df_anual_melt,
        x="Año",
        y="Ingreso_MM",
        color="Categoría",
        markers=True,
        text=df_anual_melt["Ingreso_MM"].apply(lambda x: f"${x:,.0f}"),
        title="Evolución Anual de Ingresos por Dimensión (2015 – 2023 Q3) [Miles de Millones]",
        labels={
            "Año": "Año",
            "Ingreso_MM": "Ingreso Anual (Miles de Millones - MM)",
            "Categoría": "Dimensión",
        },
    )
    fig_linea.update_traces(textposition="top center", line=dict(width=3), marker=dict(size=8))
    fig_linea.update_xaxes(dtick=1)
    st.plotly_chart(fig_linea, use_container_width=True)

    st.subheader("🔎 Explorador de Tendencia Trimestral por Subcategoría")
    subcats_sel = st.multiselect(
        "Selecciona una o varias subcategorías para comparar su trayectoria trimestral:",
        options=sorted(df_prep["Sub Cat"].unique().tolist()),
        default=["Smartphones", "Services", "Americas", "Europe"],
    )

    if subcats_sel:
        df_trim = df_prep[df_prep["Sub Cat"].isin(subcats_sel)].sort_values(by=["Año", "Trimestre"])
        fig_trim = px.line(
            df_trim,
            x="Period",
            y="Valor_Miles_Millones",
            color="Sub Cat",
            markers=True,
            title="Evolución Trimestral Detallada (2015 Q1 – 2023 Q3) [MM]",
            labels={
                "Period": "Trimestre",
                "Valor_Miles_Millones": "Ingreso Trimestral (MM)",
                "Sub Cat": "Subcategoría",
            },
        )
        fig_trim.update_xaxes(tickangle=-45)
        st.plotly_chart(fig_trim, use_container_width=True)

    st.subheader("📋 Tabla de Evolución Anual Consolidada (MM)")
    st.dataframe(df_anual, use_container_width=True)

    st.success(
        "**Interpretación y Apoyo a la Decisión:**\n"
        "- Entre **2017** ($2,170.43 MM consolidados) y **2022** ($4,789.48 MM consolidados) se observa una expansión sostenida, "
        "duplicando el volumen de ingresos en un lapso de cinco años.\n"
        "- En los primeros tres trimestres de **2023 (Q1–Q3)** se acumulan **$1,619.30 MM** en Producto y **$1,575.66 MM** en Región ($3,194.96 MM consolidados), "
        "manteniendo un ritmo superior al periodo 2015–2020.\n"
        "- **Decisión que apoya:** Planificar la capacidad logística y presupuestaria considerando los picos estacionales observados en los cierres de año (Q4) y monitorear la desaceleración relativa tras el máximo de 2022."
    )

# -------------------- TAB 4: CONCLUSIONES Y LIMITACIONES --------------------
with tab4:
    st.header("Conclusiones, Recomendaciones y Limitaciones del Estudio")

    col_c, col_r = st.columns(2)
    with col_c:
        st.subheader("✅ Conclusiones Principales")
        st.write(
            "1. **Concentración por Producto:** `Smartphones` genera el **52.31%** de la participación promedio en su categoría ($7,198.22 MM), "
            "consolidándose como el eje central de ingresos, respaldado por `Services` (18.78%).\n"
            "2. **Concentración Geográfica:** `Americas` aporta el **43.24%** de los ingresos regionales ($6,379.47 MM), seguida por `Europe` (23.07%) y `Greater China` (18.96%).\n"
            "3. **Crecimiento Histórico:** La compañía mostró una tendencia expansiva clara entre 2017 y 2022, alcanzando su pico máximo en 2022 ($4,789.48 MM).\n"
            "4. **Trazabilidad Analítica:** El flujo automatizado en Python y Pandas garantizó integridad total (350 registros, 0 nulos) y consistencia entre el notebook, los reportes CSV y esta aplicación."
        )

    with col_r:
        st.subheader("🚀 Recomendaciones Estratégicas")
        st.write(
            "1. **Diversificación de Portafolio:** Impulsar el crecimiento de `Services` y `Computers` para reducir la alta exposición financiera a un solo producto (`Smartphones`).\n"
            "2. **Expansión en Mercados Secundarios:** Evaluar estrategias comerciales en `Japan` (8.07%) y `Rest of Asia Pacific` (6.66%), que presentan la menor participación regional.\n"
            "3. **Incorporación de Datos de Costos:** Integrar en futuras fases métricas de margen bruto, costos operativos y precios unitarios para evaluar rentabilidad real."
        )

    st.warning(
        "⚠️ **Limitaciones del Análisis (Alcance Metodológico):**\n"
        "- **Ingresos vs. Rentabilidad:** Los datos representan exclusivamente **ingresos brutos**; al no contar con costos ni gastos operativos, no es posible afirmar qué subcategoría es más rentable.\n"
        "- **Naturaleza de los Datos:** La variable `Value - Randomized` proviene de un conjunto público con valores aleatorizados/sintéticos, por lo que los montos responden a un ejercicio analítico y no a estados financieros auditados.\n"
        "- **Periodo Parcial en 2023:** El año 2023 contiene información únicamente hasta el tercer trimestre (`2023 Q3`), por lo que no debe compararse directamente como año completo frente a 2015–2022.\n"
        "- **Carácter Descriptivo:** El estudio identifica tendencias y concentraciones históricas sin establecer relaciones de causalidad ni modelos predictivos."
    )