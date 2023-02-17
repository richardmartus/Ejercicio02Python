# Se requiere un programa en Java para calcular el resultado de la suma, diferencia, producto,
#  módulo y cociente de dos números decimales de cualquier longitud.

# print(f'{real:.2f}')
class calculadora:
    def __init__(self, num1, num2):
        self.num1 = float(num1)
        self.num2 = float(num2)

    def sumar(self):
        suma = self.num1 + self.num2
        print("el resultado de la suma es: ", (f'{suma:.2f}'))

    def restar(self):
        resta = self.num1 - self.num2
        print("el resultado de la resta es: ", (f'{resta:.2f}'))

    def multiplicar(self):
        multiplicacion = self.num1 * self.num2
        print("el resultado de la multiplicación es: ", (f'{multiplicacion:.2f}'))

    def dividir(self):
        division = self.num1 / self.num2
        print("el resultado de la división es: ", (f'{division:.2f}'))

    def modulo(self):
        mod = self.num1 % self.num2
        print("el resultado del módulo es: ", (f'{mod:.2f}'))


num1 = input("ingrese un numero: ")
num2 = input("ingrese un numero: ")

calculadora = calculadora(num1, num2)
calculadora.sumar()
calculadora.restar()
calculadora.multiplicar()
calculadora.dividir()
calculadora.modulo()