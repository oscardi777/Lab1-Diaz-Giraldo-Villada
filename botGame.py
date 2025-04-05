import random
from transFunction import transs

def replicaGame(machine_winners, sesgo):
  #Inicio de la funcion replicaGame
  print("Estas en la función de Replica VS máquina")

  l = random.randint(8, 30) # Longitud de la cadena

  while True:
    while True:  # Se genera el numero de a´s y b´s aleatorio
      k = random.randint(1,30) 
      s = random.randint(1,30) 
      n = random.randint(1,30) 
      if (k + s) % 3 == n % 3:  # Se verifica la condición de congruencia
        break
      else:
        continue
    if (k+s+n)>=l:    # Se verifica que la cadena si cumpla con la longitud y se genera la cadena
      cadena = "a"*k + "b"*s + "a"*n
      break
    else: 
      continue
    
  # Se imprime la cadena aleatoria y se valida por la funcion de transicion
  print("La cadena aleatoria es: " + cadena)
  answer, x, a, b = transs(False, cadena) # Se verifica la cadena

  if answer:    # Se hace la partición y se genera un i aleatorio para realizar el bombeo
    #Se llama la funcion iterations para que el usuario escoja su i correspondiente
    winner = splitBot(cadena, a, b, sesgo)

    if winner:
      print("La nueva cadena es valida, la replica ha ganado")
      return machine_winners
    else:
      print("La nueva cadena no es valida, la replica ha perdido")
      return machine_winners + 1
    
  #Fin de la funcion replicaGame

def splitBot(cadena, n, m, sesgo):
  #Inicio de la funcion de iterations_bot

  if m-n==1 : # Caso importante una sola b en la cadena
    stop = m
  elif n==m:
    n = int(n/2)
    stop = random.randint(n+1, m)
  else:
    stop = random.randint(n+1, m)

  if sesgo:
    n += 1

  # La cadena v puede parar hasta la ultima b y podra ser utilizada
  u = cadena[:n-1]
  v = cadena[n-1:stop]
  x = cadena[stop:]

  #Se muestra al usuario la seleccion arbitriara de los u, v y x
  print("La cadena se ha validado correctamente")
  print("Se hará una partición de la siguiente manera")
  print(f"Se escogerá u = {u} ; v = {v} ; x = {x}")

  #Se llama la funcion iterations para que el usuario escoja su i correspondiente
  return iterationsBot(u, v, x)

  #Fin de la funcion de splitBot


def iterationsBot(u, v, x): 
  #Inicio de la funcion de iterations_bot
    
  #Se actualiza el v (a partir del i suministrado) y se actualiza la cadena a w_i
  i = random.randint(0, 30)

  print(f"El numero i escogido por la replica ha sido: {i}")
    
  v_i = v*i
  w_i = u+v_i+x
  print(f"Su nueva cadena v´ = {v_i} ")
  print(f"Luego su cadena w´ = {w_i} ")
  print("Ahora revisemos si es aceptada por el Lenguaje")

  answer = transs(False, w_i)[0]
  
  #Se decide el ganador del juego:
  
  return answer
        
  #Fin de la funcion de iterations_bot
    
