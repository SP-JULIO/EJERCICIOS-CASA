# Solicitud de entrada de datos
contraseña_1 = input("Crea una nueva contraseña: ")
contraseña_2 = input("Confirma tu contraseña: ")

# Validación directa
if (contraseña_1 == contraseña_2 
    and len(contraseña_1) >= 8 
    and any(c.isupper() for c in contraseña_1) 
    and any(c.islower() for c in contraseña_1) 
    and any(c.isdigit() for c in contraseña_1) 
    and any(c in "!#$%&/?¡¿/*-+~-_" for c in contraseña_1)):
    print ("La contraseña se ha creado exitosamente")

elif len (contraseña_1) < 8 : 
    print("¡Error! La contrasela debe de tener al menos 8 caracteres.")

else:
    # Si no son iguales y la longitud es >= 8, este es el unico caso restante
    print("¡Error! Las contraseñas no cumple con los requisitos debe de tener almenos mayusculas, minusculas, numeros y caracteres")