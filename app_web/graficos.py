import os
from datetime import datetime
import matplotlib.pyplot as plt

def generar_slug(texto):
    return texto.lower().replace(" ", "_")

def generar_grafica(filtrados, estacion, medicion, carpeta_salidas = "salidas"):
    if not os.path.exists(carpeta_salidas):
        os.makedirs(carpeta_salidas)

    hoy = datetime.now().strftime("%Y-%m-%d")
    slug = generar_slug(estacion)
    nombre_archivo = f"{hoy}_{slug}_{medicion}.png"
    ruta_png = os.path.join(carpeta_salidas, nombre_archivo)

    x = []
    y = []
    for fila in filtrados:
        x.append(fila["fecha_hora"])
        y.append(fila["valor"])

    plt.plot(x, y)
    plt.title(f"{medicion} — {estacion}")
    plt.xlabel("Fecha y hora")
    plt.ylabel(medicion)
    plt.savefig(ruta_png)
    plt.show()
 
    return ruta_png