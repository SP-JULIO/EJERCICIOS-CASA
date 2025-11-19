# Solicitud de entrada de datos
contraseña_1 =input("crea una nueva contraseña: ")
contraseña_2 =input("confirma tu contraseña: ")

# Combinacion directa de las condiciones
if(contraseña_1 == contraseña_2) and (len(contraseña_1)>= 8) :
    print("¡contraseña creada exitosamente!")

elif len(contraseña_1) < 8: 
    print("¡Error! La contrasela debe de tener al menos 8 caracteres.")

else:
    # Si no son iguales y la longitud es >= 8, este es el unico caso restante
    print("¡Error! Las contraseñas no coninciden")

# fin del codigo