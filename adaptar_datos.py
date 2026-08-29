
with open("datos/observaciones.txt", "r", encoding="latin-1") as archivo:
    for linea in archivo:
        print(linea.strip())

# El parámetro encoding="latin-1" le indica a Python qué tabla de caracteres utilizar
# para traducir los bytes crudos del archivo de texto a letras y símbolos legibles.