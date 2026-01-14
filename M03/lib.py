import sys

import mysql.connector
from _mysql_connector import MySQLInterfaceError
from mysql.connector import DatabaseError

#Definición literales
menu0 = "\n" + "-".center(50,"-") +"\n"+"MENU PRINCIPAL".center(50,"*") + "\n" + "-".center(50,"-") + "\n" + "1)Crear Usuario\n2)Iniciar Sesión\n3)Mostrar aventuras\n4)Salir\n"
inputOptText="\nElige tu opción: "
menu_creausu = "\n\n\n" + "-".center(50,"-") +"\n"+"CREACION USUARIO".center(50,"*") + "\n" + "-".center(50,"-")
menu_inises = "\n\n\n" + "-".center(50,"-") +"\n"+"INICIO SESION".center(50,"*") + "\n" + "-".center(50,"-")
menu_pj = "\n\n\n" + "-".center(50,"-") +"\n"+"SELECCIONA UN PERSONAJE".center(50,"*") + "\n" + "-".center(50,"-") + "\n"
cab_pj = "{:<5}{:>45}".format("ID","NOMBRE") + "\n" + "-".center(50,"-") + "\n"
acabado = "-".center(50,"-") + "\n"
datos = ""

#Definición variables
login = ""
dicc_pj_recu = {}
dicc_get_users = {}

#Definición funciones
def conectar_bbdd():
    try:
        global cursor
        global conn
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="proyectobjr",
            database="proyecto_bjr",
            port=3306
        )
        cursor = conn.cursor(dictionary=True)  # resultados como dict
        print("\nSe ha conectado correctamente a la Base de datos.")
        return 1
    except MySQLInterfaceError as e:
        print("\nSe ha producido un error al conectar con la Base de datos.")
        sys.exit()
    except DatabaseError as e2:
        print("\nSe ha producido un error al conectar con la Base de datos.")
        sys.exit()
    finally:
        print("")

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
        input("Pulsa enter para continuar")

def select_character():
    print(menu_pj+cab_pj)

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

def getCharacters():
    datos = ""
    cursor.execute("SELECT * FROM characters")
    pj_recu = cursor.fetchall()
    for pj in pj_recu:
        datos = datos + "{:<5}{:>45}".format(pj["idCharacter"], pj["CharacterName"]) + "\n"
        dicc_pj_recu[pj["idCharacter"]] = pj["CharacterName"]
    print(menu_pj+cab_pj+datos+acabado)
    print(dicc_pj_recu)

def checkUserbdd(usu,pwd):
    conectar_bbdd()
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
    print(menu_creausu)
    usu = input("Introduce el nombre de usuario a crear: ")
    while not checkUser(usu):
        usu = input("Por favor introduce el nombre de usuario a crear: ")
    # Revisamos si ya existe el usuario en BBDD:
    while userExists(usu) == False:
        usu = input("El usuario ya existe, por favor introduce uno diferente: ")
    print("Usuario disponible.\n")
    pwd = input("Crea el password para acceder: ")
    if checkPassword(pwd):
        sql = "INSERT INTO user (Username, Password) VALUES (%s);"
        cursor.execute(sql, (usu, pwd))
        conn.commit()
        print("Se ha creado el nuevo usuario")

def getUsers():
    conectar_bbdd()
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

def getOpt(textOpts="",inputOptText="",rangeList=[],dictionary={},exceptions=[]):
    print(textOpts)
    while True:
        res = input(inputOptText)
        try:
            if res.isdigit():
                assert int(res) <= rangeList[-1], "El número introducido no es una opción válida\n\n"
                if rangeList.count(int(res)) >= 0:
                 #   print("Accedemos a la opción -> {} de la lista ".format(res))
                    return  int(res)
            elif exceptions.count(res) > 0 or res == "-1":
                #print("Se ha escogido la opción -> {} de las excepciones ".format(res))
                return res
            else:
                print("Res es = a {}".format(res))
                raise AssertionError("El valor introducido no es una opción válida\n\n")
        except AssertionError as p:
            print(p)
            return p