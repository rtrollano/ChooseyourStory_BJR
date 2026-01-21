import random
from datetime import datetime
from funciones import *

entrar_juego = True
flag_main = True
login = ""

while flag_main:
    opc = getOpt(menu_principal,inputOptText,[1,2,3], exceptions=['w','e',-1])

    # 1)Crear Usuario
    if opc == 1:
        insertUser()

    # 2)Iniciar Sesión
    elif opc == 2:
        if not login:
            login = iniciar_sesion()
            if login:
               print("Has realizado el login correctamente, bienvenido {}\n".format(login))
               print("Enter para continuar...")

               entrar_juego = True
               while entrar_juego:

                   # Funcio imprimir menú +  validació opcion
                   opcion = getOpt(textOpts="\n" + menu_logout + "\n", inputOptText="\nOpcion: ",rangeList=[1, 2, 3, 4, 5], exceptions=[])


                   # ======================== 1)Logout ================================
                   if opcion == 1:
                       input("Cerrando sesion de {}...".format(login))
                       entrar_juego = False
                       login = ""


                   # ========================= 2)Play ================================
                   elif opcion == 2:

                       # --- CONSTRUCCIÓN DEL DICCIONARIO DE AVENTURAS DESDE LA BASE DE DATOS ---
                       adventures = build_adventures_dict()

                       # ------ Imprimir posibles AVENTURAS -------
                       getFormatedAdventures(get_adventures_with_chars())

                       # ------ Escoger AVENTURA -------
                       opc_aventura = selectAdventure(get_adventures_with_chars(), game_context)

                       # Aquí ya tienes la aventura seleccionada, normalmente se guarda en game_context
                       idAdventure = game_context['idAdventure']  # Usamos la aventura que eligió el usuario

                       # Construir diccionario de respuestas desde la base de datos
                       answers_dict = build_answers_by_step_adventure(idAdventure)

                       # ------ Escoger CHARACTER -------
                       characters = get_characters()
                       opc_character = select_characters(adventures, characters, game_context)



                       ####################### Guardar idAdventure/ idCharacter / idUser
                       idUsu = getIdUserByName(login)
                       print("INSERT INTO game (idUser,idCharacter, idAdventure, date) VALUES ({}, {}, {}, {});".format(
                           idUsu, opc_character, opc_aventura, datetime.now()))
                       conn = get_connection()
                       cursor = conn.cursor(dictionary=True)
                       cursor.execute(""" INSERT INTO game (idUser, idAdventure, idCharacter, date) VALUES (%s, %s, %s, %s)
                                                                      """, (idUsu, opc_aventura, opc_character, datetime.now()))
                       states_rows = cursor.fetchall()
                       conn.commit()
                       cursor.close()
                       conn.close()

                       # ------- INICIO DEL JUEGO --------
                       choices = []  # Guardar decisiones del jugador

                       # Creas un diccionario de estados actuales con sus valores iniciales
                       game_states = {}



                       # ---------- Inicializar estados según la aventura dentro de BBDD----------
                       conn = get_connection()
                       cursor = conn.cursor(dictionary=True)
                       cursor.execute(""" SELECT gsm.Name AS state_name, gsm.initial_value
                                                   FROM adventure_states ast
                                                   JOIN game_states_master gsm ON gsm.idState = ast.idState
                                                   WHERE ast.idAdventure = %s
                                               """, (idAdventure,))
                       states_rows = cursor.fetchall()
                       cursor.close()
                       conn.close()



                       # Diccionario con los valores iniciales
                       for row in states_rows:
                           state_name = row['state_name']
                           initial_value = row['initial_value']
                           game_states[state_name] = initial_value

                       # print("GAme_States: {}".format(game_states))

                       # --- CONSTRUCCIÓN DEL DICCIONARIO DE PASOS DESDE LA BBDD ---
                       id_by_steps = build_id_by_steps_dict()

                       # Diccionario de steps para la aventura seleccionada
                       steps_dict = id_by_steps[idAdventure]
                       current_step = min(steps_dict.keys())  # primer step

                       juego_on = True
                       while juego_on:

                           flag_00 = True  # Reiniciar flag_00 cada vez que volvemos al menú

                           step_data = steps_dict[current_step]

                           print("\n" + getHeader(game_context['nameAdventure']))
                           print("\n{}".format(step_data['Description']) + "\n")


                           # --- Construir opciones únicas para mostrar al usuario ---
                           answer_posible = []  # lista con 1 opción por usuario
                           mapa_opciones = {}  # mapea cada opción de usuario (1 o 2) a los idAnswer reales

                           # recorremos todas las respuestas del step actual
                           for key in answers_dict[idAdventure]:
                               idAnswer, step_id = key
                               if step_id == current_step:
                                   desc = answers_dict[idAdventure][key]['Description']
                                   if desc not in answer_posible:
                                       answer_posible.append(desc)
                                   opcion_usuario = answer_posible.index(desc) + 1
                                   if opcion_usuario not in mapa_opciones:
                                       mapa_opciones[opcion_usuario] = []
                                   mapa_opciones[opcion_usuario].append(idAnswer)


                           # --- Mostrar opciones al usuario ---
                           LEFT_MARGIN = 10
                           LINE_WIDTH = 60
                           i = 1
                           while i <= len(answer_posible):
                               print(getFormatedAnswers(i, answer_posible[i - 1], LINE_WIDTH, LEFT_MARGIN))
                               i += 1

                           # --- Input del usuario ---
                           id_input = input("\nQue decision tomas? 1 | 2: ")
                           while id_input != "1" and id_input != "2":
                               print("Opción NO válida")
                               id_input = input("Que decision tomas? 1 | 2: ")
                           id_input = int(id_input)

                           # --- Mapear la opción elegida a uno de los idAnswer reales ---
                           if id_input in mapa_opciones:
                               id_decision = random.choice(mapa_opciones[id_input])
                           else:
                               # esto solo ocurre si no se construyó bien mapa_opciones
                               print("ERROR: No hay respuestas para esa opción")
                               break

                           # Calcular resultado (exito / fallo)
                           resultado_decision = id_decision

                           choices.append((current_step, id_decision, resultado_decision))  # GUARDAR decisión + resultado

                           # Vamos a insertar cada elección tomada
                           insertChoice(current_step, id_decision)

                           # Obtener datos del resultado y imprime consecuencias de la decision
                           result_data = answers_dict[idAdventure][(resultado_decision, current_step)]
                           print("\nRESULTADO:", result_data['Resolution_Answer'])

                           # Asignar pérdidas o ganancias de forma genérica según los estados del juego
                           for state_name in ['tripulacion', 'nave', 'salud']:
                               if state_name in game_states:
                                   if state_name == 'tripulacion':
                                       game_states[state_name] -= result_data.get('crew_loss', 0)
                                   elif state_name == 'nave':
                                       game_states[state_name] -= result_data.get('damage_ship', 0)
                                   elif state_name == 'salud':
                                       game_states[state_name] -= result_data.get('salud', 0)

                           # Imprimir estado de manera genérica
                           if game_states != {}:
                               estado_str = ""
                               for state_name in game_states:
                                   estado_str += state_name.capitalize() + ": " + str(
                                       game_states[state_name]) + " | "
                               estado_str = estado_str[:-3]  # eliminar el último " | "
                               print("Estado actual ->", estado_str)

                           # Obtener siguiente paso
                           next_step = result_data['NextStep_Adventure']

                           # FIN DE LA AVENTURA
                           if ('nave' in game_states and game_states['nave'] <= 0) or ('tripulacion' in game_states and game_states['tripulacion'] <= 0):

                               if 'nave' in game_states and game_states['nave'] <= 0:
                                   print("Con los sistemas al borde del colapso y la nave irreparablemente dañada, la misión fracasa;\nun estallido final consume la nave, borrando toda esperanza de supervivencia.'")
                                   final_id = 1000  # corresponde a FINAL_NAVE
                                   choices.append((current_step, final_id, final_id))

                                   print("\nFIN DE LA AVENTURA")
                                   input("Press ENTER para volver al menú...")


                               if 'tripulacion' in game_states and game_states['tripulacion'] <= 0:
                                   print("Los tripulantes caen, víctimas del agotamiento, las enfermedades y los daños físicos sufridos durante la misión;\nla nave flota en el vacío sin rumbo ni destino.'")
                                   final_id = 999  # corresponde a FINAL_TRIPULACION
                                   choices.append((current_step, final_id, final_id))

                                   print("\nFIN DE LA AVENTURA")
                                   input("Press ENTER para volver al menú...")
                               juego_on = False


                           elif next_step is None or step_data['Final_Step'] == 1:
                               print("\nFIN DE LA AVENTURA")
                               input("Press ENTER para volver al menú...")
                               juego_on = False



                           else:
                               # si la partida no termina
                               current_step = next_step
                               input("\nPresiona ENTER para continuar...\n")

                       print(game_context)
                       input("\nPresiona ENTER para continuar...\n")


                       played_choices = getChoices(choices)


                   # ==================== 3)Replay Adventure ==========================
                   elif opcion == 3:
                       print("3)Rejugar Aventura")
                        #Mostramos tabla con los datos de las aventuras registradas
                       replay()

                       opc = input("Elige una aventura -> ")
                       while opc.isalpha():
                           opc = input("Incorrecto. Introduce un valor numérico por favor -> ")
                       opc = int(opc)

                       recuDatosReplay(opc)
                   # ======================== 4)Reports ================================
                   elif opcion == 4:
                       report = True
                       while report:
                           opcion = getOpt(textOpts="\n" + menu_report + "\n",inputOptText="\nOpcion: ", rangeList=[1, 2, 3, 4],exceptions=[])
                           opcion = int(opcion)

                           if opcion == 1:

                               # Recoger datos de las tablas (RESPUESTAS más usadas)
                               rows = get_most_used_answers_per_adventure(6)

                               # Formatear la impresion de los datos
                               print_most_used_answers(rows)

                           elif opcion == 2:

                               conn = get_connection()
                               cursor = conn.cursor(dictionary=True)

                               cursor.execute("""
                                   SELECT username, partidas
                                   FROM (
                                       SELECT u.Username AS username, COUNT(g.idGame) AS partidas
                                       FROM user u
                                       JOIN game g ON g.idUser = u.idUser
                                       GROUP BY u.idUser, u.Username
                                   ) t
                                   WHERE partidas = (
                                       SELECT MAX(partidas)
                                       FROM (
                                           SELECT COUNT(idGame) AS partidas
                                           FROM game
                                           GROUP BY idUser
                                       ) x
                                   );""")

                               rows = cursor.fetchall()

                               cursor.close()
                               conn.close()

                               if not rows:
                                   print("No hay partidas registradas.")
                                   input("Presiona ENTER para continuar...")
                               else:
                                   print("=" * 90+ "\n" +"Jugador que más veces ha jugado".center(90,) + "\n"+"=" * 90)

                                   cabecera_usuario = "NOMBRE USUARIO"
                                   cabecera_partidas = "PARTIDAS JUGADAS"

                                   print("{:<70}{}".format(cabecera_usuario, cabecera_partidas))
                                   print("*" * 90)

                                   for row in rows:
                                       username = row['username']
                                       partidas = row['partidas']

                                       linea = "{:<70}{}".format(username, partidas)
                                       print(linea)

                                   input("\nPresiona ENTER para continuar...\n")

                           elif opcion == 3:
                               username_input = input("Que usuario quieres ver?: ").strip()

                               conn = get_connection()
                               cursor = conn.cursor(dictionary=True)

                               cursor.execute("""
                                   SELECT 
                                       g.idAdventure AS idAdventure,
                                       a.Name AS adventure_name,
                                       g.date AS game_date
                                   FROM game g
                                   JOIN user u ON u.idUser = g.idUser
                                   JOIN adventure a ON a.idAdventure = g.idAdventure
                                   WHERE u.Username = %s
                                   ORDER BY g.date""", (username_input,))

                               rows = cursor.fetchall()

                               cursor.close()
                               conn.close()

                               print("=" * 120)
                               titulo = "Partidas jugadas por {}".format(username_input)
                               print(titulo.center(120))
                               print("=" * 120)

                               cab_id = "idAdventure"
                               cab_name = "Name"
                               cab_date = "date"

                               print("{:<40}{:<40}{}".format(cab_id, cab_name, cab_date))
                               print("*" * 120)

                               if len(rows) == 0:
                                   print("No se han encontrado partidas jugadas de este User.")
                               else:
                                   for row in rows:
                                       id_adventure = row['idAdventure']
                                       adventure_name = row['adventure_name']
                                       game_date = row['game_date']

                                       linea = "{:<40}{:<40}{}".format(
                                           id_adventure,
                                           adventure_name,
                                           game_date)
                                       print(linea)

                               input("\nPresiona ENTER para continuar...\n")

                           elif opcion == 4:
                                input("Back...")
                                report = False




                   # 5)Exit
                   elif opcion == 5:
                       print("Saliendo...")
                       entrar_juego = False
                       flag_main = False




    # 3)Mostrar aventuras
    elif opc == 3:
        if not login:
            print("No puedes empezar a jugar sin hacer login antes.")
            input("Pulsa enter para continuar.")

    # 4)Salir
    elif opc == 4:
        print("Cerrando el programa...")
        flag_main = False
