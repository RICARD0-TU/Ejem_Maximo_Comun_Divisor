class CalculadoraMCD:
    def __init__(self, a, b):
        """
        Inicializa la calculadora con dos números enteros positivos.

        Args:
        a (int): El primer número entero positivo.
        b (int): El segundo número entero positivo.
        """
        self._a = a
        self._b = b

    def gcd(self):
        """
        Calcula el Máximo Común Divisor (MCD) de los dos números utilizando el algoritmo de Euclides.

        Returns:
        int: El MCD de los dos números.
        """
        a, b = self._a, self._b
        while b != 0:
            a, b = b, a % b
        return a

    # Getter y Setter para 'a'
    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if value <= 0:
            raise ValueError("El valor de a debe ser un número entero positivo.")
        self._a = value

    # Getter y Setter para 'b'
    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if value <= 0:
            raise ValueError("El valor de b debe ser un número entero positivo.")
        self._b = value


# Función para validar si el número ingresado es positivo
def validar_numero(num):
    try:
        num = int(num)
        if num <= 0:
            print("Por favor, ingrese un número entero positivo.")
            return False, None
        return True, num
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
        return False, None


def solicitar_numero(mensaje):
    """
    Solicita entrada de usuario para un número entero positivo.

    Args:
    mensaje (str): El mensaje que se muestra al solicitar la entrada.

    Returns:
    int: El número entero positivo ingresado por el usuario.
    """
    while True:
        num = input(mensaje)
        valido, num = validar_numero(num)
        if valido:
            return num

# Solicitar entrada de usuario para el primer número
num1 = solicitar_numero("Ingrese el primer número entero positivo: ")

# Solicitar entrada de usuario para el segundo número
num2 = solicitar_numero("Ingrese el segundo número entero positivo: ")

# Crear la instancia de la clase CalculadoraMCD
calculadora = CalculadoraMCD(int(num1), int(num2))

# Calcular y mostrar el MCD
print("El Máximo Común Divisor de", calculadora.a, "y", calculadora.b, "es:", calculadora.gcd())
