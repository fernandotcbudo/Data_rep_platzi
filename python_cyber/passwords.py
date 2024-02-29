import string
import random 

length=  int(input("Ingresa el tamaño de la contraseña: "))

characters= string.ascii_letters + string.digits + string.punctuation

password= "".join(random.choice(characters) for i in range(length))

print(f'La contraseña guardada es {password}')