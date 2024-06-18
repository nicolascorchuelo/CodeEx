# Code exercise MELI

Creación de pipeline en python para la disponiblización de un DataFramse resultante.

## Explicación del proceso

Se crea un proyecto un pensamemiento de OOP, para mejor modificación y escalabilidad.

* `common.py:` Archivo que carga la configuración .yaml del proyecto.
* `config.yaml:` Archivo de configuración, se encuentra los parámetros
* `EDA.ipynb:` Anáisis exploratorio de los dataset.
* `funtions.py:` Archivo que contiene todas las funciones del modelo.
* `main.py:` Achivo principal de ejecución, contiene todo el procesos del desarrollo.
* `read_source.py:` Archivo, calse de lectura de las fuentes (.json,csv).
* `requirements.txt:` Toddas las dependecias del proyecto.
* `.gitignore:` Directorio de capertas que no se suben al repo.


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

El proceso da como resultado un dataframe que contiene la información necesaria para su análsis y responde las preguntas planteadas en el CodeEx, cada coluna respende cada uno de los puntos.

● prints de la última semana 
  ● por cada print: 
    ○ un campo que indique si se hizo click o no 
    ○ cantidad de veces que el usuario vio cada value prop en las 3 semanas previas a ese print. 
    ○ cantidad de veces que el usuario clickeo cada value prop en las 3 semanas previas a ese print.
    ○ cantidad de pagos que el usuario realizó para cada value prop en las 3 semanas previas a ese print.
    ○ importes acumulados que el usuario gasto para cada value prop en las 3 semanas previas a ese print.


![image](https://github.com/nicolascorchuelo/CodeEx/assets/90802118/efd72a4c-f4af-4d53-95b2-eb0929d5f754)


## Bonus y oportunidad de mejora

* Agregar excepciones al código (buena práctica), controlar el error.
* Agregar procesos de pruebas automatizados con librerías espeicales (pruebas automáticas).
* Se puede implementar monitoréo a la ejecución (escricura de logs).
* Mediante herramientas de CI/CD como github actions, se puede automatizar el despligue.
* Se puede optar por manejar contenedores la solución o servicios serverless
* Se puede tener un mejor análisis de resultado postrando de forma más diciente los insights de la información.
