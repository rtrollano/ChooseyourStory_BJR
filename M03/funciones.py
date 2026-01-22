import textwrap
import mysql.connector
from db import *

# =======================
# Diccionario game_context
# =======================
game_context = {
    'idGame':1,
    'idAdventure': 1,
    'nameAdventure': 'Expedición al Sector Z-47',
    'user': 'Jugador1',
    'idUser': 1,
    'idChar': 1,
    'characterName': 'Alex',  # Puede cambiar según elección
}




# =======================
# Diccionario replayAdventures
# =======================
replayAdventures = {
    1: {'idUser': 1, 'Username': 'Jugador1', 'idAdventure': 1, 'Name': 'Expedición al Sector Z-47', 'idCharacter': 1, 'CharacterName': 'Alex'},
    2: {'idUser': 1, 'Username': 'Jugador1', 'idAdventure': 1, 'Name': 'Expedición al Sector Z-47', 'idCharacter': 2, 'CharacterName': 'Sam'},
    3: {'idUser': 1, 'Username': 'Jugador1', 'idAdventure': 1, 'Name': 'Expedición al Sector Z-47', 'idCharacter': 3, 'CharacterName': 'Riley'}
}





# =================================================================
#                            FUNCIONES
# =================================================================

#def get_answers_bystep_adventure(idAdventure):
#    return idAnswers_ByStep_Adventure[idAdventure]



# - - - - CREA DICCIONARIO ADVENTURE - - - - -
def get_adventures_with_chars():
    """
    Recupera todas las aventuras desde la base de datos.
    Devuelve un diccionario con la estructura:
    { idAdventure: {'Name': nombre, 'Description': desc, 'characters': [...], 'states': [...] } }
    """
    conn = get_connection()
    if conn is None:
        print("Error: no se pudo conectar a la base de datos")
        return {}

    cursor = conn.cursor(dictionary=True)

    # --- Recuperar info básica de aventuras ---w
    cursor.execute("SELECT * FROM adventure")
    aventuras_db = cursor.fetchall()
    adventures_dict = {}
    for adv in aventuras_db:
        adventures_dict[adv["idAdventure"]] = {
            "Name": adv["Name"],
            "Description": adv["Description"]        }
    # --- Recuperar personajes asociados a cada aventura ---
    cursor.execute("SELECT idAdventure, idCharacter FROM adventure_characters")
    adv_chars = cursor.fetchall()
    for row in adv_chars:
        adv_id = row["idAdventure"]
        char_id = row["idCharacter"]
        if adv_id in adv_chars:
            adv_chars[adv_id]["idCharacter"].append(char_id)

    # --- Recuperar estados asociados a cada aventura ---
    cursor.execute("SELECT idAdventure, idState FROM adventure_states")
    adv_states = cursor.fetchall()
    for row in adv_states:
        adv_id = row["idAdventure"]
        state_id = row["idState"]
        if adv_id in adv_states:
            adv_states[adv_id]["idState"].append(state_id)

    cursor.close()
    conn.close()

    return adventures_dict





# - - - - CREA DICCIONARIO CHARACTERS - - -
def get_characters():
    """devuelve un diccionario: { id_character: name }
    """
    characters = {}

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT idCharacter, CharacterName
        FROM characters
        ORDER BY idCharacter
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        characters[row["idCharacter"]] = row["CharacterName"]

    cursor.close()
    conn.close()

    return characters




def getReplayAdventures():
    return replayAdventures




# DEVUELVE UNA TUPLA CON LAS CHOICES DEL USER
def getChoices(choices):
    return tuple(choices)




# FORMATEA BONITO LA IMPRESIÓN DE AVENTURAS DISPONIBLES
def getFormatedAdventures(adventures):
    DESC_W = 50

    cabecera_adv = ("Adventures".center(130, '=') + "\n" +"{:<20}{:<60}{:<50}\n".format("Id Adventure", "Adventure", "Description") +"*" * 130 + "\n\n")

    datos = ""
    list_adventures = list(adventures.keys())

    for i in range(len(list_adventures)):
        adv_id = list_adventures[i]
        name = adventures[adv_id]['Name']
        desc = adventures[adv_id]['Description']

        # Cortar descripcion en varias lineas
        desc_lines = textwrap.wrap(desc, DESC_W)

        datos += "{:<20}{:<60}{}\n".format(i + 1, name, desc_lines[0])

        # Lineas siguientes (solo descripcion)
        for line in desc_lines[1:]:
            datos += "{:<20}{:<60}{}\n".format("", "", line)

        datos += "\n"

    print(cabecera_adv + datos)




