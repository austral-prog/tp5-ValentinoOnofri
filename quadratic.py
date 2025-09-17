# Replace the "ANSWER HERE" for your answer
# a = float(input("Ingrese el valor del coeficiente A: "))
# b = float(input("Ingrese el valor del coeficiente B: "))
# c = float(input("Ingrese el valor del coeficiente C: "))
# x = float(input("Ingrese el valor de la incognita X: "))

def roots(a, b, c):
    discriminante = (b**2 - 4*a*c)
    if discriminante > 0:
        r1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
        r2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
        raices = f"({r1}, {r2})"
    elif discriminante == 0:
        r1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
        r2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
        raices = f"({r1})"
    else:
        raices = "( )"
    return raices
    
def value_y(a, b, c, x):
    valor_y = a * (x **2) + b * x + c
    return valor_y

def to_string(a, b, c):
    result = " "
    if a != 0: 
        result = f"f(x) = {a} * X^2"
    if b != 0:
        if result == " ":
            result = f"f(x) = {b} * X"
        else:
            result = result + f" + {b} * X"
    if c != 0:
        if result == " ":
            result = f"f(x) = {c}"
        else:
            result = result + f" + {c}"
    return result

def derivation(a, b, c):
    derivada_cuadrado = 2 * a
    derivada_termino_lineal = b
    result = ""
    if a != 0:
        result = f"f'(x) = {derivada_cuadrado} * X"
    if b != 0:
        if result == "":
            result = f"f'(x) = {derivada_termino_lineal}"
        else:
            result = result + f" + {derivada_termino_lineal}"
    if a == 0 and b == 0:
        result = f"f'(x) = 0"
    return result
