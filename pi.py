# 1
name = input("¿Cómo te llamas?: ")
print(f"Hola {name} quede lol con tu nombre")
#2
name1 = input("¿Cómo te llamas?: ")
edad= int(input("¿Cuántos años tienes?: "))
edadlol = edad + 1
print(f"Hola {name1} El próximo año tendrás {edadlol} años.")
#3
name2 =input("¿Cómo te llamas?: ")
ape= input("¿y cual es tu apellido ?: ")
estu= input("¿Que carrera estudias we? ")
print(f"{name2} {ape} estudia la carrera  {estu}")
#4
pal = input("escribe una palabra: ")
pa1l = pal[1]
pal2 = pal[-1]
print (f"Las primera y ultima letra de tu palabra son {pa1l} y {pal2} ")
#5
edad1= int(input("¿Cuántos años tienes?: "))
meses = edad1 * 12
print(f"tu edad en meses son:  {meses} loool" \
"")
#6
name3 = input("Ingresa tu apodo xd: ")
pi = 3,1416
print(f"hola {name3} el valor de pi es {pi} ")
#7
frase = input("hola pone una frase: ")
print(frase * 3)
#8
name3=input("tu nombre?")
edad2= int(input("Tu edad?: "))
carre= input("que estudias?: ")
hobby= input("cual es tu hobby?: ")
ficha = f"""
Ficha Personal:
---------------
Nombre: {name3}
Edad: {edad2} años
Carrera: {carre}
Hobby: {hobby}
"""
print(ficha)
#9
oracion = input("Introduce una oración: ")
oracion_limpia = oracion.strip()
oracion_mayusculas = oracion_limpia.upper()
oracion_modificada = oracion_mayusculas.replace("A", "@")
print("Oración modificada:", oracion_modificada)
#10
cadena = "Estudiante: Ana Pérez - Edad: 21 - Carrera: Diseño"
partes = cadena.split(" - ")
nom = partes[0].split(": ")[1]
edad = partes[1].split(": ")[1]
carr= partes[2].split(": ")[1]
print(f"Nombre: {nom}, Edad: {edad}, Carrera: {carr}")
#11
nom = input("Por favor, ingresa tu nombre: ")
prime = nom[0].lower()
longi = len(nom)
identificador = f"usuario{prime}{longi}@duoc.cl"
print(f"\nBienvenido/a a Duoc UC, {nom}.")
print(f"Tu identificador es: {identificador}")

#12 
usuario_correcto = "usuarioa4@duoc.cl"
contrasena_correcta = "1234"
usuario_ingresado = input("Introduce tu usuario: ")
contrasena_ingresada = input("Introduce tu contraseña: ")

if usuario_ingresado == usuario_correcto and contrasena_ingresada == contrasena_correcta:
    print("Acceso correcto")
else:
    print("Usuario o contraseña incorrectos.")

#13

def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")  
    return palabra == palabra[::-1]
palabra = input("Introduce una palabra: ")
if es_palindromo(palabra):
    print(f"La palabra '{palabra}' es un palíndromo")
else:
    print(f"La palabra '{palabra}' no es un palíndromo.")
#14
nom1 = input("Ingresa el primer nombre: ")
nom2 = input("Ingresa el segundo nombre: ")
nom3 = input("Ingresa el tercer nombre: ")
print(f"¡Hola {nom1} eres un grande")
print(f"¡Hola {nom2} eres un crack")
print(f"¡Hola {nom3} k buen nombre")
#15
nombre = input("Ingresa tu nombre: ")
voca = "aeiouAEIOU"
contador = 0
for letra in nombre:
    if letra in voca:
        contador += 1
print(f"Tu nombre tiene {contador} vocales.")
#16
frase = input("Ingresa una frase: ")
caracteres = len(frase)
palabras = len(frase.split())
print(f"La cantidad de caracteres en la frase es: {caracteres}")
print(f"La cantidad de palabras en la frase es: {palabras}")
