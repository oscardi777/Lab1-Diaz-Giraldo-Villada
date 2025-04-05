import random

def countletters(w, pos, l, door):
  #Inicio de la funcion de countletters
  cont = 0  # Contador de caracteres l consecutivos
  i = pos  # Posición actual en la cadena
  for lit in w[i:]:  # Se verifica la letra desde la posición i en adelante
    if lit == l:
      # Se actualiza el contador de la letra y de la posición donde se deja la lectura
      cont += 1
      i += 1
    else:
      if door:  # Si door es True, la cadena será inválida si hay una 'b' después de la segunda secuencia de 'a'
        return False, 0, 0
      return True, cont, i  # Caso contrario se retorna la cantidad de letras l y la posición donde se finaliza la lectura
  return True, cont, i
  #Fin de la funcion de countletters

def validar_cadena(w, r=None):
  #Inicio de la función para validar la cadena de acuerdo con el lenguaje
  check1a = countletters(w, 0, "a", False)  # Contar las 'a' iniciales
  checkb = countletters(w, check1a[2], "b", False)  # Contar las 'b' después de las primeras 'a'
  check2a = countletters(w, checkb[2], "a", True)  # Contar las 'a' finales. 'door' en True para validar que no haya 'b' luego

  # Extraer valores de cada verificación
  door = check2a[0]  # Indica si la cadena sigue siendo válida
  num1a = check1a[1]  # Cantidad de 'a' iniciales
  numb = checkb[1]  # Cantidad de 'b'
  num2a = check2a[1]  # Cantidad de 'a' finales

  # Valores de la posición donde terminan la secuencia de la primera 'a' y de las 'b'
  n = check1a[2]
  m = checkb[2]

  long_w = num1a + numb + num2a  # Contador del tamaño de la cadena caracter a caracter

  if door:
    mod = (num1a + numb - num2a) % 3  # Validación de múltiplo de 3 según las reglas del lenguaje
    if mod == 0 and (r is None or long_w >= r):  # Solo se verifica longitud si r fue proporcionado (modo=True)
      return True, w, n, m  # Cadena válida
  return False, "", 0, 0  # Cadena inválida
  #Fin de la función para validar la cadena

def transs(modo, cadena):
  #Inicio de la funcion general de transición del lenguaje
  if modo:
    r = random.randint(8, 30)  # Se genera un número aleatorio entre 8 y 30 como longitud mínima requerida
    while True:
      # Se le pedirá al usuario ingresar una cadena válida
      w = input(f"Ingrese una cadena de caracteres válida y de largo mayor o igual a {r}: ")
      valido, w_valida, n, m = validar_cadena(w, r)  # Validar la cadena ingresada
      if valido:
        return True, w_valida, n, m  # Retorna que la cadena es válida
      print("La cadena no es válida. Por favor vuelva a intentarlo.")  # Se informa al usuario y se repite
  else:
    # Si el modo es False, simplemente se valida la cadena dada sin pedir al usuario
    return validar_cadena(cadena)
  #Fin de la funcion general de transición del lenguaje