# CONSTRUIR DICCIONARIO DE CONTEXTO AVENTURAS
def build_dic_adventura_context():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT idAdventure, context_text
        FROM adventure_context
    """)

    rows = cursor.fetchall()

    adventure_context = {}

    for row in rows:
        adventure_context[row['idAdventure']] = row['context_text']

    cursor.close()
    conn.close()

    return adventure_context





# - - - PIDE Y VALIDA LA ELECCION DE LA AVENTURA Y IMPRIME EL CONTEXTO DE ESTA - - -
def selectAdventure(adventures, game_context):
    list_adventures = list(adventures.keys())

    opc_aventura = input("\nElige la aventura: ")
    while not opc_aventura.isdigit() or int(opc_aventura) not in range(1, len(list_adventures) + 1):
        print("Opción inválida")
        opc_aventura = input("Elige la aventura: ")

    opc_aventura = list_adventures[int(opc_aventura) - 1]

    #print("opc", opc_aventura)
    #input("...")

    # Actualizar game_context
    game_context['idAdventure'] = opc_aventura
    game_context['nameAdventure'] = adventures[opc_aventura]['Name']


    adventure_context = build_dic_adventura_context()
    # Mostrar contexto inicial (si existe)
    if opc_aventura in adventure_context:
        print("\n=== CONTEXTO DE LA AVENTURA ===")
        print(adventure_context[opc_aventura])
        input("\nPresiona ENTER para comenzar la aventura...\n")

    return opc_aventura




# - - - IMPRIME LOS CHARACTERS DISPO SEGUN AVENTURA - - -
def select_characters(adventures, characters, game_context):
    """
    Muestra los personajes disponibles para la aventura seleccionada,
    usando la tabla adventure_characters.
    """
    idAdventure = game_context

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    print(idAdventure)
    cursor.execute("""
        SELECT idCharacter
        FROM adventure_characters
        WHERE idAdventure = %s
    """, (idAdventure["idAdventure"],))
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    if not rows:
        print(" Esta aventura no tiene personajes asignados.")
        return None

    character_ids = [row['idCharacter'] for row in rows]

    print("\n" + "Characters".center(100, "=") + "\n")
    for id_char in character_ids:
        print(f"{id_char}) {characters[id_char]}")

    opc_character = input("\nElige el personaje: ")
    while not opc_character.isdigit() or int(opc_character) not in character_ids:
        print("Opción inválida")
        opc_character = input("Elige el personaje: ")

    opc_character = int(opc_character)

    return opc_character





# GENERA EL HEADER CON NOMBRE AVENTURA EN CADA DECSIÓN NUEVA
def getHeader(text):
    cabecera = ("*"*160 + "\n" +text.center(160, '=') + "\n"+ "*"*160 )
    return cabecera




# IMPRIME BONITO LAS OPCIONES QUE PUEDE ELEGIR EL USER EN CADA DECISIÓN
def getFormatedAnswers(idAnswer, text, lenLine, leftMargin):
    lines = textwrap.wrap(text, lenLine)

    margin = " " * leftMargin
    output = ""

    # Primera linea con el id
    output += "{}{}) {}\n".format(margin, idAnswer, lines[0])

    # Lineas siguientes alineadas
    for line in lines[1:]:
        output += "{}   {}\n".format(margin, line)

    return output




# IMPRIMIR UN MENÚ ESTILO: menu_logout = "1)Logout\n2)Play\n3)Replay Adventure\n4)Reports\n5)Exit"
def getOpt(textOpts="", inputOptText="", rangeList=[], dictionary={}, exceptions=[]):
    # Mostrar menu
    print(textOpts)
    while True:
        opt = input(inputOptText)
        # Caso excepciones (aceptar tal cual)
        if opt in exceptions:
            return opt
        # Si es numero
        if opt.isdigit():
            opt_int = int(opt)
            # Valido por lista
            if opt_int in rangeList:
                return opt_int
            # Valido por diccionario
            if dictionary and opt_int in dictionary.keys():
                return opt_int

        print("El valor introducido no es una opción válida")




# - - - CONSTRUIR DICCIONARIO DE POSIBLES RESPUESTAS CON SUS CONSEQUENCIAS Y STATES SEGÚN AVENTURA - - -
def build_answers_by_step_adventure(idAdventure):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT idAnswer, idStep, description, resolution_answer, next_step,
               crew_loss, damage_ship, salud
        FROM answers
        WHERE idAdventure = %s
    """, (idAdventure,))
    answers = cursor.fetchall()

    result = {idAdventure: {}}
    for a in answers:
        key = (a['idAnswer'], a['idStep'])
        result[idAdventure][key] = {
            'Description': a['description'],
            'Resolution_Answer': a['resolution_answer'],
            'NextStep_Adventure': a['next_step'],
            'crew_loss': a['crew_loss'],
            'damage_ship': a['damage_ship'],
            'salud': a['salud'],
            'states': {}
        }

    cursor.close()
    conn.close()
    return result





