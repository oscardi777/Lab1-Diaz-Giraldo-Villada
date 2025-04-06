# Lab1-Diaz-Giraldo-Villada
Proyecto Laboratorio 1 LFA

Archivo transFunction.py:

    Función countletters(string, pos, l, door)
    
    """
    Cuenta la cantidad de caracteres consecutivos de un tipo ('a' o 'b') en una cadena.

    Parámetros:
        - string (str): Cadena de caracteres a analizar.
        - pos (int): Posición inicial desde donde iniciar el conteo.
        - l (char): Carácter ('a' o 'b') que se va a contar.
        - door (bool): Si es True, la función invalidará la cadena si encuentra una 'b' después de la segunda sección de 'a'.

    Retorna:
        - (bool) Indica si la estructura de la cadena sigue siendo válida hasta este punto.
        - (int) Número de caracteres 'l' consecutivos encontrados.
        - (int) Posición final después del conteo.
    """

    Función transs(modo, cadena)
    """
    Función que valida una cadena de caracteres compuesta por 'a' y 'b'.

    Parámetros:
        - cadena (str): Cadena de caracteres a analizar.
        - modo (bool): Si es True, la función toma el camino a solicitar la cadena hasta que el usuario digite una correcta
                       Si es False, la función toma el camino a simplemente validar si la cadena ingresada sera acepta o no

    La validación se realiza con base en las siguientes reglas:
    1. La cadena debe tener una cantidad inicial de 'a'.
    2. Luego debe haber una cantidad de 'b'.
    3. Finalmente, otra cantidad de 'a', sin que después de esta última parte haya más 'b'.
    4. La diferencia entre la cantidad de 'a' al inicio y las 'b' con respecto a las 'a' finales
        debe ser un múltiplo de 3.
    5. La cadena debe tener una longitud mayor o igual a un valor aleatorio `r` entre 8 y 30.

    Retorna:
        - (True, string, n) si la cadena es válida, donde:
            -True es para reportar que se ha tomado una cadena valida
            -string es para que se tenga la cadena guardada en el codigo
            -n es la posicion de la primera de las b´s dentro de la cadena
        - Continúa solicitando la entrada si la cadena no es válida.
    """

Archivo playerGame.py:
    Función userGame()
    """
    Función que representa el juego en el modo 'Usuario vs Máquina'.

    Valida la cadena ingresada y si es correcta, procede con la partición de la misma.

    Lo hace a partir de la función transs(True, "") que al estar en True se pedira una cadena al usuario hasta que digite alguna valida

    Esta función ademas de retornar la cadena del usuario, retorna la posicion donde empiezan las letras b´s de la cadena elegida por el usuario. Esta informacion es importante para realizar la particion en las subcadenas u, v y x

    Llama a la función iterations() para que el programa empiece a validar si la palabra uv^ix sera aceptada de acuerdo al i que escoja el usuario

    Función iterations(u, v, x)

    Función que realizara la validacion pertinente al valor i seleccionado por el usuario que podra o no ser aceptada.

    Recibe como parametros cada una de las subcadenas u, v y x. Y le solicita al usuario el numero i para repetir la cadena v.

    Se solicita el i del usuario que debe ser mayor o igual a 0 hasta que se cumpla con un numero valido.

    Se actualiza la cadena a partir del i ingresado por el usuario para crear w_i, la cual ahora sera validada por transs

    Esta ultima función en particular, ahora sera llamada con su modo en Falso para que no verifique la cadena "hasta" que la misma sea aceptada, sino que tendra el resultado de ser aceptada o no y es todo.

    Asi se definiria si el usuario gana o pierde en el juego

    """
Archivo botGame.py:
    Función replicaGame()
    """
    Función que representa el juego en el modo 'Réplica vs Máquina'.

    Genera cadenas aleatorias que pertenecen a L, las valida y procede con la partición de estas.
    
    Lo hace a partir de la función transs(False, cadena) que al estar en False no se pedira una cadena al usuario, sino que verifica directamente la cadena que recibio como parámetro de entrada.

    Esta función ademas de retornar la cadena aleatoria, retorna la posicion donde empiezan las letras b´s de la misma. Esta informacion es importante para realizar la particion en las subcadenas u, v y x

    Llama a la función iterationsBot() para que el programa empiece a validar si la palabra uv^ix sera aceptada de acuerdo a un i generado aleatoriamente. 

    Función iterationsBot(u, v, x)

    Función que realizara la validacion pertinente al valor i aleatorio.

    Recibe como parametros cada una de las subcadenas u, v, x. Y genera un numero i aleatorio 

    Se actualiza la cadena a partir del i aleatorio para crear w_i, la cual ahora sera validada por transs

    Esta ultima función en particular, ahora sera llamada con su modo en Falso para que no verifique la cadena "hasta" que la misma sea aceptada, sino que tendra el resultado de ser aceptada o no y es todo.

    Asi se definiria si la replica gana o pierde en el juego.
    
Archivo main.py
    Función menu:

    Es un menu sencillo donde se tiene los dos modos de juego, tanto para la replica como para el usuario "contra" la maquina, a partir de que el usuario digite una opcion valida para cada modo de juego.
