# Programación 1 - 2026 👾

## Grupo:

```python
while True:
    dopamina.borrar()
```

>[!Note]
>**"Un bucle infinito en Python que busca vaciar tu cerebro del veneno del scroll infinito"**<br>

## Autores

- [@julietaguzman](https://github.com/julietaguzman)
- [@chazargl](https://github.com/chazargl)

```python
    Alumnos: Julieta Guzmán / Juan Matias Chazarreta
    Ingeniería en Telecomunicaciones
    Universidad Nacional de Río Negro (UNRN)
```

<p align="center">
  <img src="assets/images/images.png" alt="Logo" width="400">
</p>

## Lenguajes

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Sobre este repositorio

Acá se va a publica todo lo relacionado al progreso del trabajo práctico integrador N° 1: un flujo completo de procesamiento de datos meteorológicos del Servicio Meteorológico Nacional (SMN).

1. Conversor TXT a JSON.
2. Análisis del JSON y app web interactiva.

```
trabajo_integrador/
├── conversor/                    # Parte 1
│   ├── adaptar_datos.py
│   └── validaciones.py
├── app_web/                      # Parte 2
│   ├── procesar_datos.py
│   ├── datos.py
│   ├── estadisticas.py
│   ├── graficos.py
│   ├── entradas/
│   │   └── observaciones.json
│   └── salidas/
├── requirements.txt
└── README.md
```

Ejecución: 
2. ### Conversor TXT a JSON

```bash
cd conversor
python adaptar_datos.py observaciones.txt observaciones.json
```

2. ### Procesamiento de datos

```bash
cd app_web
python procesar_datos.py entradas/observaciones.json "AEROPARQUE AERO" temperatura
```
