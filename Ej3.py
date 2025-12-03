#Solicitud de datos
contraseña_1 =input("Solicitud crear contraseña". )
contraseña_2 =input("confirmar contraseña". )

# Verificacion de datos
if (contraseña_1 == contraseña_2
   and len(contraseña_1) >=8
   and any(c.isupper() for c in contraseña_1)
   and any(c.islower() for c in contraseña_1)
   and any(c.isdigit() for c in contraseña_1)
   and any(c.in"!#$%&/?¡¿÷×-+~_" for c in contraseña_1)
   print(" La contraseña se ha creado exitosamente")

elif len(contraseña_1) < 8 :
    print("!Error¡ La contraseña debe de tener al menos 8 caracteres")

else
   # si no son iguales y la longitud es >=8, este es el unico caso restante
   print("!Error¡ Las contraseñas no cumplen con los requisitos deben de tener al menos mayusculas, minusculas, numeros y caracteres")

# fin del codigo
