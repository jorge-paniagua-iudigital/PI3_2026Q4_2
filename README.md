# Analítica Descriptiva de Ingresos Trimestrales — Potato Inc.

**Proyecto Integrador III · Analítica de Datos (Etapas AE2 – AE4)**  
**Autor:** Jorge Mario Paniagua Saraz (`mario.paniagua@est.iudigital.edu.co`)  
**Institución:** Institución Universitaria Digital de Antioquia  

---

## 🌐 Aplicación Interactiva Desplegada (Streamlit)

Accede al tablero interactivo en la nube aquí:  
👉 **[https://pi32026q42-dda4j9bqerr4yxwajucufx.streamlit.app/](https://pi32026q42-dda4j9bqerr4yxwajucufx.streamlit.app/)**

---

## 🎯 Necesidad del Negocio y Preguntas Analíticas

El proyecto atiende la necesidad de la Gerencia de Finanzas y Vicepresidencia Estratégica de **Potato Inc.** de consolidar y comparar el desempeño histórico de los ingresos trimestrales por **Línea de Producto** y **Región Geográfica** entre **2015 Q1 y 2023 Q3** (35 trimestres).

1. **Pregunta 1:** ¿Cuáles son las subcategorías con mayor aporte financiero acumulado y promedio dentro de las dimensiones de Producto y Región?
2. **Pregunta 2:** ¿Cómo han evolucionado los ingresos consolidados año tras año entre la dimensión de Producto y Región durante el periodo 2015 – 2023?

---

## 📂 Estructura del Repositorio y Rutas de Datos

```text
PI3_2026Q4_2/
├── .github/workflows/
│   └── run_notebook.yml                                      # Ejecución automática del notebook en GitHub Actions
├── src/sincronicas/
│   ├── Semana_2EA2.ipynb                                     # Notebook de extracción, limpieza, enriquecimiento y análisis
│   ├── datos/
│   │   ├── company_dataset.csv                               # Dataset crudo original (dune123/company_dataset, 350 filas)
│   │   └── company_dataset_preparado.csv                     # Dataset limpio y enriquecido (Año, Trimestre, MM, %)
│   └── reportes/
│       ├── tabla_desempeno_subcategorias.csv                 # Métricas consolidadas por subcategoría (Pregunta 1)
│       └── tabla_evolucion_anual.csv                         # Serie anual comparativa por categoría (Pregunta 2)
├── app.py                                                    # Aplicación web interactiva en Streamlit
├── Informe_Final_Proyecto_Integrador_PotatoInc.pdf           # Informe académico completo del proyecto (AE2 + AE3 + AE4)
├── requirements.txt                                          # Dependencias del proyecto
└── README.md                                                 # Documentación técnica y guía de ejecución
```

---

## ⚙️ Dependencias

Las librerías requeridas se encuentran declaradas en `requirements.txt`:

* `numpy` y `pandas`: manipulación, limpieza y agregación de datos.
* `matplotlib` y `plotly`: visualización estática e interactiva.
* `datasets`: extracción del conjunto de datos desde Hugging Face (`dune123/company_dataset`).
* `notebook`: ejecución reproducible del cuaderno Jupyter.
* `streamlit`: interfaz web interactiva del proyecto.

---

## 🚀 Instrucciones de Ejecución Local

1. **Clonar el repositorio e ingresar a la carpeta:**

   ```bash
   git clone https://github.com/jorge-paniagua-iudigital/PI3_2026Q4_2.git
   cd PI3_2026Q4_2
   ```

2. **Crear y activar el entorno virtual (Linux/macOS):**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación de Streamlit:**

   ```bash
   streamlit run app.py
   ```

   La aplicación quedará disponible en `http://localhost:8501`.