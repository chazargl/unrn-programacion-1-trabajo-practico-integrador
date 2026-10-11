import sys

from datos import cargar_json, filtrar_datos
from estadisticas import calcular_estadisticas
from graficos import generar_grafica
from datos import cargar_json, filtrar_datos, guardar_csv

def main():
    ruta_json = sys.argv[1]
    estacion = sys.argv[2]
    medicion = sys.argv[3]

    try:
        datos = cargar_json(ruta_json)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error al cargar el JSON: {e}")
        sys.exit(1)

    try:
        filtrados = filtrar_datos(datos, estacion, medicion)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    if len(filtrados) == 0:
        print(f"No hay datos de '{medicion}' para '{estacion}'.")
        sys.exit(0)

    estadisticas = calcular_estadisticas(filtrados)
    ruta_grafica = generar_grafica(filtrados, estacion, medicion)
    ruta_csv = guardar_csv(filtrados, estacion, medicion)
    
    print(f"Estadisticas: {estadisticas}")
    print(f"Grafica guardada en: {ruta_grafica}")
    print(f"CSV guardado en: {ruta_csv}")
    
    print("Uso: python procesar_datos.py <ruta_json> <estacion> <medicion>")
    #Estacion AEROPARQUE AERO
    #Medicion: temperatura, humedad, presion, viento

main()