# - - - CONSTRUIR DICCIONARIO DE LAS AVENTURA DISPO- - -
def build_adventures_dict():
    adventures_dict = {}

    # Abrir conexión
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Traer todas las aventuras
    cursor.execute("SELECT idAdventure, name, description FROM adventure")
    adventures_rows = cursor.fetchall()

    for row in adventures_rows:
        id_adv = row['idAdventure']

        # Traer personajes de esta aventura
        cursor.execute("""
                SELECT idCharacter FROM adventure_characters
                WHERE idAdventure = %s
            """, (id_adv,))
        chars = [r['idCharacter'] for r in cursor.fetchall()]

        # Traer estados de esta aventura
        cursor.execute("""
                SELECT idState FROM adventure_states
                WHERE idAdventure = %s
            """, (id_adv,))
        states = [r['idState'] for r in cursor.fetchall()]

        # Construir entrada del diccionario
        adventures_dict[id_adv] = {
            'Name': row['name'],  # Nota: Python es case-sensitive
            'Description': row['description'],
            'characters': chars,
            'states': states
        }

    # Cerrar cursor y conexión
    cursor.close()
    conn.close()

    return adventures_dict



def build_id_by_steps_dict():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Traer todos los pasos de todas las aventuras
    cursor.execute("""
        SELECT idStep, idAdventure, description, final_step
        FROM steps
    """)
    steps_rows = cursor.fetchall()

    # Diccionario final
    id_by_steps = {}

    for row in steps_rows:
        adv_id = row['idAdventure']
        step_id = row['idStep']
        if adv_id not in id_by_steps:
            id_by_steps[adv_id] = {}

        # Traer respuestas asociadas a este step
        cursor.execute("""
            SELECT idAnswer
            FROM answers
            WHERE idAdventure = %s AND idStep = %s
            ORDER BY idAnswer
        """, (adv_id, step_id))
        answers_rows = cursor.fetchall()
        answers_in_step = tuple(r['idAnswer'] for r in answers_rows)

        # Construir el diccionario del step
        id_by_steps[adv_id][step_id] = {
            'Description': row['description'],
            'answers_in_step': answers_in_step,
            'Final_Step': row['final_step']
        }

    cursor.close()
    conn.close()
    return id_by_steps





def getFormatedTable(queryTable, title=""):
    import textwrap

    MAX_WIDTH = 120
    headers = queryTable[0]
    rows = queryTable[1:]

    num_cols = len(headers)
    col_width = MAX_WIDTH // num_cols

    result = ""

    # ===== TITULO =====
    if title:
        result += "\n" + title.center(MAX_WIDTH, "=") + "\n"

    # ===== CABECERAS =====
    for header in headers:
        result += "{:<{w}}".format(header, w=col_width)
    result += "\n" + "*" * MAX_WIDTH + "\n\n"

    # ===== FILAS =====
    for row in rows:
        # Envolver texto de cada columna
        wrapped_cols = []
        max_lines = 0

        for col in row:
            wrapped = textwrap.wrap(str(col), col_width)
            wrapped_cols.append(wrapped)
            max_lines = max(max_lines, len(wrapped))

        # Imprimir linea a linea
        for i in range(max_lines):
            for col in wrapped_cols:
                if i < len(col):
                    result += "{:<{w}}".format(col[i], w=col_width)
                else:
                    result += " " * col_width
            result += "\n"

        result += "\n"

    return result










