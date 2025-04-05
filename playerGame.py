from transFunction import transs
import random as r


def userGame():
#Inicio de la funcion de userGame

  answer, cadena, n, m = transs(True, "")  # Obtiene la validación de la cadena
  if answer:

    if m-n>1 : # Caso importante una sola b en la cadena
      stop = r.randint(n, m)
    else:
      stop = m

    # La cadena v puede parar hasta la ultima b y podra ser utilizada

    u = cadena[:n-1]
    v = cadena[n-1:stop]
    x = cadena[stop:]

    #Se muestra al usuario la seleccion arbitriara de los u, v y x

    print("La cadena se ha validado correctamente")
    print("Se hará una partición de la siguiente manera")
    print(f"Se escogerá u = {u} ; v = {v} ; x = {x}")

  #Se llama la funcion iterations para que el usuario escoja su i correspondiente
  winner = iterations(u, v, x)

  if winner:
    print("La cadena es valida, el jugador ha ganado")
  else:
    print("La cadena no es valida, el jugador ha perdido")

#Fin de la funcion de userGame

def iterations(u, v, x):
#Inicio de la funcion de iterations

  print("Escoja un numero i para repetir i-veces la cadena v tal que pertenezca a L")
  
  #Se solicita al usuario un i valido hasta que lo proporcione
  while True:
      i = int(input("i = "))  #Convierte la entrada a entero
      if i>=0: #Se verifica su no negatividad
        print(f"El número ingresado es: {i}")
        break
      else:
        print("Vuelva a interntarlo Debe ingresar un número entero posotivo.")
        continue

  #Se actualiza el v (a partir del i suministrado) y se actualiza la cadena a w_i
  v_i = v*i
  w_i = u+v_i+x
  print(f"Su nueva cadena v´ = {v_i} ")
  print(f"Luego su cadena w´ = {w_i} ")
  print("Ahora revisemos si es aceptada por el Lenguaje")

  #Se verifica la aceptacion de esta nueva cadena a partir del modo False de la función transs
  answer = transs(modo=False, cadena=w_i)[0]

  #Se returna la validez de la nueva cadena:
  return answer

#Fin de la funcion de iterations


