# proyecto7

# Proyecto de Data Science: Proyecto7_DS

Este proyecto es un ejemplo de flujo de trabajo en data science, incluyendo preprocesamiento de datos, entrenamiento de modelos y evaluación. El proyecto está organizado de manera modular y utiliza `Makefile` y `conda` para automatizar y asegurar la reproducibilidad.

## Estructura del Proyecto

```plaintext
project/
│
├── data/
│   ├── raw/                   # Datos originales sin procesar
│   ├── processed/             # Datos preprocesados listos para el modelo
│
├── scripts/
│   ├── 01_preprocess_data.py  # Script de preprocesamiento de datos
│   ├── 02_train_model.py      # Script de entrenamiento del modelo
│   ├── 03_evaluate_model.py   # Script de evaluación del modelo
│
├── models/
│   └── best_model.pkl         # Modelo entrenado y guardado
│
├── environment.yml            # Configuración del entorno conda
├── Makefile                   # Archivo Make para automatización de tareas
└── README.md                  # Documentación del proyecto
```


## Uso del Proyecto

### Clonar el repositorio

```sh
git clone <URL_del_repositorio>
cd Proyecto7_DS
```

### Crear y activar el entorno virtual

```conda env create -f environment.yml
conda activate proyecto7_ds
```