# =========================================================================
#                             VARIABLES SIMPLES
# =========================================================================
menu_logout = "\n" + "-".center(50,"-") +"\n"+"AVENTURA".center(50,"*") + "\n" + "-".center(50,"-") + "\n" + "1)Cerrar Sesión\n2)Jugar\n3)Rejugar Aventura\n4)Reportes\n5)Salir"
menu_report = "1)Respuestas más utilizadas\n2)Jugador que más veces ha jugado\n3)Aventuras jugadas por el jugador  \n4)Retroceder"
menu_principal = "\n" + "-".center(50,"-") +"\n"+"MENU PRINCIPAL".center(50,"*") + "\n" + "-".center(50,"-") + "\n" + "1)Crear Usuario\n2)Iniciar Sesión\n3)Salir\n"
inputOptText="\nElige tu opción: "
menu_creausu = "\n\n\n" + "-".center(50,"-") +"\n"+"CREACION USUARIO".center(50,"*") + "\n" + "-".center(50,"-")
menu_inises = "\n\n\n" + "-".center(50,"-") +"\n"+"INICIO SESION".center(50,"*") + "\n" + "-".center(50,"-")
menu_ch = "\n\n\n" + "-".center(50,"-") +"\n"+"SELECCIONA UN PERSONAJE".center(50,"*") + "\n" + "-".center(50,"-") + "\n"
cab_ch = "{:<5}{:>45}".format("ID","NOMBRE") + "\n" + "-".center(50,"-") + "\n"
menu_rep = "\n\n\n" + "-".center(160,"-") +"\n"+"REJUGAR AVENTURA".center(160,"*") + "\n" + "-".center(160,"-") + "\n"
cab_rep = "{:<15}{:<30}{:<25}{:<30}{:<60}".format("ID_JUEGO","FECHA_INICIO","USUARIO","NOMBRE_AVENTURA","NOMBRE_PERSONAJE") + "\n"
acabado = "-".center(50,"-") + "\n"
acabado_rep = "-".center(160,"-") + "\n"
dicc_ch_recu = {}
dicc_get_users = {}
dicc_get_adventures = {}
dicc_get_games = {}
dicc_get_choices = {}



def iniciar_sesion():
    print(menu_inises)
    usu = input("Introduce tu usuario: ")
    while not usu.isalnum() or usu == "":
        usu = input("Valor incorrecto, por favor introduce el nombre de usuario a crear: ")
    pwd = input("Introduce el password para acceder: ")
    while pwd == "" or pwd.count(" ") > 0:
        pwd = input("Valor incorrecto, por favor introduce el password para acceder. No puede contener espacios en blanco: ")
    if userExists(usu, pwd):
        login = usu
        return login
    else:
        print("El usuario y/o el password no son correctos.")
        input("Pulsa enter para volver al menú principal.")

def select_character():
    print(menu_ch+cab_ch)

def contiene_minus(pwd):
    for min in pwd:
        if min.islower():
            return True
    return False
def contiene_mayus(pwd):
    for may in pwd:
        if may.isupper():
            return True
    return False

def contiene_especial(pwd):
    for esp in pwd:
        if not esp.isalnum():
            return True
    return False

def checkPassword(password):
    while len(password) < 8 or len(password) > 12 or password.count(" ") > 0 or not contiene_minus(password) or not contiene_mayus(password) or not contiene_especial(password):
        print("El password debe tener una longitud comprendida entre 8 y 12 caracteres, alguna letra minúscula, alguna letra mayíscula y algún carácter especial.")
        return False
    return True

def checkUser(user):
    while len(user) < 6 or len(user) > 10 or user.count(" ") > 0 or not user.isalnum():
        print("El usuario debe tener una longitud comprendida entre 6 y 10 caracteres y ser alfanumérico.")
        return False
    return True

def checkUserbdd(usu,pwd):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    sql = "SELECT Username FROM user where Username = %s"
    cursor.execute(sql, (usu,))
    user_bbdd = cursor.fetchall()
    if not user_bbdd:
        return 0
    sql2 = "SELECT Username FROM user where Username = %s and Password = %s"
    cursor.execute(sql2, (usu, pwd))
    usu_pwd = cursor.fetchall()
    if not usu_pwd:
        return -1
    else:
        return 1

