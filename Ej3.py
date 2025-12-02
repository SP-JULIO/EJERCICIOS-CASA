# Solicitud de entrada de datos
contraseña_1 = input("Crea una nueva contraseña: ")
contraseña_2 = input("Confirma tu contraseña: ")

# Función para validar reglas de la contraseña
def validar_contrasena(contrasena):
    if len(contrasena) < 8:
        return "¡Error! La contraseña debe tener al menos 8 caracteres."
    if not any(r"[A-Z]", contrasena):
        return "¡Error! La contraseña debe contener al menos una letra mayúscula."
    if not any(r"[a-z]", contrasena):
        return "¡Error! La contraseña debe contener al menos una letra minúscula."
    if not any(r"[0-9]", contrasena):
        return "¡Error! La contraseña debe contener al menos un número."
    if not any(r"[!@#$%^&*(),.?\":{}|<>]", contrasena):
        return "¡Error! La contraseña debe contener al menos un carácter especial."
    return "OK"

# fin del del codigo

