def calcular_estadisticas(filtrados):
   
    if len(filtrados) == 0:
        return {
            "cantidad": 0,
            "minimo": None,
            "maximo": None,
            "promedio": None,
        }

    valores = []
    for fila in filtrados:
        valores.append(fila["valor"])

    cantidad = len(valores)
    minimo = min(valores)
    maximo = max(valores)
    promedio = sum(valores) / cantidad

    return {
        "cantidad": cantidad,
        "minimo": minimo,
        "maximo": maximo,
        "promedio": promedio,
    }