def userExists(usu, pwd=""):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    if pwd == "":
        sql = "SELECT Username FROM user where Username = %s"
        cursor.execute(sql, (usu,))
        usu_recu = cursor.fetchall()
        if not usu_recu:
            return True
        else:
            return False
    else:
        sql = "SELECT Username FROM user where Username = %s and Password = %s"
        cursor.execute(sql, (usu,pwd))
        usu_recu = cursor.fetchall()
        if not usu_recu:
            return False
        else:
            return True

def insertUser():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    print(menu_creausu)
    usu = input("Introduce el nombre de usuario a crear: ")
    while not checkUser(usu):
        usu = input("Por favor introduce el nombre de usuario a crear: ")
    # Revisamos si ya existe el usuario en BBDD:
    while userExists(usu) == False:
        usu = input("El usuario ya existe, por favor introduce uno diferente: ")
    print("Usuario disponible.\n")
    pwd = input("Crea el password para acceder: ")
    while not checkPassword(pwd):
        pwd = input("Por favor introduce el password de usuario a crear: ")
    sql = "INSERT INTO user (Username, Password) VALUES (%s, %s);"
    cursor.execute(sql, (usu, pwd))
    conn.commit()
    print("Se ha creado el nuevo usuario")
    input("Pulsa Enter para volver al menú principal")

def getUsers():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user")
    user_recu = cursor.fetchall()
    for usu in user_recu:
        dicc_get_users[usu["Username"]] = {"password": usu["Password"], "idUser":usu["idUser"]}
    return dicc_get_users
def getUserIds():
    getUsers()
    lista = [[],[]]
    for usuario in dicc_get_users:
        lista[0].append(usuario)
        lista[1].append(dicc_get_users[usuario]["idUser"])
    print(lista)

# def getOpt(textOpts="",inputOptText="",rangeList=[],dictionary={},exceptions=[]):
#     print(textOpts)
#     while True:
#         res = input(inputOptText)
#         try:
#             if res.isdigit():
#                 assert int(res) <= rangeList[-1], "El número introducido no es una opción válida\n\n"
#                 if rangeList.count(int(res)) >= 0:
#                  #   print("Accedemos a la opción -> {} de la lista ".format(res))
#                     return  int(res)
#             elif exceptions.count(res) > 0 or res == "-1":
#                 #print("Se ha escogido la opción -> {} de las excepciones ".format(res))
#                 return res
#             else:
#                 print("Res es = a {}".format(res))
#                 raise AssertionError("El valor introducido no es una opción válida\n\n")
#         except AssertionError as p:
#             print(p)
#             return p

#############################################
####### Volcar las tablas a diccionarios
#############################################
def getCharacters():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM characters")
    ch_recu = cursor.fetchall()
    for ch in ch_recu:
        dicc_ch_recu[ch["idCharacter"]] = ch["CharacterName"]
    return dicc_ch_recu

def getAdventures():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM adventure")
    adv_recu = cursor.fetchall()
    dicc_get_adventures = {}
    for adv in adv_recu:
        dicc_get_adventures[adv["idAdventure"]] = { "Name": adv["Name"], "Description": adv["Description"]}
    return dicc_get_adventures

def getGame_States_Master():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM game_states_master")
    gsm_recu = cursor.fetchall()
    dicc_get_gsm = {}
    for gsm in gsm_recu:
        dicc_get_gsm[gsm["idState"]] = { "Name": gsm["Name"], "initial_value": gsm["initial_value"]}
    return dicc_get_gsm

def getAdventure_States():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM adventure_states")
    advs_recu = cursor.fetchall()
    dicc_get_advs = {}
    for advs in advs_recu:
        dicc_get_advs[advs["idAdventure"]] = advs["idState"]
    return dicc_get_advs

def getAdventure_Context():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM adventure_context")
    advc_recu = cursor.fetchall()
    dicc_get_advc = {}
    for advc in advc_recu:
        dicc_get_advc[advc["idAdventure"]] = advc["context_text"]
    return dicc_get_advc

