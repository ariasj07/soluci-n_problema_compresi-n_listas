# Solución:
usuarios = [f"usuario{i}" for i in range(30)]

correos = [f"correo{i}@correo.com" for i in range(30)]

dicc = {
    f"CORREO_{usuarios[i].upper()}": correos[29 - i]
    for i in range(30)
}

"""
¿Que está pasando?"""
- Se crean las listas, con el formato que se solicitó.
Luego se está creando el diccionario, como clave se pone el usuario en la posición "i", la cual en la primera
iteracíon es 0, es decir usarios[i] = usuario[0] = "usuario0". Además con ayuda de los f strings, se añade
"CORREO_" adelante de cada clave

El valor asignado a las claves, es correos[29 - i]. "i" en la primer iteración, como mencioné, es 0, entonces, 29 - 0 = 29. Es decir, el ítem en la posición 30 que se encuentra
en el índice 29

En la segunda iteracíon, se repite todo, con respecto a correos[29 - i], ya en esta iteración "i" es 1, es decir 29 - 1 = 28. Lo que vendría siendo el correo en la posición 29, índice 28
Con eso se logra la solución al problema
"""
