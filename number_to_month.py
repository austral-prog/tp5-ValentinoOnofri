# Replace the "ANSWER HERE" for your answer
def number_to_month(month):
    if 1 <= month <= 12:
        if month == 1:
            resultado = "enero"
        elif month == 2:
            resultado = "febrero"
        elif month == 3:
            resultado = "marzo"
        elif month == 4:
            resultado = "abril"
        elif month == 5:
            resultado = "mayo"
        elif month == 6:
            resultado = "junio"
        elif month == 7:
            resultado = "julio"
        elif month == 8:
            resultado = "agosto"
        elif month == 9:
            resultado = "septiembre"
        elif month == 10:
            resultado = "octubre"
        elif month == 11:
            resultado = "noviembre"
        elif month == 12:
            resultado = "diciembre"
    else:
        resultado = "error"
    return resultado # Remove this line and implement