def getAnswers():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM answers")
    ans_recu = cursor.fetchall()
    dicc_get_ans = {}
    for ans in ans_recu:
        dicc_get_ans[ans["idAnswer"]] = { "idAdventure":ans["idAdventure"],"idStep":ans["idStep"],"description":ans["description"],"resolution_answer":ans["resolution_answer"],"crew_loss":ans["crew_loss"],"damage_ship":ans["damage_ship"],"salud":ans["salud"],"next_step":ans["next_step"]}
    return dicc_get_ans

def getAnswer_State_Effects():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM answer_state_effects")
    ase_recu = cursor.fetchall()
    dicc_get_ase = {}
    for ase in ase_recu:
        dicc_get_ase[ase["idAnswer"]] = { "idAdventure":ase["idAdventure"],"idState":ase["idState"],"value":ase["value"]}
    return dicc_get_ase

def getAnswer_Bysteps_Adventure():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM answers_bysteps_adventure")
    aba_recu = cursor.fetchall()
    dicc_get_aba = {}
    for aba in aba_recu:
        dicc_get_aba[aba["idAnswers_ByStep_Adventure"]] = { "idByStep_Adventure":aba["idByStep_Adventure"],"Description":aba["Description"],"Resolution_Answer":aba["Resolution_Answer"],"NextStep_Adventure":aba["NextStep_Adventure"]}
    return dicc_get_aba

def getByStep_Adventure():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM bystep_adventure")
    bsa_recu = cursor.fetchall()
    dicc_get_bsa = {}
    for bsa in bsa_recu:
        dicc_get_bsa[bsa["idByStep_Adventure"]] = {"idAdventure": bsa["idAdventure"], "Description": bsa["Description"], "Final_Step": bsa["Final_Step"]}
    return dicc_get_bsa

def getGame():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM game")
    game_recu = cursor.fetchall()
    dicc_get_game = {}
    for game in game_recu:
        dicc_get_game[game["idGame"]] = {"idUser": game["idUser"], "idCharacter": game["idCharacter"],"idAdventure": game["idAdventure"],"date": game["date"]}
    return dicc_get_game

def getSteps():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM steps")
    steps_recu = cursor.fetchall()
    dicc_get_steps = {}
    for steps in steps_recu:
        dicc_get_steps[steps["idStep"]] = {"idAdventure": steps["idAdventure"], "description": steps["description"],"final_step": steps["final_step"]}
    return dicc_get_steps

def getReplay_Adventures():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM replay_adventures")
    rep_recu = cursor.fetchall()
    dicc_get_rep = {}
    for rep in rep_recu:
        dicc_get_rep[rep["idReplay"]] = {"idUser": rep["idUser"],"idAdventure": rep["idAdventure"],"idCharacter": rep["idCharacter"], "adventure_name": rep["adventure_name"],"character_name": rep["character_name"]}
    return dicc_get_rep

def getUser():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user")
    user_recu = cursor.fetchall()
    dicc_get_user = {}
    for user in user_recu:
        dicc_get_user[user["idUser"]] = { "Username": user["Username"], "Password": user["Password"]}
    return dicc_get_user

def getIdUserByName(login):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    sql = "SELECT idUser FROM user where Username = %s"
    cursor.execute(sql, (login,))
    usu_recu = cursor.fetchall()
    return usu_recu[0]["idUser"]

def getLastIdGame():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT idGame FROM game ORDER BY idGame DESC LIMIT 1")
    id_game = cursor.fetchall()
    return id_game[0]["idGame"]

def insertChoice(current, id_decision):
    id_game = getLastIdGame()
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    sql = "INSERT INTO choices (idGame, currentStep, idDecision) VALUES (%s, %s, %s);"
    cursor.execute(sql, (id_game,current, id_decision))
    conn.commit()

