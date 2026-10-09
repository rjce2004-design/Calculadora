import math

# Catálogo de operaciones: la UI lo consulta para construir el menú
OPERACIONES = {
    "sumar":          {"simbolo": "+",   "nombre": "Sumar",           "unaria": False},
    "restar":         {"simbolo": "−",   "nombre": "Restar",          "unaria": False},
    "multiplicar":    {"simbolo": "×",   "nombre": "Multiplicar",     "unaria": False},
    "dividir":        {"simbolo": "÷",   "nombre": "Dividir",         "unaria": False},
    "potencia":       {"simbolo": "xʸ",  "nombre": "Potencia",        "unaria": False},
    "modulo":         {"simbolo": "mod", "nombre": "Módulo (residuo)", "unaria": False},
    "porcentaje":     {"simbolo": "%",   "nombre": "B% de A",         "unaria": False},
    "raiz_cuadrada":  {"simbolo": "√",   "nombre": "Raíz cuadrada",   "unaria": True},
    "factorial":      {"simbolo": "n!",  "nombre": "Factorial",       "unaria": True},
    "logaritmo":      {"simbolo": "log", "nombre": "Logaritmo base 10", "unaria": True},
}


def _limpiar(n):
    """Muestra 4 en lugar de 4.0 cuando el resultado es entero."""
    if isinstance(n, float) and n.is_integer() and abs(n) < 1e15:
        return int(n)
    return n


def calcular(a: float, b: float, operacion: str):
    if operacion not in OPERACIONES:
        raise ValueError("Operación no válida")

    if operacion == "sumar":
        r = a + b
    elif operacion == "restar":
        r = a - b
    elif operacion == "multiplicar":
        r = a * b
    elif operacion == "dividir":
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        r = a / b
    elif operacion == "potencia":
        r = math.pow(a, b)  # lanza ValueError si el resultado sería complejo
    elif operacion == "modulo":
        if b == 0:
            raise ValueError("No se puede calcular el módulo con cero")
        r = a % b
    elif operacion == "porcentaje":
        r = a * b / 100
    elif operacion == "raiz_cuadrada":
        if a < 0:
            raise ValueError("No existe raíz cuadrada real de un negativo")
        r = math.sqrt(a)
    elif operacion == "factorial":
        if a < 0 or not float(a).is_integer():
            raise ValueError("El factorial solo existe para enteros no negativos")
        if a > 170:
            raise ValueError("El factorial es demasiado grande (máximo 170)")
        r = math.factorial(int(a))
    elif operacion == "logaritmo":
        if a <= 0:
            raise ValueError("El logaritmo requiere un número mayor que cero")
        r = math.log10(a)

    return _limpiar(float(r) if not isinstance(r, int) else r)