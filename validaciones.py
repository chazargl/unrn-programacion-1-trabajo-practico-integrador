
# Modulo de validaciones

palabras_encabezado = ["FECHA", "HORA", "TEMP", "HUM", "PNM", "DD", "FF", "NOMBRE"]

def encabezado_o_vacia (linea):
    if not linea or not linea.strip():
        return True
    
    linea_mayusculas = linea.upper()
    for palabra in palabras_encabezado:
        if palabra in linea_mayusculas:
            return True

    return False

def validar_fecha (fecha_string):
    if len(fecha_string) != 8:
        return False, f"La fecha debe tener 8 digitos (DDMMAAAA): {fecha_string}"

    if not fecha_string.isdigit():
        return False, f"La fecha solo debe contener numeros: {fecha_string}"

    try:
        dia = int(fecha_string[0:2]) # [inicio, fin] abarca los dos primeros digitos
        mes = int(fecha_string[2:4])
        año = int(fecha_string[4:8])
    except ValueError:
        return False, f"Error al procesar la fecha:{fecha_string}"

# Parsear: Analizar una cadena de texto de una sola línea 
# para separar sus partes y extraer datos útiles
def parsear_linea (linea):
    linea_limpia = linea.strip()
    if not linea_limpia:
        return None, "Linea vacia"

    partes = linea_limpia.split() # Separa la lineas con espacios

    if len(partes) < 8:
        return None, "Faltan campos"

    try:
        fecha_string = partes[0]
        hora_string = partes[1]
        temp_string = partes[2]
        hum_string = partes[3]
        pnm_string = partes[4]
        dd_string = partes[5]
        ff_string = partes[6]
        estacion = " ".join(partes[7:]) # Toma los elementos del indice 7 hasta el final
        # " ".join(...): Une todos los elementos de esa sublista en un 
        # único texto (string),insertando un espacio en blanco entre cada palabra.
    except ValueError:
        return None, "Contienen caracteres invalidos o faltan datos"

    fecha_valida, error_fecha = validar_fecha(fecha_string)
    if not fecha_valida:
        return None, f"Error en fecha: {error_fecha}"

    try:
        hora = int(hora_string)
        temp = float(temp_string)
        hum = int(hum_string)
        pnm = float(pnm_string)
        dd = int(dd_string)
        ff = float(ff_string)

        if hora <= 0 or hora >= 23:
            return None, f"Hora fuera de rango (0 - 23): {hora}"
        if hum <= 0 or hum >= 100:
            return None, f"Humedad fuera de rango (0 - 100%) {hum}"
        if dd <= 0 or dd >= 360:
            return None, f"Direccion del viento fuera del rango (0 - 360 grados): {dd}"
        if ff < 0:
            return None, f"Velocidad del viento negativa: {ff}"
        if not estacion.strip():
            return None, "El nombre de la estacion esta vacion"
    except ValueError:
        return None, "Contiene caracteres invalidos o faltan datos"

    registro = {
        "fecha": fecha_string,
        "hora": hora,
        "temperatura": temp,
        "humedad": hum,
        "presion": pnm,
        "direccion_del_viento": dd,
        "velocidad_del_viento": ff,
        "estacion": estacion
    }

    return registro, None



    