def replay():
    datos = ""
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""select g.idGame, g.date, u.Username, a.Name, c.CharacterName
    from game g, user u, adventure a, characters c
    where g.idUser = u.idUser
    and g.idCharacter = c.idCharacter
    and g.idAdventure = a.idAdventure
    order by idGame asc;""")
    replay_list = cursor.fetchall()
    for rep in replay_list:
        datos = datos + "{:<15}{:<30}{:<25}{:<30}{:<60}".format(rep["idGame"], str(rep["date"]), rep["Username"], rep["Name"], rep["CharacterName"]) + "\n"
    tabla_replay = menu_rep+cab_rep+acabado_rep+datos+acabado_rep
    print(tabla_replay)
    return replay_list

def recuDatosReplay(idGame):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    sql = """select st.idStep, st.description, ans.idAnswer, ans.description, ans.resolution_answer
    FROM steps st, answers ans, choices ch, game g
    where ans.idStep = st.idStep
    AND ans.idAdventure = st.idAdventure
    and ans.idAdventure = g.idAdventure
    and g.idGame = ch.idGame
    and ch.currentStep = st.idStep
    and ch.idGame = %s
    and ch.idDecision = ans.idAnswer
    ORDER BY ans.idAnswer;"""
    cursor.execute(sql, (idGame,))
    datos_replay_list = cursor.fetchall()
    if aventuraPorJuego(idGame) == 1:
        for datrep in datos_replay_list:
            print("Paso elegido: {:<60}\nRespuesta: {:<60}\n".format(datrep["description"],datrep["resolution_answer"]))
            input("")
        print("FIN")
        input("Pulsa Enter para seguir.")
    return datos_replay_list


def aventuraPorJuego(idGame):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    sql = "Select a.description, a.name from game g, adventure a where g.idGame = %s and g.idAdventure = a.idAdventure"
    cursor.execute(sql, (idGame,))
    recu_cod_adv = cursor.fetchall()
    if recu_cod_adv != []:
        print("\nLa aventura que vamos a revivir es la de {}:\n{}\nA continuación reviviremos las elecciones elegidas pulsando Enter:\n".format(recu_cod_adv[0]["name"], recu_cod_adv[0]["description"]))
        return 1
    else:
        print("La opción escogida es incorrecta")
        input("Pulsa Enter para seguir.")
        return 0


def get_most_used_answers_per_adventure(limit=6):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    sql = """
    SELECT
        s.idAdventure,
        adv.Name AS adventure_name,
        s.idStep,
        s.description AS step_description,
        a.idAnswer,
        a.description AS answer_description,
        COUNT(*) AS times_selected
    FROM choices c
    JOIN answers a
        ON a.idAnswer = c.idDecision
    JOIN steps s
        ON s.idStep = c.currentStep
    JOIN adventure adv
        ON adv.idAdventure = s.idAdventure
    GROUP BY 
        s.idAdventure, adv.Name, s.idStep, s.description, a.idAnswer, a.description
    ORDER BY times_selected DESC
    LIMIT %s;
    """
    cursor.execute(sql, (limit,))
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows



def print_most_used_answers(rows):
    # Anchos de columnas más grandes para mayor separación
    width_adventure = 35
    width_step = 40
    width_answer = 30
    width_times = 5

    titulo = "Respuestas más utilizadas"
    print("=" * 160 + "\n" + titulo.center(160) + "\n" + "=" * 160)

    # Cabecera
    print(
        "{:<35}{:<50}{:<50}{:<5}".format("ID AVENTURA - NOMBRE", "ID PASO - DESCRIPCIÓN", "ID RESPUESTA - DESCRIPCIÓN","NUMERO VECES SELECCIONADA") + "\n" + "*" * 160)

    for row in rows:
        # Dividir el texto largo en varias líneas
        step_lines = textwrap.wrap(row['step_description'], width_step)
        answer_lines = textwrap.wrap(row['answer_description'], width_answer)

        # Determinar cuántas líneas necesitamos imprimir
        num_step_lines = len(step_lines)
        num_answer_lines = len(answer_lines)

        # Recorremos desde 0 hasta el número máximo de líneas manualmente
        i = 0
        while i < num_step_lines or i < num_answer_lines:
            # Mostrar ID solo en la primera línea del bloque
            if i == 0:
                adventure_text = "{} - {}".format(row['idAdventure'], row['adventure_name'])
                times_text = str(row['times_selected'])
                step_text = "{} - {}".format(row['idStep'], step_lines[i]) if i < num_step_lines else ""
                answer_text = "{} - {}".format(row['idAnswer'], answer_lines[i]) if i < num_answer_lines else ""
            else:
                adventure_text = ""
                times_text = ""
                step_text = step_lines[i] if i < num_step_lines else ""
                answer_text = answer_lines[i] if i < num_answer_lines else ""

            print("{:<35}{:<50}{:<50}{:<5}".format(adventure_text,step_text, answer_text,times_text))
            i += 1

        # Salto de línea entre bloques
        print()

    input("\nPresiona ENTER para continuar...\n")
