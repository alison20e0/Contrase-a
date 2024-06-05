import random

caract = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input("Por favor ingrese la longitud de la contraseña: "))

# Variable para almacenar la contraseña generada
contraseña_generada = ""

for i in range(longitud):
    contraseña_generada += random.choice(caract)

# Contraseña resultante
print("La contraseña generada es:", contraseña_generada)