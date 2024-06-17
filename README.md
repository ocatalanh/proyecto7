# proyecto7

# Proyecto de Data Science: Proyecto7_DS
# Generación Z

Este proyecto es un ejemplo de flujo de trabajo en data science, incluyendo preprocesamiento de datos, entrenamiento de modelos y evaluación. El proyecto está organizado de manera modular y utiliza `Makefile` y `conda` para automatizar y asegurar la reproducibilidad.

# Objetivo
Predecir la lealtad del personal del hacia la empresa perteneciente al grupo social denominado Generación Z, distinguiendo si estaría dispuesto a trabajar por más de tres años con un empleador, lo que permitiría mayores certezas para la dirección de recursos humanos de donde invertir el capital de capacitaciones y entrenamiento a largo plazo.

## Estructura del Proyecto

```plaintext
Proyecto7_DS/
## Estructura del Proyecto

```plaintext

├── data/                           # Directorio que contiene los datos
│   ├── processed/                  # Datos procesados
│   │   ├── datos_split_procesados.pkl  # Datos procesados y divididos
│   │   └── df_eda.pkl              # Datos utilizados para el análisis exploratorio
│   └── raw/                        # Datos sin procesar
│       └── Your Career Aspirations of GenZ.csv  # Conjunto de datos crudos
├── mapa/                           # Directorio que contiene archivos de mapas
│   └── mapa_codigos_postales.html  # Mapa de códigos postales en formato HTML
├── models/                         # Directorio que contiene archivos de modelos
│   ├── escalador.pkl               # Modelo de escalado
│   ├── mejor_rf_modelo.pkl         # Mejor modelo de Random Forest
│   ├── onehot_encoder.pkl          # Modelo OneHotEncoder
│   ├── onehot_encoder_multi_var.pkl # OneHotEncoder para múltiples variables
│   └── pca.pkl                     # Modelo de Análisis de Componentes Principales (PCA)
├── scripts/                        # Directorio que contiene scripts
│   ├── one_hot_encoder.py          # Script para one-hot encoding
│   ├── pipeline.py                 # Script para la creación del pipeline de datos
│   ├── remp_valores_binarios.py    # Script para reemplazo de valores binarios
│   ├── split_and_group.py          # Script para dividir y agrupar datos
│   ├── test_post.py                # Script para pruebas de solicitudes POST
│   ├── traducir_respuestas.py      # Script para traducir respuestas
│   └── trad_columnas.py            # Script para traducir columnas
│   
├── .gitignore                      # Archivo que especifica qué archivos y directorios deben ser ignorados por Git
├── 0_EDA_Proyecto7.ipynb           # Notebook de Jupyter para el análisis exploratorio de datos
├── 1_Preprocesamiento_Proyecto7.ipynb  # Notebook de Jupyter para el preprocesamiento de datos
├── 2_Modelo_Proyecto7.ipynb        # Notebook de Jupyter para el entrenamiento y evaluación de modelos
├── 3_Emsable.ipynb                 # Notebook de Jupyter para el ensamblaje de modelos
├── app.py                          # Archivo principal de la aplicación
├── consulta.json                   # Archivo JSON para consultas
├── environment.yml                 # Configuración del entorno Conda
├── listar_archivos.py              # Script para listar archivos y directorios
├── ppt_proyecto7.pptx              # Presentación del proyecto en PowerPoint
├── README.md                       # Documentación del proyecto
├── requirements.txt                # Dependencias de Python necesarias
└── UDD_Proyecto_M7.ipynb           # Notebook del proyecto

```

# Técnica de Machine Learning
Se entrenarán diferentes modelos de machine learning supervisado para determinar cuáles de ellos no arroja un mejor score de precisión que permita determinar  la disposición a ser un trabajador más leal con la empresa.

# Origen de los Datos 
Para el entrenamiento de machine learning se utilizará el dataset Generación Z, el cual consiste en 15 columnas que contienen diferentes preguntas sobre los gustos y preferencias de la Generación Z. 

- Aspiraciones profesionales de la generación Z: https://www.kaggle.com/datasets/kulturehire/understanding-career-aspirations-of-genz

# Quienes son la Generación Z
La Generación Z es aquella nacida entre mediados de los 90 y principios de 2010, es la primera generación de nativos digitales que ha crecido con internet y smartphones. Son altamente competentes en tecnología y prefieren plataformas visuales como YouTube y TikTok. Valoran la autenticidad, la transparencia y están profundamente comprometidos con causas sociales y ambientales. Buscan flexibilidad laboral y un equilibrio entre trabajo y vida personal. Su enfoque en la diversidad y la inclusión, junto con una prudencia financiera, los distingue en el panorama global actual.

# Uso del Proyecto

### Clonar el repositorio

```sh
git clone <https://github.com/ocatalanh/proyecto7.git>
cd Proyecto7_DS
```

### Crear y activar el entorno virtual

```conda env create -f environment.yml
conda activate proyecto7_ds
```