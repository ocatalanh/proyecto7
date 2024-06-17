# Proyecto de Data Science: Proyecto7_DS
# Generación Z

Este proyecto es un ejemplo de flujo de trabajo en data science, incluyendo preprocesamiento de datos, entrenamiento de modelos y evaluación. El proyecto está organizado de manera modular y utiliza `Makefile` y `conda` para automatizar y asegurar la reproducibilidad.

# Objetivo
Predecir la lealtad del personal del hacia la empresa perteneciente al grupo social denominado Generación Z, distinguiendo si estaría dispuesto a trabajar por más de tres años con un empleador, lo que permitiría mayores certezas para la dirección de recursos humanos de donde invertir el capital de capacitaciones y entrenamiento a largo plazo.

## Estructura del Proyecto

```plaintext
Proyecto7_DS/
## Estructura del Proyecto



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

## Clonar el repositorio

```sh
git clone <https://github.com/ocatalanh/proyecto7.git>
cd Proyecto7_DS
```
## Instalar Make
Antes de empezar, asegúrate de tener instalado `make` en tu sistema. Puedes instalarlo ejecutando los siguientes comandos:


## Instalación de `make` con Chocolatey en Windows

### Instalación de Chocolatey (si aún no está instalado)

1. **Abrir PowerShell como administrador:**
   - Haz clic derecho en el ícono de PowerShell en el menú de inicio.
   - Selecciona "Ejecutar como administrador".

2. **Instalar Chocolatey:**
   - Ejecuta el siguiente comando en PowerShell como administrador:
     ```bash
     Set-ExecutionPolicy Bypass -Scope Process -Force; `
     [System.Net.ServicePointManager]::SecurityProtocol = `
     [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
     iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
     ```
   - Este comando descargará e instalará Chocolatey en tu sistema.

3. **Verificar la instalación de Chocolatey:**
   - Una vez completada la instalación, verifica que Chocolatey esté instalado correctamente ejecutando:
     ```bash
     choco --version
     ```
   - Deberías ver la versión de Chocolatey que se instaló.

### Instalación de `make` con Chocolatey

4. **Instalar `make`:**
   - Una vez que tengas Chocolatey instalado y funcionando, puedes instalar `make` ejecutando el siguiente comando en PowerShell (administrador):
     ```bash
     choco install make
     ```
   - Chocolatey buscará la última versión estable de `make` y la instalará en tu sistema.

5. **Verificar la instalación de `make`:**
   - Después de la instalación, verifica que `make` esté instalado correctamente ejecutando:
     ```bash
     make --version
     ```
   - Deberías ver la versión de `make` que se instaló.

### Uso de `make`

Una vez instalado `make` con Chocolatey, puedes usarlo para ejecutar comandos definidos en un archivo Makefile en tu proyecto. Asegúrate de tener un Makefile adecuadamente configurado con las reglas y comandos necesarios para configurar el entorno, ejecutar scripts, etc.

Por ejemplo, para ejecutar una regla `setup` definida en tu Makefile, puedes hacerlo ejecutando:
```bash
make setup
```



## Crear, activar el entono virtual y correr flask
Ejecutar en la terminal el comando make setup, este instalará el entorno del proyecto, lo activara y correra la aplicación flask para probar el modelo

```sh
make setup

```
## Enviar un request mediante post
* Ingresar a https://www.postman.com/
* Configurar para enviar una request meadiante el metodo POST
* Ingresar al Url http://127.0.0.1:5000/predice
* arbrir el archivo consulta.json, copiar y pegar alguna de las consultas en el body del request formato raw
* enviar y verificar respuesta

## Respuestas esperadas
 * Si en modelo el resultado es 0 indicara "Ningun grado de lealtad hacia la empresa"
 * Si en modelo el resultado es 1 indicara "Mediano grado de lealtad hacia la empresa"
 * Si en modelo el resultado es 2 indicara "Totalmente leal hacia la empresa"
 * Culaquier otro caso indicara "Predicción no reconocida"
