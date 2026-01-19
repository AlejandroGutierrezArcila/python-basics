# Simple calculator program

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir por cero"

print("Calculadora simple")
print("Suma:", add(5, 3))
print("Resta:", subtract(5, 3))
print("Multiplicación:", multiply(5, 3))
print("División:", divide(5, 3))
