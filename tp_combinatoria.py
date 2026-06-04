# math se importa para usar log10, que permite calcular la cantidad de dígitos del resultado sin convertirlo a texto.
import math

print("Bienvenidos al TP de Combinatoria - Caso 6")
print("Alumnos Paulo Orsini y Luis Troche")
print("Comisión 9 - Año 2026")
print()
print("Este programa calcula la cantidad de claves posibles de longitud n")
print("usando m símbolos disponibles, con repetición permitida y orden importante.")
print("Tipo de conteo: Variación con Repetición → Fórmula: VR(m, n) = m^n")
print()

def resolver(m, n):
    # Validamos primero el tipo de dato para evitar calcular con valores no enteros.
    if not isinstance(m, int) or not isinstance(n, int):
        raise TypeError("Los valores de m y n deben ser números naturales (enteros positivos)")
    # m representa la cantidad de símbolos disponibles; debe ser al menos 1.
    if m < 1:
        raise ValueError("El valor de m debe ser un número natural (entero positivo)")
    # n representa la longitud de la clave; también debe ser un natural positivo.
    if n < 1:
        raise ValueError("El valor de n debe ser un número natural (entero positivo)")
    # Como el orden importa y se permite repetir símbolos, aplicamos VR(m, n) = m^n.
    return m ** n


def input_validado(mensaje, minimo, mensaje_error):
    # Solicita un entero con validación de tipo y rango, permitiendo reintentos
    # El ciclo while True mantiene el pedido activo hasta que el usuario ingrese un valor válido.
    while True:
        try:
            # input muestra el mensaje recibido por parámetro y captura lo que escribe el usuario.
            # int convierte ese texto a número entero para poder validarlo y usarlo en el cálculo.
            valor = int(input(mensaje))
            if valor < minimo:
                # Si el número no cumple el mínimo, se informa el error y el ciclo vuelve a empezar.
                print(f"Error: {mensaje_error}")
            else:
                # Cuando el valor es entero y cumple el mínimo, se devuelve y termina la función.
                return valor
        except ValueError:
            # Si la conversión a entero falla, se informa el error y se vuelve a pedir el dato.
            print("Error: Por favor, ingrese un número válido")


# Primer input: pide m, que es la cantidad de símbolos disponibles para formar claves.
m = input_validado(
    "Ingrese el valor de m (cantidad de símbolos disponibles): ",
    minimo=1,
    mensaje_error="El valor de m debe ser un número natural (entero positivo)"
)
# Segundo input: pide n, que es la longitud que tendrá cada clave.
n = input_validado(
    "Ingrese el valor de n (longitud de la clave): ",
    minimo=1,
    mensaje_error="El valor de n debe ser un número natural (entero positivo)"
)

resultado = resolver(m, n)
print()
# Calculamos la cantidad de dígitos del resultado usando logaritmo en base 10 antes de intentar mostrarlo.
# Esto evita un error de Python que ocurre al convertir a texto enteros con más de 4300 dígitos.
digitos = int(n * math.log10(m)) + 1
if digitos > 4300:
    # Si el resultado es demasiado grande, se muestra en notación aproximada en lugar del número completo.
    print(f"La cantidad de claves posibles es: aproximadamente 10^{digitos} (resultado demasiado grande para mostrar completo)")
else:
    # Si el resultado está dentro del límite, se muestra el número exacto completo.
    print(f"La cantidad de claves posibles es: {resultado}")
print("Este programa resuelve una combinatoria de variación con repetición cuya fórmula es: VR(m, n) = m^n")
