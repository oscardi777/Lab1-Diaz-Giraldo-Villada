from transFunction import transs

def userGame():
#Inicio de la funcion de userGame

  answer, cadena, n = transs(True, "")  # Obtiene la validación de la cadena
  if answer:
    u = cadena[:n-1]
    v = cadena[n-1:n+1]
    x = cadena[n+1:]

    #Se muestra al usuario la seleccion arbitriara de los u, v y x

    print("La cadena se ha validado correctamente")
    print("Se hará una partición de la siguiente manera")
    print(f"Se escogerá u = {u} ; v = {v} ; x = {x}")

  #Se llama la funcion iterations para que el usuario escoja su i correspondiente
  iterations(u, v, x)

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
  answer, cadena, n = transs(modo=False, cadena=w_i)

  #Se decide el ganador del juego:
  if(answer):
    print("La cadena es aceptada por el lenguaje")
    print("Has ganado")
  else:
    print("La cadena no es aceptada por el lenguaje")
    print("Ha ganado la maquina")

#Fin de la funcion de iterations


