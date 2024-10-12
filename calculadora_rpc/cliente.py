import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:9000/")

print("Elige una operación a realizar:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Ingresa la opción deseada (1-4): ")

num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))

if choice == "1":
    result = proxy.add(num1, num2)
    print(f"El resultado de {num1} + {num2} es: {result}")
elif choice == "2":
    result = proxy.subtract(num1, num2)
    print(f"El resultado de {num1} - {num2} es: {result}")
elif choice == "3":
    result = proxy.multiply(num1, num2)
    print(f"El resultado de {num1} * {num2} es: {result}")
elif choice == "4":
    result = proxy.divide(num1, num2)
    print(f"El resultado de {num1} / {num2} es: {result}")
else:
    print("Opción inválida")