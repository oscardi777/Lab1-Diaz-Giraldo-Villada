import random
from transFunction import transs

def replicaGame():
    
    #Inicio de la funcion replicaGame
    
    """
    Función que representa el juego en el modo 'Réplica vs Máquina'.
    
    """
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
        print("La cadena aleatoria es: " + cadena)
        answer, cadena, n, m = transs(False, cadena) # Se verifica la cadena
        break
      else: 
        continue
    if answer:    # Se hace la partición y se genera un i aleatorio para realizar el bombeo
      u = cadena[:n-1]        # Toma todas las 'a' iniciales menos la última
      v = cadena[n-1:n+1]     # Toma la última 'a' inicial y la primera 'b'
      x = cadena[n+1:]        # Toma desde la segunda 'b' en adelante

      print("La cadena se ha validado correctamente")
      print("Se hará una partición de la siguiente manera")
      print(f"Se escogerá u = {u} ; v = {v} ; x = {x}")
      print("Ahora se solicita un i valido que mantenga la validez de la cadena:")
      i= random.randint(0,30)
      print(f"El i escogido ha sido: {i}")

    winner = iterations_bot(u, v, x, i)

    if winner:
      print("La cadena es valida, la replica ha ganado")
    else:
      print("La cadena no es valida, la replica ha perdido")
    
    #Fin de la funcion replicaGame


def iterations_bot(u, v, x,i): 
    #Inicio de la funcion de iterations_bot
    
    #Se actualiza el v (a partir del i suministrado) y se actualiza la cadena a w_i
    
    v_i = v*i
    w_i = u+v_i+x
    print(f"Su nueva cadena v´ = {v_i} ")
    print(f"Luego su cadena w´ = {w_i} ")
    print("Ahora revisemos si es aceptada por el Lenguaje")

    answer, string, n, m = transs(modo=False, cadena=w_i)
    
    #Se decide el ganador del juego:
    
    return answer
        
    #Fin de la funcion de iterations_bot
