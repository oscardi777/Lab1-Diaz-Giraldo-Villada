# Lab1-Diaz-Giraldo-Villada
Proyecto Laboratorio 1 LFA

# Para ejecutar el codigo descargue los cuatro archivos:
    -botGame.py
    -main.py
    -playerGame.py
    -transFunction.py
Y luego ejecute desde la terminal (en la carpeta donde se encuentran los cuatro archivos):

Python .\main.py

# Explicación de las funciones encontradas en cada archivo:

" Archivo transFunction.py:

    """
    Función transs(modo, cadena):
    """

        Función que valida una cadena de caracteres compuesta por 'a' y 'b'.

        """
        Parámetros:
        """

            - modo (bool): 
                -Si es True, la función toma el camino a solicitar la cadena hasta que el usuario digite una correcta
                -Si es False, la función toma el camino a simplemente validar si la cadena ingresada sera acepta o no
            - cadena (str): Cadena de caracteres a analizar

        """
        Funcionamiento:
        """

            La validacion de esta cadena se realiza con la función validar_cadena()
            Que dependiendo del bool modo, se pedira al usuario la cadena o no

            Cuando el modo es True se utiliza randint(8, 30) para simular un numero aleatorio que determinara la longitud minima de la cadena a solicitar al usuario
            Asi mismo en este modo le pedira al usuario una cadena valida (determinada por la funcion validar_cadena()) indefinidamente hasta que se indique valido = True (primer valor de retorno de la función validar_cadena())
            

        """
        Retorna:
        """

            - bool es para reportar que se ha tomado una cadena valida o no (True or False)
            - string es para que se tenga la cadena valida para su uso en la particion de la cadena
            - n es la posicion de la primera de las b´s dentro de la cadena
            - m es la posicion de la primera de las segundas a´s de la cadena


    """
    Función validar_cadena(w, r=0):
    """

        Esta funcion en resumen es la que determinara si la cadena es valida o no en L

        """
        Parámetros:
        """

            -w (str): Es la cadena escogida por el usuario o la Replica segun sea el caso pendiente por validarse su aceptacion en L
            -r=0 (int): Es la longitud minima de la palabra que el usuario o la Replica deben cumplir para ser validas minimo, por defecto se imputa r=0 para el caso en el que solo se validara la aceptacion de la cadena

        """
        Funcionamiento:
        """

        Esta función llama a la función countletters() para conocer la cantidad de cada caracter de la palabra pendiente por validar.
        Es llamada para conocer primero la cantidad inicial de a´s, luego la cantidad de b´s y por ultimo la segunda seccion de a´s
        La función countletters() reporta si ha encontrado un caracter distinto al final de la ultima seccion de a´s, por lo que alerta a la funcion si sera valida o no para su lectura
        Gracias a la función countletters() tambien es posible conocer las posiciones donde inicia y termina cada caracter, es asi como los valores n y m son inicializados
        Con la cantidad de a´s y b´s de la cadena es posible conocer la longitud de la misma (porque las palabras aceptas solo seran del tipo a^k*b^s*a^n)
        Luego se determina si la cadena es valida (de la forma propuesta para ser acepta por L a^k*b^s*a^n)
        Se determina la congruencia por el modulo y se verifica que su longitud sea mayor a la longitud r aleatoria que viene si la cadena hasta ahora esta siendo escrita por el usuario

        Para la congruencia por el modulo, es conocido que si k+s (congruente) n (mod3) es porque: k+s = 3*l + x y n = 3*p + x
        Es decir tienen el mismo residuo. Pero esto es lo mismo que si k+s-n = 3*o es decir que k+s-n sea multiplo de 3 (por tener el mismo residuo) es por esto que la verificacion del modulo se verifica revisando si k+s-n mod 3 == 0


        """
        Retorna:
        """

            - (bool) Indica si la estructura de la cadena ha sido aceptada
            - (str) Retorna la cadena que ha sido aceptada finalmente
            - (int) Número de caracteres 'l' consecutivos encontrados.
            - (int) Posición final después del conteo.


    """
    Función countletters(string, pos, l, door)
    """

        Función que contara la cantidad de letras en cada seccion de la cadena

        """
        Parámetros:
        """

            - w (str): La cadena completa que se desea analizar.
            - pos (int): Es la posición inicial desde donde se empezará a leer la cadena. Permitiendo segmentar la lectura para verificar cada sección.
            - l (str): Es el carácter que se desea contar. Puede ser 'a' o 'b' dependiendo del bloque que se esté evaluando.
            - door (bool): Si es True, se utiliza como medida de seguridad para validar que después del último bloque de 'a' (en la tercera sección) no aparezcan otros caracteres como 'b'.   

        """
        Funcionamiento:
        """     

            La función recorre la cadena w desde la posición pos, leyendo carácter por carácter. 
            Si el carácter coincide con l, incrementa un contador cont y avanza una posición.
            Si el carácter es distinto a l, se toman dos caminos:
                - True, se retorna inmediatamente False, ya que se ha violado la estructura esperada del lenguaje (una 'b' luego de las segundas 'a').
                - False, se retorna el número de letras l contadas consecutivamente, y la posición donde se detuvo la lectura.
            Al finalizar la lectura completa sin errores, se retorna que la cadena es válida para esa sección junto al número de letras contadas y la posición final alcanzada.

        """
        Retorna:
        """

            - (bool): Indica si la secuencia de caracteres evaluada cumple con la estructura esperada. En especial, si door=True, este valor puede ser False si se detecta un carácter no permitido al final de la lectura.
            - (int): Número total de caracteres l consecutivos contados desde la posición pos.
            - (int): Posición final alcanzada al terminar de contar los caracteres (para la siguiente lectura).


    
