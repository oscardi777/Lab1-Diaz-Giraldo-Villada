import random

def countletters(string, pos, l, door):
#Inicio de la funcion de countletters
  cont = 0  # Contador de caracteres l consecutivos
  i = pos  # Posición actual en la cadena

  for lit in string[i:]: #Se verifica la letra desde la posicion i en adelante
    if lit == l:
      #Se actualiza el contador de la letra y de la posicion donde se deja la lectura
      cont += 1
      i += 1
    else:
      if door:  #Si door es True, la cadena será inválida si hay una 'b' después de la segunda secuencia de 'a'
        return False, 0, 0
      return True, cont, i #Caso contrario se retorna la cantidad de letras l y la posicion donde se finaliza la lectura
  return True, cont, i
#Fin de la funcion de countletters

def transs(modo, cadena):
#Inicio de la funcion general de transicion del lenguaje

  r = random.randint(8, 30)  #Se genera un número aleatorio entre 8 y 30 como longitud mínima requerida
  p = random.randint(0,100)  #Se genera un número aleatorio entre 0 y 100 para la funcionalidad del 90% sesgado

  while True:
    #Dependiendo del tipo de validación que se haga se le pedira o no al usuario digitarla o simplemente se procedera a validar
    if modo:
      string = input(f"Ingrese una cadena de caracteres válida y de largo mayor o igual a {r}: ")
    else:
      string = cadena

    #Realizar conteo de letras en cada sección esperada de la cadena
    check1a = countletters(string, 0, "a", False)  #Contar las 'a' iniciales
    checkb = countletters(string, check1a[2], "b", False)  #Contar las 'b' después de las primeras 'a'
    check2a = countletters(string, checkb[2], "a", True)  #Contar las 'a' finales, recordar se recibe como ultimo parametro para determinar si hay letras b´s luego de las segundas a´s

    #Extraer valores de cada verificación
    door = check2a[0]  #Indica si la cadena sigue siendo válida
    num1a = check1a[1]  #Cantidad de 'a' iniciales
    numb = checkb[1]  #Cantidad de 'b'
    num2a = check2a[1]  #Cantidad de 'a' finales

    if door:
      mod = (num1a + numb - num2a) % 3  #Validación de múltiplo de 3
      if mod == 0 and len(string) >= r:
        #A partir del numero random p, al tener su intervalo de 0-100, se tomara este resultado como un "separados" entre las probabilidades
        if p<=90:
          #El 90% de las veces se utilizara un n sesgado (a que gane la maquina)
          n = check1a[2]
          m = checkb[2]
        else:
          #El 10% de las veces se utilizara un n no sesgado (puede ganar cualquiera)
          n = check1a[2] + 1
          m = checkb[2]

        return True, string, n, m  #Retorna que la cadena es válida
      else:
        if modo:
          print("La cadena no es válida. Por favor vuelva a intentarlo.")
        else:
          #La cadena no es válida la maquina gana
          return False, "", 0, 0
    else:
      if modo:
        print("La cadena no es válida. Por favor vuelva a intentarlo.")
      else:
        #La cadena no es válida la maquina gana
        return False, "", 0, 0

#Fin de la funcion general de transicion del lenguaje

