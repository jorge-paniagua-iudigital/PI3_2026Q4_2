# Caracterización y Análisis Descriptivo de los Ingresos Trimestrales de Potato Inc. (2015 Q1 – 2023 Q3)

Este repositorio contiene el desarrollo de la **Primera Etapa (EA2 - Ideación, Diseño y Documentación de la Necesidad)** del Proyecto Integrador de Analítica de Datos. El objetivo principal es definir, diseñar y documentar una necesidad de información financiera para apoyar la toma de decisiones estratégicas, a partir de la exploración técnica de un dataset tabular obtenido de Hugging Face.

---

## 📌 Propósito y Necesidad Analítica
* **Beneficiario:** Gerencia de Finanzas y Vicepresidencia Estratégica de Potato Inc.
* **Escenario:** Escenario cuantitativo hipotético basado en series de tiempo trimestrales.
* **Necesidad de información:** La empresa requiere un diagnóstico consolidado que compare la evolución y participación de sus ingresos trimestrales según dos categorías clave: región geográfica (`Revenue By Region`) y línea de producto (`Revenue By Product`).
* **Pregunta de análisis:** ¿Cómo han evolucionado y se han distribuido los ingresos de Potato Inc. entre el primer trimestre de 2015 y el tercer trimestre de 2023 según las categorías de región y línea de producto?

---

## 📊 Ficha del Dataset
* **Identificador en Hugging Face:** [`dune123/company_dataset`](https://huggingface.co/datasets/dune123/company_dataset)
* **Entidad / Empresa:** Potato Inc.
* **Dimensiones procesadas:** 350 filas (registros) y 5 columnas útiles.
* **Cobertura temporal:** 35 trimestres consecutivos (desde `2015 Q1` hasta `2023 Q3`).
* **Variables principales:** `Company Name`, `Category`, `Sub Cat`, `Period`, `Value - Randomized`.
* **Naturaleza de datos:** Datos secundarios con valores numéricos sintéticos/aleatorizados, orientados a la caracterización descriptiva de ingresos.

---

## 📁 Estructura del Repositorio

```text
.
├── AE2/
│   ├── documento/
│   │   └── Proyecto_Integrador_EA2_PotatoInc.docx   # Documento formal del avance (Word)
│   ├── notebooks/
│   │   └── Semana_2EA2.ipynb                        # Jupyter Notebook ejecutado
│   └── resultados/
│       └── reportes/
│           └── company_dataset.txt                  # Resumen .txt generado automáticamente
├── src/
│   └── clases_po/                                   # Clases reutilizables en Python
│       ├── __init__.py
│       ├── hf_loader.py                             # Carga de datasets desde Hugging Face
│       └── reportes.py                              # Clase para generación del reporte .txt
├── README.md                                        # Documentación general del repositorio
└── requirements.txt                                 # Dependencias del proyecto
```

---

## 🛠️ Pasos de Ejecución

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/jorge-paniagua-iudigital/PI3_2026Q4_2.git
   cd tu-repositorio
   ```

2. **Crear y activar entorno virtual (recomendado):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Linux/macOS
   # .venv\Scripts\activate   # En Windows
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar el Notebook:**
   Abre y ejecuta secuencialmente las celdas de `AE2/notebooks/Semana_2EA2.ipynb`. El código descargará el dataset desde Hugging Face, mostrará la exploración básica de los datos y creará/actualizará automáticamente el archivo de resumen en `AE2/resultados/reportes/company_dataset.txt` con codificación UTF-8.