" Archivo playerGame.py:

    """
    Función userGame(machine_winners, sesgo):
    """

        Función que permite la interaccion entre el usario en juego VS la Maquina.

        """
        Parámetros:
        """
            - machine_winners (int): Contador de las veces que la máquina ha ganado.
            - sesgo (bool): Indica si se estara jugando para que la maquina Gane "sesgadamente" (el 90% de las veces) o si se esta jugando en igualdad de condiciones

        """
        Funcionamiento:
        """

            Se llama a la función transs() para solicitar y validar una cadena proporcionada por el usuario.

            Si la cadena es válida (a traves del booleano recibido en answer, retornado en la función transs()), se llama a la función splitPlayer() para aplicar el lema del bombeo con selección aleatoria.

            Dependiendo del resultado de splitPlayer() (si la nueva cadena es aceptada o no por el lenguaje, a traves del booleano winner, retornado por la funcion splitPlayer()), se imprime un mensaje informando si el jugador ganó o perdió.

            Si el jugador pierde, se incrementa el contador de victorias de la máquina.
            
        """
        Retorna:
        """

            - (int): El nuevo valor de machine_winners, actualizado si el jugador ha perdido.

    """
    Función splitPlayer(cadena, n, m, sesgo):
    """

        Función que aplica el Lema del bombeo para soliciar revisar la aceptacion de una nueva cadena en L.

        """
        Parámetros:
        """

            - cadena (str): Cadena que ya ha sido validada y pertenece al lenguaje.
            - n (int): Posición de la primera 'b' en la cadena.
            - m (int): Posición de la primera 'a' de la segunda seccion en la cadena.
            - sesgo (bool): Indica si se estara jugando para que la maquina Gane "sesgadamente" (el 90% de las veces) o si se esta jugando en igualdad de condiciones.

        """
        Funcionamiento:
        """

            Se determina la posición de parada stop según el caso, a partir de un random para dinamismo en la seleccion de la subcadena v:
                - Si hay una sola 'b' (m-n == 1), se toma stop = m.
                - Si no hay 'a' antes de las 'b' o n == m, se escoge una nueva n = m/2 y se elige aleatoriamente stop en el intervalo (n+1, m). (porque cadenas del tipo a^l o b^k son aceptadas en el lenguaje siempre y cuando sean multiplos de 3)
                - En los demás casos, simplemente se escoge stop al azar entre (n+1, m) (desde n+1 y no desde n porque hay la posibilidad de que se escoja la misma posicion donde se empieza y no es recomendable sobretodo si se esta jugando en el modo con sesgo).
            Si sesgo es True, se incrementa n en 1. 

            (Basicamente aqui es donde ocurre la modificacion de que la maquina pueda ganar en un 90% de las ocasiones y es que cuando sesgo es False, la n estara escogida exactamente donde empiezan las b, de tal manera que como se observa en la particion de las subcadenas u, v y x, se muestra que la cadena v tomara una a hasta una cantidad stop de b´s, de manera tal que si el usuario escoge un i!=1 la cadena no sera aceptada por el lenguaje, ya que el v sera de la forma (ab^stop)^i la cual no sera aceptada por el lenguaje al tener cadenas (ab)^s en el medio de la cadena)

            (Por otro lado si Sesgo es True se empezara con n+1 lo que hace que la cadena v empiece desde (n+1)-1 que es n, es decir basicamente desde donde empiezan las b´s originalmente, lo que le da la oportunidad al usuario de contar cuantas b´s se han seleccionado en la subcadena v (dependiendo del random stop) y asi puede que gane si toma un i valido para la nueva cadena)

            Se construyen las subcadenas u, v, y x como:
            u = cadena[:n-1]
            v = cadena[n-1:stop]
            x = cadena[stop:]
            
            Se imprime la partición resultante y se llama a iterationsPlayer(u, v, x) para aplicar el bombeo con un valor i elegido por el usuario.
            
        """
        Retorna:
        """

            - (bool): Indica si la nueva cadena w' resultante de aplicar el lema del bombeo sigue siendo aceptada por el lenguaje.

    """
    Función iterationsPlayer(u, v, x):
    """

        Función que aplica la segunda parte del lema del bombeo pidiendo un i que creara una nueva cadena pendiente a revisar si es valida o no.

        """
        Parámetros:
        """

            - u (str): Subcadena inicial antes del segmento a bombear.
            - v (str): Subcadena que se repetirá i veces.
            - x (str): Subcadena final, después del segmento bombeado.

        """
        Funcionamiento:
        """

            Se solicita al usuario que ingrese un valor entero no negativo para i, que representa cuántas veces se repetirá la subcadena v.
            El ciclo se repite hasta que se ingrese un valor válido (i >= 0).
            Se construyen las nuevas cadenas:
            v' = v * i
            w' = u + v' + x
            Se imprimen ambas cadenas resultantes.
            Se llama a transs(False, w') para validar si la nueva cadena sigue siendo aceptada por el lenguaje.
            
        """
        Retorna:
        """

            - (bool): Indica si la nueva cadena bombeada pertenece al lenguaje L.

" Archivo botGame.py:

    """
    Función replicaGame():
    """

        Función que representa el juego en el modo 'Réplica vs Máquina'.

        """
        Parámetros:
        """

            - machine_winners (int): Contador de las veces que la máquina ha ganado.
            - sesgo (bool): Indica si se estara jugando para que la maquina Gane "sesgadamente" (el 90% de las veces) o si se esta jugando en igualdad de condiciones

        """
        Funcionamiento:
        """

            Función que representa el juego en el modo 'Réplica vs Máquina'.
            Genera cadenas aleatorias que pertenecen a L, las valida y procede con la partición de estas.
            Lo hace a partir de la función transs() que al estar en False no se pedira una cadena al usuario, sino que verifica directamente la cadena que recibio como parámetro de entrada.
            Esta función ademas de retornar la cadena aleatoria, retorna la posicion donde empiezan las letras b´s de la misma. Esta informacion es importante para realizar la particion en las subcadenas u, v y x

            Llama a la función splitBot() para que el programa realice la particion a las subcadenas u, v y x y luego a su vez se verifique su aceptación
            
        """
        Retorna:
        """

            - (int): El nuevo valor de machine_winners, actualizado si la Replica ha perdido.

    """
    Función splitBot(cadena, n, m, sesgo):
    """

        Función que aplica el Lema del bombeo para soliciar revisar la aceptacion de una nueva cadena en L (en el modo de juego de la Replica).

        """
        Parámetros:
        """

            - cadena (str): Cadena que ya ha sido validada y pertenece al lenguaje.
            - n (int): Posición de la primera 'b' en la cadena.
            - m (int): Posición de la primera 'a' de la segunda seccion en la cadena.
            - sesgo (bool): Indica si se estara jugando para que la maquina Gane "sesgadamente" (el 90% de las veces) o si se esta jugando en igualdad de condiciones.

        """
        Funcionamiento:
        """

            **(Se Realiza el mismo procedimiento que en la función splitBot() solo que con la cadena aleatorea generada anteriormente)**

            Se determina la posición de parada stop según el caso, a partir de un random para dinamismo en la seleccion de la subcadena v:
                - Si hay una sola 'b' (m-n == 1), se toma stop = m.
                - Si no hay 'a' antes de las 'b' o n == m, se escoge una nueva n = m/2 y se elige aleatoriamente stop en el intervalo (n+1, m). (porque cadenas del tipo a^l o b^k son aceptadas en el lenguaje siempre y cuando sean multiplos de 3)
                - En los demás casos, simplemente se escoge stop al azar entre (n+1, m) (desde n+1 y no desde n porque hay la posibilidad de que se escoja la misma posicion donde se empieza y no es recomendable sobretodo si se esta jugando en el modo con sesgo).
            Si sesgo es True, se incrementa n en 1. 

            (Basicamente aqui es donde ocurre la modificacion de que la maquina pueda ganar en un 90% de las ocasiones y es que cuando sesgo es False, la n estara escogida exactamente donde empiezan las b, de tal manera que como se observa en la particion de las subcadenas u, v y x, se muestra que la cadena v tomara una a hasta una cantidad stop de b´s, de manera tal que si el usuario escoge un i!=1 la cadena no sera aceptada por el lenguaje, ya que el v sera de la forma (ab^stop)^i la cual no sera aceptada por el lenguaje al tener cadenas (ab)^s en el medio de la cadena)

            (Por otro lado si Sesgo es True se empezara con n+1 lo que hace que la cadena v empiece desde (n+1)-1 que es n, es decir basicamente desde donde empiezan las b´s originalmente, lo que le da la oportunidad de ganar a la replica siempre y cuando ingrese un i valido para que la nueva cadena sea aceptada)

            Se construyen las subcadenas u, v, y x como:
            u = cadena[:n-1]
            v = cadena[n-1:stop]
            x = cadena[stop:]
            
            Se imprime la partición resultante y se llama a iterationsBot(u, v, x) para aplicar el bombeo con un valor i elegido por la replica.
            
        """
        Retorna:
        """

            - (bool): Indica si la nueva cadena w' resultante de aplicar el lema del bombeo sigue siendo aceptada por el lenguaje.

    """
    Función iterationsBot(u, v, x):
    """

        Función que aplica la segunda parte del lema del bombeo pidiendo un i que creara una nueva cadena pendiente a revisar si es valida o no.

        """
        Parámetros:
        """

            - u (str): Subcadena inicial antes del segmento a bombear.
            - v (str): Subcadena que se repetirá i veces.
            - x (str): Subcadena final, después del segmento bombeado.

        """
        Funcionamiento:
        """

            La Replica generara un numero i aleatorio 
            Se actualiza la cadena a partir del i aleatorio para crear w_i, la cual ahora sera validada por transs(), a partir de:
            v' = v * i
            w' = u + v' + x
            La función transs() ahora sera llamada con su modo en Falso para que no verifique la cadena "hasta" que la misma sea aceptada, sino que tendra el resultado de ser aceptada o no y es todo.
            
            Asi se definiria si la replica gana o pierde en el juego.
            
        """
        Retorna:
        """

            - (bool): Indica si la nueva cadena bombeada pertenece al lenguaje L.

" Archivo main.py:

    """
    Función menu():
    """
        Función que inicia el juego para cada modo en especifico (Usuraio vs Maquina y Replica vs Maquina)

        """
        Parámetros:
        """

            - Esta función no recibe parametros

        """
        Funcionamiento:
        """

            Se inicializan cuatro contadores:
                - machineWinPlayer: contador de victorias de la máquina en modo Usuario vs Máquina.
                - gamesPlayer: cantidad total de juegos jugados en el modo Usuraio vs Maquina.
                - machineWinReplica: contador de victorias de la máquina en el modo Réplica vs Máquina.
                - gamesReplica: cantidad total de juegos jugados en el modo Replica vs Maquina.
            
            Se entra en un ciclo while True para mantener activo el menú hasta que el usuario decida salir.
            
            En cada iteración se genera un número aleatorio entre 0 y 100, que se utilizará para definir si se aplicará el sesgo (sesgo = True si p >= 90).
            (Esta linea en especifico es el cambio en general que determina si el juego que se hara sera en igualdad de condiciones o injusto para que el 90% de las ocasiones la Maquina gane)
            (Debido a que se genera un numero aleatorio entre 0 y 100, se tiene la posibilidad de que el mismo sea mayor a 90 en un 10% de las veces, cuando esto sucede sesgo indicara en las respectivas funciones que se jugara en igualdad de condiciones, de otra manera el juego quedara sesgado para que la maquina gane)
            
            Se imprime el menú con cuatro opciones:
                1. Usuario vs Máquina
                2. Réplica vs Máquina
                3. Mostrar resultados
                4. Salir
            Dependiendo de la opción ingresada:

                - Si es "1": Se ejecuta userGame() pasando los parámetros actuales. Se actualiza el conteo de juegos y posiblemente las victorias de la máquina contra el Usuario.
                - Si es "2": Se ejecuta replicaGame() Se actualiza el conteo de juegos y posiblemente las victorias de la máquina contra la Réplica.
                - Si es "3": Se muestran por pantalla los resultados acumulados de ambas modalidades.
                - Si es "4": Se imprime un mensaje de salida y se termina el bucle while con break.
                - Si es otra opción: Se imprime un mensaje de error indicando que la opción no es válida.
            
        """
        Retorna:
        """

            - Nada. Esta función ejecuta todo su funcionamiento dentro de un bucle infinito hasta que el usuario decide salir.
