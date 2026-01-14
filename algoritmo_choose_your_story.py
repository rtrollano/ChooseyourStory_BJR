from db import *


from funciones import *


entrar_juego = True
flag_00 = True
flag_01 = False
flag_02 = False
flag_03 = False
flag_04 = False


while entrar_juego:

    # Funcio imprimir menú +  validació opcion
    opcion = getOpt(textOpts="\n" + menu_logout + "\n",inputOptText="\nOption: ",rangeList=[1, 2, 3, 4, 5],exceptions=[])

    while flag_00:

        # 1)Logout
        if opcion == 1:
            flag_00 = False
            flag_01 = True

        # 2)Play
        elif opcion == 2:
            flag_00 = False
            flag_02 = True

        # 3)Replay Adventure
        elif opcion == 3:
            flag_00 = False
            flag_03 = True

        # 4)Reports
        elif opcion == 4:
            flag_00 = False
            flag_04 = True

        # 5)Exit
        elif opcion == 5:
            input("Exit...")
            flag_00 = False
            entrar_juego = False



# ======================== 1)Logout ================================
    while flag_01:
        print("1)Logout")
        input("Exit...")
        flag_01 = False
        flag_00 = True

# ========================= 2)Play ================================
    while flag_02 :
        # ------ Imprimir posibles AVENTURAS -------
        getFormatedAdventures(get_adventures_with_chars())

        # ------ Escoger AVENTURA -------
        opc_aventura = selectAdventure(get_adventures_with_chars(), game_context)

        # ------ Escoger CHARACTER -------
        opc_character = select_characters(adventures, characters, game_context)

        #### - - - INSERTS - - - character/aventura ####

        # ------- INICIO DEL JUEGO --------
        choices = [] # Guardar decisiones del jugador

        import random

        # Creas un diccionario de estados actuales con sus valores iniciales
        game_states = {}

        states = adventures[game_context['idAdventure']].get('states', [])

        for state_id in states:
            state_info = game_states_master.get(state_id)
            game_states[state_info['name']] = state_info['initial']


        juego_on = True
        current_step = get_first_step_adventure(game_context['idAdventure']) # Primer paso de la aventura

        while juego_on:

            steps_dict = get_id_bystep_adventure(game_context['idAdventure'])
            step_data = steps_dict[current_step]

            print("\n" + getHeader(game_context['nameAdventure']))
            print("\n{}".format(step_data['Description']) + "\n")

            # Obtener diccionario filtrado por juego
            answers_dict = get_answers_bystep_adventure(game_context['idAdventure'])


            # Mostrar opciones sin duplicados
            answer_posible = []
            answers = step_data['answers_in_step']

            for i in range(0, len(answers), 2):
                answer_id = answers[i]
                answer_posible.append(answer_id)

            # Mostrar opciones al usuario a traves de la suma de funciones para
            LEFT_MARGIN = 10
            LINE_WIDTH = 60
            print(getFormatedAnswers(1,answers_dict[(answer_posible[0], current_step)]['Description'],LINE_WIDTH,LEFT_MARGIN))
            print(getFormatedAnswers(2,answers_dict[(answer_posible[1], current_step)]['Description'],LINE_WIDTH,LEFT_MARGIN))


            # Input: usuario solo ve 1 o 2
            id_input = input("\nQue decision tomas? 1 | 2: ")
            while id_input not in ['1', '2']:
                print("Opción NO válida")
                id_input = input("Que decision tomas? 1 | 2: ")

            # Mapear 1/2 a los IDs reales
            id_decision = answer_posible[int(id_input) - 1]

            # Calcular resultado (exito / fallo)
            if id_decision == answer_posible[0]:
                resultado_decision = random.randint(answer_posible[0], answer_posible[0] + 1)
            else:
                resultado_decision = random.randint(answer_posible[1], answer_posible[1] + 1)

            choices.append((current_step, id_decision, resultado_decision)) # GUARDAR decisión + resultado


            # Obtener datos del resultado y imprime consecuencias de la decision
            result_data = answers_dict[(resultado_decision, current_step)]
            print("\nRESULTADO:", result_data['Resolution_Answer'])



            # Asignar pérdidas o ganancias de forma genérica según los estados del juego
            for state_name in game_states:
                # Restar pérdidas si existen, sino 0
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
                    estado_str += state_name.capitalize() + ": " + str(game_states[state_name]) + " | "
                estado_str = estado_str[:-3]  # eliminar el último " | "
                print("Estado actual ->", estado_str)


            # Obtener siguiente paso
            next_step = result_data['NextStep_Adventure']

            # FIN DE LA AVENTURA
            if ('nave' in game_states and game_states['nave'] <= 0) or (
                    'tripulacion' in game_states and game_states['tripulacion'] <= 0):
                print("\n FIN DE LA PARTIDA")
                if 'nave' in game_states and game_states['nave'] <= 0:
                    print("Con los sistemas al borde del colapso y la nave irreparablemente dañada, la misión fracasa;\nun estallido final consume la nave, borrando toda esperanza de supervivencia.")
                    choices.append((current_step, id_decision, 'FINAL_NAVE'))

                if 'tripulacion' in game_states and game_states['tripulacion'] <= 0:
                    print("Los tripulantes caen, víctimas del agotamiento, las enfermedades y los daños físicos sufridos durante la misión;\nLa nave flota en el vacío sin rumbo ni destino.")
                    choices.append((current_step, id_decision, 'FINAL_TRIPULACION'))
                juego_on = False
                flag_02 = False

            elif next_step is None or step_data['Final_Step'] == 1:
                print("\nFIN DE LA AVENTURA")
                input("Press ENTER para volver al menú...")
                juego_on = False
                flag_02 = False
            else:
                # si la partida no termina
                current_step = next_step
                input("\nPresiona ENTER para continuar...\n")






        # # - - - - REPRODUCIR AVENTURA - - - - - -
        # played_choices = getChoices(choices)
        # print(played_choices)
        #
        # for step, decision, result in played_choices:
        #
        #     # Si el resultado es un final
        #     if result == 'FINAL_NAVE':
        #         print("PASO {} → La nave fue destruida. Fin de la misión.".format(step))
        #
        #     elif result == 'FINAL_TRIPULACION':
        #         print("PASO {} → La tripulación no sobrevivió. Fin de la misión.".format(step))
        #
        #     else:
        #         # Resultado normal (numérico)
        #         result_data = answers_dict[(result, step)]
        #         print("PASO {} → {}".format(step, result_data['Resolution_Answer']))

# ==================== 3)Replay Adventure ==========================
    while flag_03:
        print("3)Replay Adventure")
        input("Exit...")
        flag_03 = False
        flag_00 = True

# ======================== 4)Reports ================================
    while flag_04:
        opcion = getOpt(textOpts="\n" + menu_report + "\n",inputOptText="\nOption: ",rangeList=[1, 2, 3, 4],exceptions=[])
        if opcion == 1:
            query = """
                    SELECT a.id_adventure, a.name,
                           s.id_step, s.description,
                           ans.id_answer, ans.description,
                           COUNT(r.id_replay) as num_veces
                    FROM answers ans
                    JOIN steps s ON ans.id_step = s.id_step AND ans.id_adventure = s.id_adventure
                    JOIN adventures a ON s.id_adventure = a.id_adventure
                    LEFT JOIN replay_adventures r ON r.id_adventure = a.id_adventure AND r.id_character = r.id_character
                    GROUP BY a.id_adventure, s.id_step, ans.id_answer
                    ORDER BY num_veces DESC;
                """
            table = getTable(query)
            getFormatedTable(table, title="Most used answer")
            input("\nPress ENTER...")

        input("Exit...")
        flag_04 = False
        flag_00 = True