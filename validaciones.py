
# Modulo de validaciones

def encabezado_o_vacia (linea: str) -> bool:

# Parsear: Analizar una cadena de texto de una sola línea 
# para separar sus partes y extraer datos útiles

def validar_fecha (fecha_string: str) -> bool:

# Parsear: Analizar una cadena de texto de una sola línea 
# para separar sus partes y extraer datos útiles
def parsear_linea (linea: str):

    try:
        hora = int(hora_string)
        temp = float(temp_string)
        humedad = int(hum_string)
        pnm = float(pnm_string)
        dd = int(dd_string)
        ff = int(ff_string)
    except ValueError:
        return None, "Contienen caracteres invalidos o faltan datos."
    
    if hora <= 0 or hora >= 23:
        return None, f"Hora fuera de rango (0 - 23): {hora}"
    if humedad <= 0 or humedad >= 100:
        return None, f"Humedad fuera de rango (0 - 100%) {humedad}"
    if dd <= 0 or dd >= 360:
        return None, f"Direccion del viento fuera del rango (0 - 360 grados): {dd}"
    if ff < 0:
        return None, f"Velocidad del viento negativa: {ff}"
    if not estacion.strip():
        return None, "El nombre de la estacion esta vacio."

    valido = {
        "fecha": fecha_string,
        "hora": hora,
        "temperatura": temp,
        "humedad": humedad,
        "presion": pnm,
        "direccion_del_viento": dd,
        "velocidad_del_viento": ff,
        "estacion": estacion
    }

    
