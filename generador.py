import random
from werkzeug.security import generate_password_hash
from src import bienvenida

letras = 'abcdefghijklmnopqrstuvwxyz'
letrasMayusc = letras.upper()
numeros = '0123456789'
numerosDos = numeros
caracteres = '-!"#$()=?¡'
caractersDos = '*^\¿_.-:¨~'
caracteresTres = '><&/%;,|°'

datos = letras + numeros + numerosDos + letrasMayusc + caracteres + caractersDos + caracteresTres

print(bienvenida.mensajeInicial())
longitud = int(input("⤇ ingrese longitud de la contraseña: "))
contrasena = ''.join(random.sample(datos, longitud)) 
print(f"Su contraseña generada es:\n{contrasena}")
contrasenaHasheada = generate_password_hash(contrasena, 'sha256', 30)
print(f"Su contraseña hasheada es:\n{contrasenaHasheada}")
