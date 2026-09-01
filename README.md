# Programación 1 - 2026 👾

## Grupo":"

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

Acá se va a publica todo lo relacionado al progreso del trabajo práctico integrador N° 1

- Documentación de estructura JSON de salida.

```python
{
    "fecha": "ddmmaaaa",
    "hora": 0,
    "temp": 10.0,
    "humedad": 0,
    "pnm": 1019.7,
    "dd": 360,
    "ff": 1,
    "estacion": "nombre"
}
```

- Implementación inicial del parseo del TXT recibido por argumento de línea de comandos.
  - Verificar existencia del archivo TXT
  - Ignorar encabezados
  - Ignorar lineas vacias
  - Completar registros vacios con None
  - Convertir valores de texto a entero o flotante segun la estructura JSON
- Implementación inicial del módulo de validaciones.
  - La fecha es mandatoria, debe tener formato indicado en la estructura de JSON y debe ser valida.
  - El campo hora debe ser entero y estar comprendido entre 0 y 23.
  - El campo de temperatura debe ser flotante.
  - La humedad debe estar comprendida entre 0 y 100.
  - La direccion del viento sera valida entre 0 y 360.
  - La velocidad del viento sera un numero positivo.
  - El campo nombre de estacion es mandatorio y no puede estar vacio.
