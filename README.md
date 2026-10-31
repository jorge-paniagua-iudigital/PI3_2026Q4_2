# Caracterización, Transformación y Análisis de Ingresos de Potato Inc. (2015 Q1 – 2023 Q3)

Este repositorio contiene el desarrollo del **Proyecto Integrador de Analítica de Datos** para la empresa **Potato Inc.**, abarcando la **Primera Etapa (AE2)** y la **Segunda Etapa (AE3 - Transformación y Enriquecimiento de Datos)**.

---

## 📌 Preguntas de Negocio Abordadas (AE3)
1. **¿Cuáles son las subcategorías con mayor aporte financiero acumulado y promedio dentro de las dimensiones de Producto y Región?**
   * *Hallazgo:* `Smartphones` lidera en Producto con $7,198.22 MM (52.31% de participación promedio) y `Americas` lidera en Región con $6,379.47 MM (43.24% de participación promedio).
2. **¿Cómo han evolucionado los ingresos consolidados año tras año entre regiones y productos durante el periodo 2015 – 2023?**
   * *Hallazgo:* Los ingresos alcanzaron su máximo histórico en el año 2022 con $4,789.48 MM consolidados.

---

## 🛠️ Transformaciones y Enriquecimiento Realizados
* **Normalización de Tipos:** Conversión de la columna monetaria a `float64` e impartición de formato en Miles de Millones (Billions / MM).
* **Nuevas Variables Calculadas:**
  * `Año` (`int`): Año extraído de la variable `Period`.
  * `Trimestre` (`str`): Trimestre (`Q1`, `Q2`, `Q3`, `Q4`) extraído de `Period`.
  * `Valor_Miles_Millones` (`float`): Ingreso dividido entre $10^9$.
  * `Participacion_Categoria_Pct` (`float`): Porcentaje de contribución de cada subcategoría dentro de su categoría en cada trimestre.

---

## 📁 Estructura Actualizada del Repositorio

```text
.
├── .github/
│   └── workflows/
│       └── run_notebook.yml                         # Workflow de ejecución automática en GitHub Actions
├── datos/
│   ├── company_dataset.csv                          # Dataset crudo descargado de Hugging Face
│   └── company_dataset_preparado.csv                # Dataset preparado y enriquecido (9 variables)
├── reportes/
│   ├── company_dataset_summary_ae3.txt              # Resumen descriptivo .txt generado automáticamente
│   ├── tabla_desempeno_subcategorias.csv            # Tabla de resultados por Subcategoría
│   └── tabla_evolucion_anual.csv                    # Tabla de evolución anual de ingresos
├── src/
│   └── sincronicas/
│       └── Semana_2EA2.ipynb                        # Jupyter Notebook ejecutado
├── Proyecto_Integrador_AE3_PotatoInc.docx           # Documento formal del avance (Word)
├── README.md                                        # Documentación general del repositorio
└── requirements.txt                                 # Dependencias del proyecto