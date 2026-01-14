from conexion_bbdd import *
from lib import *

#programa principal
conectar_bbdd()

flg_0 = True
while flg_0:
    opc = getOpt(menu0,inputOptText,[1,2,3,4], exceptions=['w','e',-1])
    print(type(opc))
    input("stop")
    if type(opc) == "int":
        input("Valor introducido no numérico, introduzca un valor correcto. Presione Enter para continuar\n\n")
        continue
    elif opc.isdigit() and int(opc) < 1 or int(opc) > 4:
        input("Introduzca un valor correcto. Presione Enter para continuar\n\n")
        continue
    else:
        opc = int(opc)
        if opc == 1:
            insertUser()
        elif opc == 2:
            print("Has realizado el login correctamente, bienvenido {}\n".format(iniciar_sesion()))
            input("Pulsa enter para continuar")
            getCharacters()
            opc = input("Opción -> ")
            if not opc.isdigit():
                input(
                    "Valor introducido no numérico, introduzca un valor correcto. Presione Enter para continuar\n\n")
                continue
            elif opc.isdigit() and int(opc)+1 < 1 or int(opc)+1 > len(getCharacters()):
                input("Introduzca un valor correcto. Presione Enter para continuar\n\n")
                continue
            else:
                opc = int(opc) +1
                print("Has seleccionado el personaje {}".format(dicc_pj_recu[opc]["CharacterName"]))
        elif opc == 3:
            #TODO
             print("Por hacer")
        elif opc == 4:
            flg_0 = False