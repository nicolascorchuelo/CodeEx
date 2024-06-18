# Code exercise MELI

Creación de pipeline en python para la disponiblización de un DataFramse resultante.

## Explicación del proceso

* common.py: Archivo que carga la configuración .yaml del proyecto.
* config.yaml: Archivo de configuración, se encuentra los parámetros
* EDA.ipynb: Anáisis exploratorio de los dataset.
* funtions.py: Archivo que contiene todas las funciones del modelo.
* main.py: Achivo principal de ejecución, contiene todo el procesos del desarrollo.
* read_source.py: Archivo, calse de lectura de las fuentes (.json,csv).
* requirements.txt: Toddas las dependecias del proyecto.
* .gitignore: Directorio de capertas que no se suben al repo.


## Prerequsito

Se debe realizar por buenas prácticas la creación de un ambiente espécifico al cual lo denominé `etl_meli`, después de la creación se debe realizar la activación y la respectiva actualizacion de la librería `pip`.

```
python3 -m venv etl_meli
source etl_meli/bin/activate
python -m pip install --upgrade pip
```
Instalación de liberías necesarias para la ejecución del proceso.
```
pip install -r requirements.txt
```
Desactivar ambiente de ser necesarío.
```
deactivate
```

## Resultado
Resultado

## Bonus y oportunidad de mejora
