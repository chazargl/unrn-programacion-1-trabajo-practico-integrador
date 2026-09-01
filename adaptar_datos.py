
import sys
import os
import json
import validaciones

def procesar_txt(ruta_txt):
    registros_validos = []
    registros_invalidos = []

    try:
        with open(ruta_txt, "r", encoding="latin-1") as archivo:
            for numero_linea, linea in enumerate(archivo, start = 1):
                if validaciones.encabezado_o_vacia(linea):
                    continue
                registro, error = validaciones.parsear_linea(linea)

                if registro is not None:
                    registros_validos.append(registro)
                else:
                    registros_invalidos.append({
                        "numero_de_linea": numero_linea,
                        "linea_original": linea,
                        "motivo_del_error": error
                    })
    except FileNotFoundError:
        print(f"No se encontro el archivo: {ruta_txt}")
        sys.exit(1)

def generar_json(registros_validos, registros_invalidos, ruta_salida):

    total = len(registros_validos) + len(registros_invalidos)
    datos_json = {
        "total_de_registros": total,
        "cantidad_registros_validos": len (registros_validos),
        "cantidad_registros_invalidos": len(registros_invalidos),
        "registros_validos": registros_validos,
        "registros_invalidos": registros_invalidos 
    }

def main():
    if len(sys.argv) != 3:
        print("Ingreso de datos: python adaptar_datos.py archivo_entrada.txt archivo_salida.json")

    ruta_entrada = sys.argv[1]
    ruta_salida = sys.argv[2]

    registros_validos, registros_invalidos = procesar_txt(ruta_entrada)
    generar_json(registros_validos, registros_invalidos, ruta_salida)

# El parámetro encoding="latin-1" le indica a Python qué tabla de caracteres utilizar
# para traducir los bytes crudos del archivo de texto a letras y símbolos legibles.