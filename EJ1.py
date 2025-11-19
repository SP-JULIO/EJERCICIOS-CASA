# Solicitar datos usuario
nombre=input("¿Cual es tu nombre?")
año_nacimiento=int(input("¿en que año naciestes"))

#Calcular la edad (año actual aproximado: 2024)
año_actual = 2024
edad = año_actual - año_nacimiento

# Verificar mayoria de edad
es_mayor = edad >=18

# Mostrar resultaos por consola
print(f"hola {nombre},tienes aproximadamente {edad} años.")

if es_mayor:
    print("Eres mayor de edad.")

else:
    print("Eres menor de edad.")
 # fin del codigo   