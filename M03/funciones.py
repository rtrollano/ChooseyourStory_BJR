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
# Diccionario adventures
# =======================
adventures = {
    1: {'Name': 'Expedición al Sector Z-47',
        'Description': 'Una peligrosa misión espacial con decisiones críticas y encuentros inesperados.',
        'characters': [1, 2, 3,4,5], 'states': [1,2]},
    2: {'Name': 'Las cartas anónimas',
        'Description': 'En un pequeño pueblo marcado por el silencio y las viejas lealtades, un suceso inesperado despierta\nsecretos enterrados durante años y obliga a enfrentar decisiones del pasado que nunca llegaron a saldarse.',
        'characters': [6,7,8,9], 'states': []}
}

# =======================
# Diccionario characters
# =======================
# characters = {
#     1: 'Capitán: Shelton',
#     2: 'Ingeniero Jefe: Ramirez',
#     3: 'Médico de la Nave: Tanaka',
#     4: 'Especialista en Comunicaciones: Kane',
#     5: 'Médico de Vuelo: Patel',
#     6: 'Adrián Lozano – técnico municipal',
#     7: 'Valeria Méndez – Informática',
#     8: 'Héctor Sosa – gestor agrícola',
#     9: 'Isabel Fuentes – trabajadora social',
#     10: 'Óscar Beltrán – periodista local',
#     11: 'Camila Duarte – farmacéutica'
# }


# =======================
# States
# =======================
game_states_master = {
    1: {'name': 'nave', 'initial': 5},          # Para juego espacial
    2: {'name': 'tripulacion', 'initial': 5},  # Para juego espacial
          # Para juego de misterio
}

# ===========================
# Contexto de cada aventura
# ===========================

adventure_context = {
    1: "Tras años de exhaustiva preparación, cinco tripulantes de la Base Helios se disponen a embarcarse en una misión sin precedentes:\nexplorar el sector Z-47, una región del espacio jamás cartografiada.\nLos estudios preliminares sugieren que se trata de una zona rica en recursos energéticos capaces de transformar para siempre la forma en que la Tierra produce y utiliza la energía.\nConfiados en el éxito de la expedición y en la solidez de su entrenamiento,\nla nave Astraeon despega sin incidentes, adentrándose en lo desconocido…",

    2: "Todo comienza un martes de abril, a las dos de la madrugada, en Eldralva, un pueblo aislado de apenas setecientos habitantes.\nRodeado de campos y antiguas explotaciones agrícolas, es un lugar donde todos se conocen, los silencios pesan más que las palabras y el pasado nunca termina de desaparecer.",
}



# =======================
# Diccionario idAnswers_ByStep_Adventure
# =======================
# idAnswers_ByStep_Adventure = {
#     1:{
#         # ----- Decisión 1: Ruido extraño -----
#         (1, 1): {'Description': 'Enviar al ingeniero al exterior de la nave para investigar el origen del ruido.',
#                  'Resolution_Answer': 'El mecánico localiza una placa suelta antes de que cause daños mayores y refuerza la zona.','crew_loss': 0, 'damage_ship': 0, 'NextStep_Adventure': 2},
#         (2, 1): {'Description': 'Enviar al ingeniero al exterior de la nave para investigar el origen del ruido.',
#                  'Resolution_Answer': 'Durante la reparación, una pieza se desplaza bruscamente y le atrapa la mano al ingeniero del equipo, dejándole la mano gravemente herida. Tripulación -2','crew_loss': 2, 'damage_ship': 0, 'NextStep_Adventure': 2},
#         (3, 1): {'Description': 'Ignorar el ruido y continuar el viaje confiando en que no sea grave.',
#                  'Resolution_Answer': 'El fallo resulta ser menor y no vuelve a manifestarse durante el trayecto.','crew_loss': 0, 'damage_ship': 0, 'NextStep_Adventure': 2},
#         (4, 1): {'Description': 'Ignorar el ruido y continuar el viaje confiando en que no sea grave.',
#                  'Resolution_Answer': 'El problema se agrava con el tiempo y provoca una pequeña fuga de combustible. Nave -2','crew_loss': 0, 'damage_ship': 2, 'NextStep_Adventure': 2},
#
#         # ----- Decisión 2: Aterrizar en planeta -----
#         (5, 2): {'Description': 'Aterrizar en un planeta cercano para revisar sistemas y permitir que la tripulación descanse.',
#                  'Resolution_Answer': 'El aterrizaje es estable y el entorno resulta seguro.', 'crew_loss': 0, 'damage_ship': 0,'NextStep_Adventure': 3},
#         (6, 2): {'Description': 'Aterrizar en un planeta cercano para revisar sistemas y permitir que la tripulación descanse.',
#                  'Resolution_Answer': 'El terreno es muy inestable; la nave sufre daños y un tripulante resulta herido durante el descenso. Tripulación -1. Nave -3','crew_loss': 1, 'damage_ship': 2, 'NextStep_Adventure': 3},
#         (7, 2): {'Description': 'Continuar el viaje sin desviarse para no perder tiempo.',
#                  'Resolution_Answer': 'Avanzan según lo previsto sin incidentes inmediatos.', 'crew_loss': 0, 'damage_ship': 0, 'NextStep_Adventure': 5},
#         (8, 2): {'Description': 'Continuar el viaje sin desviarse para no perder tiempo.',
#                  'Resolution_Answer': 'Un desperfecto menor en el motor se intensifica por el exceso de calor generado tras un vuelo prolongado.. Nave -2', 'crew_loss': 0, 'damage_ship': 2, 'NextStep_Adventure': 5},
#
#         # ----- Decisión 3: Encuentro con alienígenas -----
#         (9, 3): {'Description': 'Intentar comunicarse y confiar en los seres alienígenas.',
#                  'Resolution_Answer': 'Los alienígenas comparten tecnología que mejora el rendimiento de la nave. Nave +3','crew_loss': 0, 'damage_ship': -3, 'NextStep_Adventure': 4},
#         (10, 3): {'Description': 'Intentar comunicarse y confiar en los seres alienígenas.',
#                   'Resolution_Answer': 'Un malentendido provoca un ataque a distancia por parte de los alienígenas con una tecnologia extraña que hiere a uno de los tripulante. Tripulación -2','crew_loss': 2, 'damage_ship': 0, 'NextStep_Adventure': 4},
#         (11, 3): {'Description': 'Retirarse con cautela y evitar cualquier contacto.',
#                   'Resolution_Answer': 'La tripulación evita posibles riesgos y continúa el viaje.', 'crew_loss': 0,'damage_ship': 0, 'NextStep_Adventure': 5},
#         (12, 3): {'Description': 'Retirarse con cautela y evitar cualquier contacto.',
#                   'Resolution_Answer': 'Los alienígenas interpretan la retirada como hostilidad y atacan brevemente la nave. Nave -1','crew_loss': 0, 'damage_ship': 1, 'NextStep_Adventure': 5},
#
#         # ----- Decisión 4: Pacto con alienígenas -----
#         (13, 4): {'Description': 'Ceder parte de los recursos para mantener la paz.',
#                   'Resolution_Answer': 'La relación se fortalece y los alienígenas prometen no interferir en su camíno.', 'crew_loss': 0, 'damage_ship': 0, 'NextStep_Adventure': 5},
#         (14, 4): {'Description': 'Ceder parte de los recursos para mantener la paz.',
#                   'Resolution_Answer': 'El capitán entrega un recurso clave para evitar el conflicto con los alienígenas.\nLa decisión deja una sensación de duda en la tripulación y debilita la confianza del equipo. Tripulación -1', 'crew_loss': 1, 'damage_ship': 0, 'NextStep_Adventure': 5},
#         (15, 4): {'Description': 'Negarse a ceder recursos y mantener una postura firme.',
#                   'Resolution_Answer': 'Al percibir la determinación de la tripulación, los alienígenas optan por retirarse, evitando un conflicto directo.','crew_loss': 0, 'damage_ship': 0, 'NextStep_Adventure': 5},
#         (16, 4): {'Description': 'Negarse a ceder recursos y mantener una postura firme.',
#                   'Resolution_Answer': 'La negativa provoca represalias que dañan la nave y a la tripulación. Tripulación -1, Nave -3','crew_loss': 1, 'damage_ship': 3, 'NextStep_Adventure': 5},
#
#         # ----- Decisión 5: Hallazgo extraño -----
#         (17, 5): {'Description': 'Recoger el mineral brillante para analizarlo.',
#                   'Resolution_Answer': 'El mineral resulta ser una fuente energética útil que aumenta la capacidad de los sistemas de la nave,\nproporcionándole una estabilidad jamás registrada en una nave de esas características. Nave +10','crew_loss': 0, 'damage_ship': -10, 'NextStep_Adventure': 6},
#         (18, 5): {'Description': 'Recoger el mineral brillante para analizarlo.',
#                   'Resolution_Answer': 'El mineral emite toxinas que afectan con fuerza al capitán de la tripulación. Tripulación -2','crew_loss': 2, 'damage_ship': 0, 'NextStep_Adventure': 6},
#         (19, 5): {'Description': 'Ignorar el mineral y no interferir.',
#                   'Resolution_Answer': 'Evitan cualquier riesgo innecesario.', 'crew_loss': 0, 'damage_ship': 0,'NextStep_Adventure': 6},
#         (20, 5): {'Description': 'Ignorar el mineral y no interferir.',
#                   'Resolution_Answer': 'El capitán decide finalmente ignorar el mineral y no asumir riesgos.\nParte de la tripulación, en desacuerdo, inicia una trifulca verbal y física que deja una profunda brecha en la confianza y la lealtad dentro del equipo. Tripulación -2','crew_loss': 2, 'damage_ship': 0, 'NextStep_Adventure': 6},
#
#         # ----- Decisión 6: Revisión de combustible -----
#         (21, 6): {'Description': 'Revisar cuidadosamente el sistema de combustible.',
#                   'Resolution_Answer': 'Se detecta una fuga menor antes de que sea crítica.', 'crew_loss': 0,'damage_ship': 0, 'NextStep_Adventure': 7},
#         (22, 6): {'Description': 'Revisar cuidadosamente el sistema de combustible.',
#                   'Resolution_Answer': 'Un descuido durante la revisión provoca un accidente grave en una sección del motor, poniendo en riesgo toda la nave. Nave -2','crew_loss': 0, 'damage_ship': 2, 'NextStep_Adventure': 7},
#         (23, 6): {'Description': 'Continuar sin revisar para ahorrar tiempo.',
#                   'Resolution_Answer': 'El sistema aguanta y sufre desgaste casi imperceptible.', 'crew_loss': 0,'damage_ship': 0, 'NextStep_Adventure': 7},
#         (24, 6): {'Description': 'Continuar sin revisar para ahorrar tiempo.',
#                   'Resolution_Answer': 'El sistema de combustible sufre un fallo crítico, obligando al equipo a realizar una reparación parcial, bajo condiciones extremadamente difíciles. Tripulación -1, Nave -3','crew_loss': 1, 'damage_ship': 3, 'NextStep_Adventure': 7},
#
#         # ----- Decisión 7: Tormenta inesperada -----
#         (25, 7): {'Description': 'Realizar maniobras agresivas para atravesar la tormenta.',
#                   'Resolution_Answer': 'Las maniobras permiten atravesar la tormenta más rápido de lo previsto, reduciendo la exposición y salvando a la nave de daños mayores.\nEste hecho logra levantar el ánimo de la tripulación en un momento crítico. Tripulación +1','crew_loss': -1, 'damage_ship': 0, 'NextStep_Adventure': 8},
#         (26, 7): {'Description': 'Realizar maniobras agresivas para atravesar la tormenta.',
#                   'Resolution_Answer': 'Las maniobras sobrecargan los sistemas de control, causando daños estructurales que agravan aún más la situación de la nave. Nave -2','crew_loss': 0, 'damage_ship': 2, 'NextStep_Adventure': 8},
#         (27, 7): {'Description': 'Buscar una ruta más segura alrededor de la tormenta.',
#                   'Resolution_Answer': 'Evitais el peligro directo y conseguis no augmentar el desgaste de la nave.','crew_loss': 0, 'damage_ship': 0, 'NextStep_Adventure': 8},
#         (28, 7): {'Description': 'Buscar una ruta más segura alrededor de la tormenta.',
#                   'Resolution_Answer': 'Logran evitar el peligro directo, pero durante las maniobras de evasión de la tormenta consumen más combustible del previsto. Nave -2','crew_loss': 0, 'damage_ship': 2, 'NextStep_Adventure': 8},
#
#         # ----- Decisión 8: Reparación crítica -----
#
#         (29, 8): {'Description': 'Usar materiales obtenidos de los alienígenas para la reparación.',
#                   'Resolution_Answer': 'La nave queda reforzada. Nave +2', 'crew_loss': 0, 'damage_ship': -2,'NextStep_Adventure': 9},
#         (30, 8): {'Description': 'Usar materiales obtenidos de los alienígenas para la reparación.',
#                   'Resolution_Answer': 'La tecnología no es compatible y la reparación no se puede completar.','crew_loss': 0, 'damage_ship': 0, 'NextStep_Adventure': 9},
#         (31, 8): {'Description': 'Reparar con el equipo estándar de la nave.',
#                   'Resolution_Answer': 'La reparación es estable y se realiza con éxito. Nave +2', 'crew_loss': 0,'damage_ship': -2, 'NextStep_Adventure': 9},
#         (32, 8): {'Description': 'Reparar con el equipo estándar de la nave.',
#                   'Resolution_Answer': 'Un error provoca un accidente leve en el motor secundario de la nave. Nave -1','crew_loss': 0, 'damage_ship': 1, 'NextStep_Adventure': 9},
#
#         # ----- Decisión 9: Explorar caverna luminosa -----
#         (33, 9): {'Description': 'Explorar la caverna luminosa.',
#                   'Resolution_Answer': 'El hallazgo de cristales energéticos abre nuevas posibilidades y podría tener un impacto decisivo en el futuro.','crew_loss': 0, 'damage_ship': 0, 'NextStep_Adventure': 11},
#         (34, 9): {'Description': 'Explorar la caverna luminosa.',
#                   'Resolution_Answer': 'Un derrumbe repentino bloquea la salida principal de la caverna, dejando a parte del equipo atrapado en su interior.','crew_loss': 0, 'damage_ship': 0, 'NextStep_Adventure': 10},
#         (35, 9): {'Description': 'Continuar sin explorar.',
#                   'Resolution_Answer': 'Evitan riesgos innecesarios y continúan la ruta hacia otra zona más al norte.','crew_loss': 0, 'damage_ship': 0, 'NextStep_Adventure': 11},
#         (36, 9): {'Description': 'Continuar sin explorar.',
#                   'Resolution_Answer': 'La decisión genera frustración, pero el capitán prioriza la exploración de una zona situada más al sur.','crew_loss': 0, 'damage_ship': 0, 'NextStep_Adventure': 11},
#
#         # ----- Decisión 10: Crisis de oxígeno -----
#         (37, 10): {'Description': 'Ir en busca de recambios de oxígeno e intentar hacerlos llegar a la tripulación atrapada entre las runas.',
#                    'Resolution_Answer': 'El oxígeno llega a tiempo y la tripulación atrapada logra resistir hasta ser rescatada.','crew_loss': 0, 'damage_ship': 0, 'NextStep_Adventure': 12},
#         (38, 10): {'Description': 'Ir en busca de recambios de oxígeno e intentar hacerlos llegar a la tripulación atrapada entre las runas.',
#                    'Resolution_Answer': 'Parte del equipo sufre agotamiento o heridas durante el traslado del oxígeno. Tripulación -3','crew_loss': 3, 'damage_ship': 0, 'NextStep_Adventure': 12},
#         (39, 10): {'Description': 'Confiar en que el nivel de oxígeno sea suficiente, dando prioridad a la movilización de la runa',
#                    'Resolution_Answer': 'La runa se moviliza con éxito y permite liberar a la tripulación antes de que el oxígeno se agote.\nEl éxito refuerza la confianza en la misión. Tripulación +1','crew_loss': 1, 'damage_ship': 0, 'NextStep_Adventure': 12},
#         (40, 10): {'Description': 'Confiar en el sistema automático.',
#                    'Resolution_Answer': 'El sistema falla gravemente.', 'crew_loss': 1, 'damage_ship': 2,'NextStep_Adventure': 12},
#
#         # ----- Decisión 11: Señal desconocida -----
#         (41, 11): {'Description': 'Responder a la señal misteriosa recibida por la nave.',
#                    'Resolution_Answer': 'La señal proviene de una inteligencia amistosa que proporciona coordenadas para obtener recursos valiosos. Nave +1, Tripulación +1.','crew_loss': -1, 'damage_ship': -1, 'NextStep_Adventure': 12},
#         (42, 11): {'Description': 'Responder a la señal misteriosa recibida por la nave.',
#                    'Resolution_Answer': 'La señal era una trampa: se activa una interferencia que daña parcialmente los sistemas de comunicación. Nave -1,','crew_loss': 0, 'damage_ship': -1, 'NextStep_Adventure': 12},
#         (43, 11): {'Description': 'Analizar la señal sin responder, estudiando su origen desde lejos.',
#                    'Resolution_Answer': 'La información obtenida permite anticipar riesgos futuros y optimizar la ruta de la nave.','crew_loss': 0, 'damage_ship': 0, 'NextStep_Adventure': 12},
#         (44, 11): {'Description': 'Analizar la señal sin responder, estudiando su origen desde lejos.',
#                    'Resolution_Answer': 'Se evita cualquier posible trampa y se enfocan en el siguiente paso de la misión.','crew_loss': 0, 'damage_ship': 0, 'NextStep_Adventure': 12},
#
#         # ----- Decisión 12: Final de la misión -----
#         (45, 12): {'Description': 'Abortar misión.', 'Resolution_Answer': 'Deciden abortar la misión y girar la nave de regreso hacia la Tierra.\nAunque sienten la decepción de no haber completado la expedición, todos los sistemas permanecen estables y la tripulación llega sana y salva.\nTras regresar a su base, pueden planear futuras aventuras con más experiencia y precaución.', 'crew_loss': 0, 'damage_ship': 0, 'NextStep_Adventure': None},
#         (46, 12): {'Description': 'Abortar misión.', 'Resolution_Answer': 'De regreso a la Tierra, la nave atraviesa inesperadamente una lluvia de meteoritos.\nLos escudos apenas resisten y cada impacto sacude la nave con violencia, provocando fallos en los sistemas vitales.\nFinalmente, la nave queda convertida a cenizas, y la tripulación sobrevive solo en los recuerdos de lo que pudo haber sido.', 'crew_loss': 0, 'damage_ship': 0, 'NextStep_Adventure': None},
#         (47, 12): {'Description': 'Continuar misión.', 'Resolution_Answer': 'Tras explorar los confines del espacio, la tripulación logra recuperar un mineral o tecnología alienígena de gran valor.\nAunque algunos miembros presentan pequeñas heridas, la nave permanece intacta.\nLa misión culmina con éxito parcial, y el hallazgo es celebrado por científicos y líderes de la expedición.', 'crew_loss': 0, 'damage_ship': 0, 'NextStep_Adventure': None},
#         (48, 12): {'Description': 'Continuar misión.', 'Resolution_Answer': 'Una serie de accidentes críticos destruye la nave por completo mientras la tripulación lucha por sobrevivir.\nLamentablemente, nadie sobrevive a la misión y la nave queda irreparable.\nLa historia concluye como una tragedia que sirve de advertencia sobre los peligros del espacio y los riesgos de la exploración.', 'crew_loss': 0, 'damage_ship': 0, 'NextStep_Adventure': None}
#     },



#     2: {
#
#         # ----- Decisión 1: Explosión del local -----
#         (1, 1): {'Description': 'Investigar personalmente los restos del local para intentar averiguar el origen de la explosión.',
#                  'Resolution_Answer': 'Mientras inspeccionas el lugar, descubres una habitación oculta llena de documentación parcialmente quemada.','Protagonista': 0, 'NextStep_Adventure': 2},
#         (2, 1): { 'Description': 'Investigar personalmente los restos del local para intentar averiguar el origen de la explosión.',
#                   'Resolution_Answer': 'Documentas el lugar sin incidentes, pero no encuentras nada concluyente antes de escuchar las sirenas de la policía acercándose.','Protagonista': 0, 'NextStep_Adventure': 3},
#         (3, 1): {'Description': 'Avisar a las autoridades para que se hagan cargo de la investigación.',
#                  'Resolution_Answer': 'La policía acordona la zona y limita tu acceso, pero al hablar con los vecinos surgen rumores sobre enfermedades extrañas tras el cierre del local.','Protagonista': 0, 'NextStep_Adventure': 3},
#         (4, 1): {'Description': 'Avisar a las autoridades para que se hagan cargo de la investigación.',
#                  'Resolution_Answer': 'Las autoridades controlan la situación y el asunto se enfría rápidamente, aunque algunos vecinos muestran un nerviosismo evidente.','Protagonista': 0, 'NextStep_Adventure': 3},
#
#         # Paso 2: La documentación encontrada
#         (5, 2): {'Description': 'Revisar la documentación encontrada antes de que alguien más llegue al lugar.',
#                  'Resolution_Answer': 'Entre los papeles aparecen nombres, fechas y referencias a envíos poco claros.', 'Protagonista': 0, 'NextStep_Adventure': 4},
#         (6, 2): {'Description': 'Revisar la documentación encontrada antes de que alguien más llegue al lugar.',
#                  'Resolution_Answer': 'La mayoría de documentos están demasiado dañados para sacar conclusiones claras.', 'Protagonista': 0, 'NextStep_Adventure': 3},
#         (7, 2): {'Description': 'Guardar la documentación sin revisarla y abandonar el lugar.',
#                  'Resolution_Answer': 'Decides no arriesgarte y marcharte, pero la duda empieza a crecer.','Protagonista': 0, 'NextStep_Adventure': 5},
#         (8, 2): {'Description': 'Guardar la documentación sin revisarla y abandonar el lugar.',
#                  'Resolution_Answer': 'Al salir apresuradamente, pierdes parte del material sin darte cuenta.', 'Protagonista': 0, 'NextStep_Adventure': 3},
#
#         # Paso 3 Primeras sospechas en el pueblo
#         (9, 3): {'Description': 'Hablar con vecinos que vivieron el cierre del negocio.',
#                  'Resolution_Answer': 'Algunos vecinos mencionan rumores sobre enfermedades inexplicables y acuerdos de silencio que tuvieron lugar años atrás.','Protagonista': 0, 'NextStep_Adventure': 4},
#         (10, 3): {'Description': 'Hablar con vecinos que vivieron el cierre del negocio.',
#                   'Resolution_Answer': 'La mayoría evita el tema o finge no recordar nada.', 'Protagonista': 0,'NextStep_Adventure': 4},
#         (11, 3): {'Description': 'Observar discretamente el ambiente del pueblo sin intervenir.',
#                   'Resolution_Answer': 'Notas nerviosismo en ciertas familias relacionadas con el antiguo local.','Protagonista': 0, 'NextStep_Adventure': 4},
#         (12, 3): {'Description': 'Observar discretamente el ambiente del pueblo sin intervenir.',
#                   'Resolution_Answer': 'No detectas nada fuera de lo normal y pierdes tiempo valioso.','Protagonista': 0, 'NextStep_Adventure': 4},
#
#         # Paso 4: Primer paquete misterioso
#         (13, 4): {'Description': 'Abrir el paquete y examinar su contenido.',
#                   'Resolution_Answer': 'Encuentras informes médicos antiguos y documentos antiguos que sugieren sin gran claridad que alguien encubrio esos informes para esconder la verdad.', 'Protagonista': 0, 'NextStep_Adventure': 5},
#         (14, 4): {'Description': 'Abrir el paquete y examinar su contenido.',
#                   'Resolution_Answer': 'Los documentos son confusos y difíciles de interpretar.', 'Protagonista': 0, 'NextStep_Adventure': 5},
#         (15, 4): {'Description': 'Guardar el paquete sin abrirlo.',
#                   'Resolution_Answer': 'Prefieres no implicarte todavía, pero la tensión aumenta, así que decides salir a dar una vuelta para calmar los nérvios.', 'Protagonista': 0, 'NextStep_Adventure': 5},
#         (16, 4): {'Description': 'Guardar el paquete sin abrirlo.',
#                   'Resolution_Answer': 'Alguien parece notar tu interés y comienzas a sentirte observado. Dejas el paquete en casa y sales en busca de aire fresco y un poco de claridad.','Protagonista': 0, 'NextStep_Adventure': 5},
#
#         # Paso 5: Alguien te sigue
#         (17, 5): {'Description': 'Intentar perder a la persona que te sigue.',
#                   'Resolution_Answer': 'Logras despistarlo, pero confirmas que alguien vigila tus movimientos.', 'Protagonista': 0, 'NextStep_Adventure': 6},
#         (18, 5): {'Description': 'Intentar perder a la persona que te sigue.',
#                   'Resolution_Answer': 'Te tropiezas y te golpeas la cabeza al caer sin entender muy bien que acaba de pasar. Cuando te giras ya lo hay nadie allí.', 'Protagonista': 0,'NextStep_Adventure': 13},
#         (19, 5): {'Description': 'Confrontar directamente a la persona sospechosa.',
#                   'Resolution_Answer': 'Al darte la vuelta, sale corriendo. A los pocos metros cae violentamente; el sonido del impacto resuena en la calle vacía.\nLo ves levantarse con dificultad, sujetándose el costado, antes de perderse en la oscuridad. Días después, recordarás esa forma de cojear.', 'Protagonista': 0,'NextStep_Adventure': 13},
#         (20, 5): {'Description': 'Confrontar directamente a la persona sospechosa.',
#                   'Resolution_Answer': '“Te asesta un golpe que te derriba. Des del suelo, ves cómo la persona que te seguía tropieza con un bordillo y cae al suelo.\n Rápidamente se reincorpora cojeando, y desaparece entre los callejones estrechos mientras tu corazón late con fuerza.', 'Protagonista': 0,'NextStep_Adventure': 13},
#
#         # Paso 6: Visitar o no al padre (clave)
#         (21, 6): {'Description': 'Visitar a tu padre en la residencia.','Resolution_Answer': 'Te habla de decisiones pasadas y errores, pero evita entrar en detalles.',
#                   'Protagonista': 0, 'NextStep_Adventure': 7},
#         (22, 6): {'Description': 'Visitar a tu padre en la residencia.',
#                   'Resolution_Answer': 'La conversación es breve y confusa; percibes un profundo arrepentimiento en sus palabras, aunque la historia que te cuenta resulta inconexa y difícil de seguir.',
#                   'Protagonista': 0, 'NextStep_Adventure': 7},
#         (23, 6): {'Description': 'Decidir no visitar a tu padre por el momento.',
#                   'Resolution_Answer': 'Te concentras en la investigación, pero sientes que evitas algo importante.',
#                   'Protagonista': 0, 'NextStep_Adventure': 7},
#         (24, 6): {'Description': 'Decidir no visitar a tu padre por el momento.',
#                   'Resolution_Answer': 'Al día siguiente recibes noticias preocupantes desde la residencia.','Protagonista': 0, 'NextStep_Adventure': 11},
#
#         # Paso 7: Muerte del padre / carta
#         (25, 7): {'Description': 'Leer la carta encontrada entre las pertenencias de tu padre.',
#                   'Resolution_Answer': 'La carta menciona promesas, silencios y una culpa que nunca se reparó.','Protagonista': 0, 'NextStep_Adventure': 11},
#         (26, 7): {'Description': 'Leer la carta encontrada entre las pertenencias de tu padre.',
#                   'Resolution_Answer': 'El contenido es ambiguo y deja más preguntas que respuestas.','Protagonista': 0, 'NextStep_Adventure': 10},
#         (27, 7): {'Description': 'No leer la carta todavía.',
#                   'Resolution_Answer': 'Decides esperar, pero la sensación de urgencia aumenta.', 'Protagonista': 0,    'NextStep_Adventure': 8},
#         (28, 7): {'Description': 'No leer la carta todavía.',
#                   'Resolution_Answer': 'Alguien parece interesado en esa carta más que tú.', 'Protagonista': 0, 'NextStep_Adventure': 9},
#
#         # Paso 8: Tensión abierta en el pueblo
#         (29, 8): {'Description': 'Hablar públicamente con algunas familias afectadas.',
#                   'Resolution_Answer': 'El pueblo comienza a dividirse y surgen bandos.', 'Protagonista': 0,'NextStep_Adventure': 12},
#         (30, 8): {'Description': 'Hablar públicamente con algunas familias afectadas.',
#                   'Resolution_Answer': 'La conversación se descontrola y genera miedo.', 'Protagonista': 0, 'NextStep_Adventure': 12},
#         (31, 8): {'Description': 'Seguir investigando en silencio.',
#                   'Resolution_Answer': 'Descubres conexiones entre ciertas familias y el antiguo negocio.','Protagonista': 0, 'NextStep_Adventure': 11},
#         (32, 8): {'Description': 'Seguir investigando en silencio.',
#                   'Resolution_Answer': 'Pierdes apoyo social y te quedas solo.', 'Protagonista': 0,'NextStep_Adventure': 11},
#
#         # Paso 9: El médico entra en escena
#         (33, 9): {'Description': 'Hablar con el médico del centro de salud.',
#                   'Resolution_Answer': 'Te menciona patrones de enfermedades sin causa clara.', 'Protagonista': 0,'NextStep_Adventure': 12},
#         (34, 9): {'Description': 'Hablar con el médico del centro de salud.',
#                   'Resolution_Answer': 'Evita responder con claridad y parece nervioso.', 'Protagonista': 0,'NextStep_Adventure': 11},
#         (35, 9): {'Description': 'Evitar al médico y observar sus movimientos.',
#                   'Resolution_Answer': 'Descubres visitas nocturnas sospechosas.', 'Protagonista': 0,'NextStep_Adventure': 12},
#         (36, 9): {'Description': 'Evitar al médico y observar sus movimientos.',
#                   'Resolution_Answer': 'Pierdes su rastro y alertas a alguien.', 'Protagonista': 0, 'NextStep_Adventure': 11},
#
#         # Paso 10: Información incompleta
#         (37, 10): {'Description': 'Cruzar toda la información recopilada.',
#                    'Resolution_Answer': 'Empiezas a ver un patrón inquietante.', 'Protagonista': 0, 'NextStep_Adventure': 12},
#         (38, 10): {'Description': 'Cruzar toda la información recopilada.',
#                    'Resolution_Answer': 'Los datos no encajan del todo.', 'Protagonista': 0, 'NextStep_Adventure': 11},
#         (39, 10): {'Description': 'Descartar parte de la información.',
#                    'Resolution_Answer': 'Simplificas el caso, pero pierdes matices importantes.', 'Protagonista': 0,'NextStep_Adventure': 11},
#         (40, 10): {'Description': 'Descartar parte de la información.',
#                    'Resolution_Answer': 'Tomas una decisión precipitada.', 'Protagonista': 0, 'NextStep_Adventure': 11},
#
#         # Paso 11: Últimas amenazas
#         (41, 11): {'Description': 'Ignorar las amenazas recibidas.',
#                    'Resolution_Answer': 'El riesgo aumenta, pero sigues adelante.', 'Protagonista': 0,'NextStep_Adventure': 12},
#         (42, 11): {'Description': 'Ignorar las amenazas recibidas.',
#                    'Resolution_Answer': 'Alguien cercano sufre las consecuencias.', 'Protagonista': 0,'NextStep_Adventure': 12},
#         (43, 11): {'Description': 'Responder de alguna forma a las amenazas.',
#                    'Resolution_Answer': 'Provocas una reacción inesperada.', 'Protagonista': 0,'NextStep_Adventure': 12},
#         (44, 11): {'Description': 'Responder de alguna forma a las amenazas.',
#                    'Resolution_Answer': 'Te expones demasiado.', 'Protagonista': 0, 'NextStep_Adventure': 12},
#
#         # Paso 13: Golpe en la cabeza
#         (49, 13): {'Description': 'Decides ir al centro médico del pueblo para que te revisen',
#                   'Resolution_Answer': 'El médico más respetado del pueblo te atiende, pero hoy parece estar de mal humor.\nApenas te examina y te despacha con una receta, sin comprobar tu estado real, dejándote con dudas sobre su profesionalidad.','NextStep_Adventure': 6},
#         (50, 13): {'Description': 'Decides ir al centro médico del pueblo para que te revisen',
#                   'Resolution_Answer': 'Al llegar, descubres que el médico habitual no está disponible. Te atiende una doctora nueva, amable y profesional, que te receta medicación para aliviar el dolor.\nAl salir, ves a un hombre conocido cojeando, preguntando por el médico principal. Su actitud te resulta extraña y te pone en alerta.','NextStep_Adventure': 6},
#         (51, 13): {'Description': 'Decides no ir al médico y quedarte descansando en casa',
#                   'Resolution_Answer': 'El reposo no ayuda y el dolor se intensifica, lo que afecta tu concentración y capacidad para analizar los documentos y pistas que ya tienes.','NextStep_Adventure': 9},
#         (52, 13): {'Description': 'Decides no ir al médico y quedarte descansando en casa',
#                   'Resolution_Answer': 'Pasas la tarde descansando y notas que el dolor disminuye.\nAprovechas para revisar mentalmente los sucesos recientes y empiezas a conectar pequeños detalles que antes habías ignorado','NextStep_Adventure': 9},
#
#         # ----- Paso 12: Finales extensos -----
#         (45, 12): {'Description': 'Decides revelar toda la verdad al público a través de un amigo propietario del periódico provincial.',
#                    'Resolution_Answer': 'Decides publicar toda la información a través del periódico provincial.\nRevelas cómo tu padre y algunos trabajadores permitieron que los químicos dañaran a varias familias y cómo los hermanos Brunde, (Hugo Brunde – Médico del pueblo y Lorenzo Brunde – Empresario y gestor de tierras),\ntras la muerte de sus padres, extorsionaron a las ex trabajadoras para quedarse con sus tierras. El pueblo estalla en debates y conflictos; unos exigen justicia mientras otros sienten traición.\nAun así, la luz de la verdad permite que algunas víctimas obtengan reconocimiento y apoyo. Has expuesto todo, pero el precio ha sido la paz del pueblo.','Protagonista': 0, 'NextStep_Adventure': None},
#
#         (46, 12): {'Description': 'Decides revelar toda la verdad al público a través de un amigo propietario del periódico provincial.',
#                    'Resolution_Answer': 'Optas por no implicar a tu padre y concentras tu investigación en los hermanos Brunde (Hugo Brunde – Médico del pueblo y Lorenzo Brunde – Empresario y gestor de tierras).\nPublicas pruebas sobre sus extorsiones a ex trabajadoras de la empresa y su especulación de terrenos.\nLa comunidad se revuelve contra ellos, y finalmente son juzgados o expulsados del pueblo. Aunque los secretos de tu padre permanecen guardados, sientes un alivio moral al proteger su memoria y exponer a quienes realmente manipulaban y amenazaban a los vecinos.\nLa justicia parcial llega, y algunas familias pueden respirar sin miedo, mientras tú cargas con la complejidad del silencio y la verdad incompleta.','Protagonista': 0, 'NextStep_Adventure': None},
#
#         (47, 12): {'Description': 'Decides guardar todos los secretos y marcharte del pueblo, sin implicarte en nada.',
#                    'Resolution_Answer': 'Decides no hacer pública ninguna información.\nGuardas los secretos de tu padre y de los hermanos Brunde (Hugo Brunde – Médico del pueblo y Lorenzo Brunde – Empresario y gestor de tierras), pero abandonas el pueblo, llevándote contigo la memoria de lo sucedido.\nLas familias extorsionadas y enfermas continúan enfrentando las consecuencias, pero tú eliges alejarte del resentimiento y el conflicto. El tiempo será juez de las cicatrices abiertas y de las injusticias no reparadas.\nMientras te alejas, piensas en la vida que podrías reconstruir lejos de Valdemora, con la certeza de que algunas verdades son demasiado pesadas para compartir, y que tu propia paz depende de tu silencio.',
#                    'Protagonista': 0, 'NextStep_Adventure': None},
#
#         (48, 12): {'Description': 'Decides mantener el secreto parcialmente y solo proteger a tu familia, sin revelar nada a nadie.',
#                    'Resolution_Answer': 'Decides guardar el secreto y abandonar Valdemora, llevándote contigo la carga de todo lo ocurrido.\nDurante dos años intentas rehacer tu vida lejos del pueblo, con la memoria de los abusos de los hermanos Brunde y las injusticias contra las familias ex trabajadoras siempre presentes.\nUn día, recibes una llamada de un amigo propietario del diario provincial: al día siguiente se publicará toda la verdad. Los hermanos seguirán enfrentando las consecuencias, y finalmente se conocerá el papel de tu padre y de quienes silenciaron los daños.\nTe quedas en silencio, observando cómo el tiempo revela lo que tú decidiste proteger.','Protagonista': 0, 'NextStep_Adventure': None},
#
#     }
#
# }




# =======================
# Diccionario id_by_steps
# =======================
id_by_steps = {
    1: {
        1: {'Description': 'Durante las primeras horas del viaje, un ruido metálico irregular comienza a escucharse desde una de las secciones externas de la nave.\nLos sensores no detectan nada concluyente, pero la tripulación empieza a inquietarse.','answers_in_step': (1, 2, 3, 4),'Final_Step': 0},
        2: {'Description': 'Tras evaluar la situación, la tripulación debate si aterrizar en un planeta cercano para revisar sistemas y descansar,\no continuar el viaje sin desviarse del plan original.','answers_in_step': (5, 6, 7, 8),'Final_Step': 0},
        3: {'Description': 'Al avanzar por el sector, detectan señales de vida inteligente.\nPronto se encuentran frente a una forma de vida alienígena desconocida, cuyo comportamiento es difícil de interpretar.','answers_in_step': (9, 10, 11, 12),'Final_Step': 0},
        4: {'Description': 'Las comunicaciones con los alienígenas evolucionan hacia una posible negociación.\nAmbas partes parecen desconfiar, pero una alianza podría traer beneficios… o graves consecuencias.','answers_in_step': (13, 14, 15, 16),'Final_Step': 0},
        5: {'Description': 'En la superficie de un pequeño planeta, el equipo detecta un objeto brillante parcialmente enterrado.\nSu origen parece ser desconocido y llama su atención.','answers_in_step': (17, 18, 19, 20),'Final_Step': 0},
        6: {'Description': 'Antes de continuar, surge la duda sobre el estado real del combustible.\nUna revisión podría prevenir problemas futuros, aunque también implica perder más tiempo.','answers_in_step': (21, 22, 23, 24),'Final_Step': 0},
        7: {'Description': 'Una tormenta atmosférica inesperada golpea la nave. Los sistemas tiemblan y el margen de error es mínimo.','answers_in_step': (25, 26, 27, 28),'Final_Step': 0},
        8: {'Description': 'El deterioro progresivo fuerza al equipo a ejecutar una reparación vital de la nave.','answers_in_step': (29, 30, 31, 32),'Final_Step': 0},
        9: {'Description': 'Durante la exploración, se descubre una caverna iluminada por cristales naturales que emiten energía.','answers_in_step': (33, 34, 35, 36),'Final_Step': 0},
        10: {'Description': 'Las alarmas se activan: los niveles de oxígeno de los trajes fluctúan peligrosamente. Una mala decisión podría ser fatal.','answers_in_step': (37, 38, 39, 40),'Final_Step': 0},
        11: {'Description': 'La nave recibe una señal desconocida de origen incierto que podría ser una trampa o una oportunidad.','answers_in_step': (41, 42, 43, 44),'Final_Step': 0},
        12: {'Description': 'Tras todo lo ocurrido, la tripulación debe tomar la decisión final:\nAbortar la misión y regresar a casa o continuar hasta el final, asumiendo todos los riesgos.','answers_in_step': (45, 46, 47, 48),'Final_Step': 1}
    },

    2: {
        1: {'Description':'Una explosión sacude las afueras del pueblo de madrugada mientras vas de camino a casa.\nAl acercarte al lugar, reconoces un viejo local cerrado desde hace casi dos década, ahora reducido a escombros.\n'
            'El edificio perteneció a una familia influyente y reservada.Mientras rodeas los restos, un olor extraño se queda suspendido en el aire y te obliga a detenerte.',
            'answers_in_step': (1, 2, 3, 4), 'Final_Step': 0},
        2: {'Description':'Permaneces cerca del lugar mientras la zona aún está desierta. El silencio es incómodo y cada sonido parece fuera de lugar.\n''Algo en ese sitio no encaja del todo, pero no logras concretar qué es exactamente.',
            'answers_in_step': (5, 6, 7, 8), 'Final_Step': 0},
        3: {'Description':'Con el paso de las horas, el pueblo despierta. Las miradas se cruzan más de lo habitual y notas conversaciones que se cortan cuando te acercas.\n'
            'Empiezas a sentir que la explosión ha removido algo más que ruinas.','answers_in_step': (9, 10, 11, 12), 'Final_Step': 0},
        4: {'Description': 'Ese mismo día, un rumor se extiende con rapidez: varias personas han recibido un paquete en la puerta de casa.\n'
            'Entre esas personas estás tú, que encuentras el paquete en la puerta principal cuando te dipones a salir de casa.','answers_in_step': (13, 14, 15, 16), 'Final_Step': 0},
        5: {'Description': 'Mientras caminas por el pueblo, empiezas a notar una presencia que parece mantenerse siempre a cierta distancia.',
            'answers_in_step': (17, 18, 19, 20), 'Final_Step': 0},
        6: {'Description':'Las dudas empiezan a acumularse y, casi sin querer, piensas en tu padre.\n''Hace tiempo que no vas a la residencia a visitarlo, pero algo te dice que deberías hacerlo… o quizá no.',
            'answers_in_step': (21, 22, 23, 24), 'Final_Step': 0},
        7: {'Description':'Los acontecimientos se precipitan. La residencia te llama a primera hora: tu padre ha sufrido un accidente durante la noche. Una fallo en la medicación, dicen. Cuando llegas, ya es demasiado tarde.\n'
            'Mientras recoges sus pocas pertenencias encuentras varias cartas antiguas. Una de ellas está marcada con tu nombre y una frase escrita a mano que te deja helado/a:"La VERDAD que no quiero llevarme conmigo".',
            'answers_in_step': (25, 26, 27, 28), 'Final_Step': 0},
        8: {'Description':'El ambiente del pueblo cambia de forma visible.\n''Algunas personas me evitan, otras parecen buscarme. La tensión se palpa en cada conversación.',
            'answers_in_step': (29, 30, 31, 32), 'Final_Step': 0},
        9: {'Description':'Empiezo a fijarme en detalles que antes pasaban desapercibidos.\n''Ciertas personas parecen saber más de lo que dicen, y algunas preguntas generan silencios demasiado largos.',
            'answers_in_step': (33, 34, 35, 36), 'Final_Step': 0},
        10: {'Description':'Revisas mentalmente todo lo ocurrido desde la explosión.\n''Hay conexiones que empiezan a formarse, aunque todavía no logras ver el cuadro completo.',
            'answers_in_step': (37, 38, 39, 40), 'Final_Step': 0},
        11: {'Description':'Las advertencias dejan de ser sutiles.\n''Mensajes indirectos, gestos, comentarios que parecen decirme que siga adelante… o que me detenga.',
            'answers_in_step': (41, 42, 43, 44), 'Final_Step': 0},
        12: {'Description':'Llegas a un punto en el que ya no puedes seguir fingiendo que no entiendes lo que ocurre.\n''Hagas lo que haga a partir de ahora, nada volverá a ser igual.',
            'answers_in_step': (45, 46, 47, 48), 'Final_Step': 1},
        13: {'Description': 'Tras varios días de molestias musculares y punzadas en la cabeza, y considerando todo lo sucedido, contemplas la idea de ir al médico para que te examinen y te receten algo que calme los síntomas.\n',
            'answers_in_step': (49, 50, 51, 52), 'Final_Step': 0}
    }
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

    # --- Recuperar info básica de aventuras ---
    cursor.execute("SELECT distinct codAdventure, Name, description FROM adventure")
    aventuras_db = cursor.fetchall()
    adventures_dict = {}
    for adv in aventuras_db:
        adventures_dict[adv["codAdventure"]] = {
            "Name": adv["Name"],
            "Description": adv["description"],
            "characters": [],  # Se llenará después
            "states": []       # Se llenará después
        }
    # --- Recuperar personajes asociados a cada aventura ---
    cursor.execute("SELECT idAdventure, idCharacter FROM adventure_characters")
    adv_chars = cursor.fetchall()
    for row in adv_chars:
        adv_id = row["idAdventure"]
        char_id = row["idCharacter"]
        if adv_id in adventures_dict:
            adventures_dict[adv_id]["characters"].append(char_id)

    # --- Recuperar estados asociados a cada aventura ---
    cursor.execute("SELECT idAdventure, idState FROM adventure_states")
    adv_states = cursor.fetchall()
    for row in adv_states:
        adv_id = row["idAdventure"]
        state_id = row["idState"]
        if adv_id in adventures_dict:
            adventures_dict[adv_id]["states"].append(state_id)

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



def get_id_bystep_adventure(idAdventure):
    return id_by_steps[idAdventure]




# - - - - ENCUENTRA PRIMER PASO DE LA AVENTURA - - - -
def get_first_step_adventure(idAdventure):
    # Obtener todos los pasos de la aventura actual
    steps_dict = get_id_bystep_adventure(idAdventure)
    # Retornar el primer key (step) del diccionario
    return list(steps_dict.keys())[0]




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




# - - - PIDE Y VALIDA LA ELECCION DE LA AVENTURA Y IMPRIME EL CONTEXTO DE ESTA - - -
def selectAdventure(adventures, game_context):
    list_adventures = list(adventures.keys())

    opc_aventura = input("\nElige la aventura: ")
    while not opc_aventura.isdigit() or int(opc_aventura) not in range(1, len(list_adventures) + 1):
        print("Opción inválida")
        opc_aventura = input("Elige la aventura: ")

    opc_aventura = list_adventures[int(opc_aventura) - 1]

    # Actualizar game_context
    game_context['idAdventure'] = opc_aventura
    game_context['nameAdventure'] = adventures[opc_aventura]['Name']

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
    pide al usuario que elija uno, y actualiza game_context.
    """
    opc_aventura = game_context['idAdventure']
    character_ids = adventures[opc_aventura]['characters']

    print("\n"+"Characters".center(100,"=")+ "\n")
    for id_char in character_ids:
        print("{}) {}".format(id_char, characters[id_char]))


    opc_character = input("\nElige el personaje: ")
    while not opc_character.isdigit() or int(opc_character) not in character_ids:
        print("Opción inválida")
        opc_character = input("Elige el personaje: ")

    opc_character = int(opc_character)

    # Actualizar game_context
    game_context['idChar'] = opc_character
    game_context['characterName'] = characters[opc_character]

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

        print("Invalid option")




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





# - - - CONSTRUIR DICCIONARIO DE POSIBLES RESPUESTAS CON SUS CONSEQUENCIAS Y STATES SEGÚN AVENTURA - - -
# Función que construye el diccionario dinámico de answers
def build_answers_by_step_adventure(idAdventure):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Respuestas base
    cursor.execute("""
        SELECT idAnswer, idStep, description, resolution_answer, next_step
        FROM answers
        WHERE idAdventure = %s
    """, (idAdventure,))
    answers = cursor.fetchall()

    # Estados afectados por respuesta
    cursor.execute("""
        SELECT ase.idAnswer,
               gsm.name AS state_name,
               ase.value
        FROM answer_state_effects ase
        JOIN game_states_master gsm ON gsm.idState = ase.idState
        WHERE ase.idAdventure = %s
    """, (idAdventure,))
    states_rows = cursor.fetchall()

    # Mapear estados por respuesta
    states_map = {}
    for row in states_rows:
        states_map.setdefault(row['idAnswer'], {})[row['state_name']] = row['value']

    # Construir diccionario final
    result = {idAdventure: {}}

    for a in answers:
        key = (a['idAnswer'], a['idStep'])
        result[idAdventure][key] = {
            'Description': a['description'],
            'Resolution_Answer': a['resolution_answer'],
            'NextStep_Adventure': a['next_step'],
            'states': states_map.get(a['idAnswer'], {})
        }

    cursor.close()
    conn.close()
    return result







# =========================================================================
#                             VARIABLES SIMPLES
# =========================================================================
#menu_logout = "1)Logout\n2)Play\n3)Replay Adventure\n4)Reports\n5)Exit"
#menu_report = "1)Most used answer\n2)Player with more games played\n3)Games played by user \n4)Back"
menu_logout = "\n" + "-".center(50,"-") +"\n"+"AVENTURA".center(50,"*") + "\n" + "-".center(50,"-") + "\n" + "1)Cerrar Sesión\n2)Jugar\n3)Rejugar Aventura\n4)Reportes\n5)Salir"
menu_report = "1)Respuestas más utilizadas\n2)Jugador que más veces ha jugado\n3)Aventuras jugadas por el jugador  \n4)Back"
menu_principal = "\n" + "-".center(50,"-") +"\n"+"MENU PRINCIPAL".center(50,"*") + "\n" + "-".center(50,"-") + "\n" + "1)Crear Usuario\n2)Iniciar Sesión\n3)Mostrar aventuras\n4)Salir\n"
inputOptText="\nElige tu opción: "
menu_creausu = "\n\n\n" + "-".center(50,"-") +"\n"+"CREACION USUARIO".center(50,"*") + "\n" + "-".center(50,"-")
menu_inises = "\n\n\n" + "-".center(50,"-") +"\n"+"INICIO SESION".center(50,"*") + "\n" + "-".center(50,"-")
menu_ch = "\n\n\n" + "-".center(50,"-") +"\n"+"SELECCIONA UN PERSONAJE".center(50,"*") + "\n" + "-".center(50,"-") + "\n"
cab_ch = "{:<5}{:>45}".format("ID","NOMBRE") + "\n" + "-".center(50,"-") + "\n"
acabado = "-".center(50,"-") + "\n"
datos = ""
dicc_ch_recu = {}
dicc_get_users = {}
dicc_get_adventures = {}
dicc_get_games = {}
dicc_get_choices = {}
login = ""















# def getTableMostUsedAnswers(cursor):
#     query = """
#     SELECT
#         a.id_adventure || ' - ' || a.name,
#         s.id_step || ' - ' || s.description,
#         an.id_answer || ' - ' || an.description,
#         COUNT(pa.id_answer) as times_used
#     FROM played_answers pa
#     JOIN adventures a ON a.id_adventure = pa.id_adventure
#     JOIN steps s ON s.id_step = pa.id_step AND s.id_adventure = pa.id_adventure
#     JOIN answers an ON an.id_answer = pa.id_answer AND an.id_adventure = pa.id_adventure
#     GROUP BY pa.id_adventure, pa.id_step, pa.id_answer
#     ORDER BY times_used DESC
#     """
#
#     cursor.execute(query)
#     rows = cursor.fetchall()
#
#     headers = (
#         "ID AVENTURA - NOMBRE",
#         "ID PASO - DESCRIPCION",
#         "ID RESPUESTA - DESCRIPCION",
#         "NUMERO VECES SELECCIONADA"
#     )
#
#     return (headers, *rows)
#
#
#
# def getFormatedTable(queryTable, title=""):
#     """
#     Recibe queryTable como lo retorna getTable()
#     y lo imprime en consola formateado.
#     """
#     MAX_WIDTH = 120  # Ancho máximo de la consola
#     n_columns = len(queryTable[0])
#     col_width = MAX_WIDTH // n_columns  # ancho aproximado por columna
#
#     output = ""
#     if title:
#         output += "="*MAX_WIDTH + "\n"
#         output += title.center(MAX_WIDTH) + "\n"
#         output += "="*MAX_WIDTH + "\n"
#
#     # Cabecera
#     headers = queryTable[0]
#     for h in headers:
#         output += f"{h[:col_width]:<{col_width}}"
#     output += "\n" + "*"*MAX_WIDTH + "\n"
#
#     # Filas
#     for row in queryTable[1:]:
#         # Cortar cada celda en varias líneas si es necesario
#         wrapped_cells = [textwrap.wrap(str(cell), col_width) for cell in row]
#         max_lines = max(len(c) for c in wrapped_cells)
#
#         for i in range(max_lines):
#             for cell_lines in wrapped_cells:
#                 if i < len(cell_lines):
#                     output += f"{cell_lines[i]:<{col_width}}"
#                 else:
#                     output += " " * col_width
#             output += "\n"
#         output += "\n"
#
#     print(output)
#
#
#
#
# from db import get_connection  # tu función de conexión
#
# def getTable(query):
#     """
#     Ejecuta un query SQL y devuelve una tupla de tuplas:
#     (headers, fila1, fila2, ...)
#     """
#     conn = get_connection()  # Crear conexión
#     if conn is None:
#         print("Error: no se pudo conectar a la base de datos")
#         return ()
#
#     cursor = conn.cursor(dictionary=True)  # Diccionarios para poder usar row.values()
#
#     cursor.execute(query)
#     rows = cursor.fetchall()
#
#     # Cabeceras
#     headers = tuple(cursor.column_names)
#     result = [headers]
#
#     for row in rows:
#         result.append(tuple(row.values()))  # Convertir diccionario a tupla
#
#     cursor.close()
#     conn.close()
#
#     return tuple(result)

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
    if checkPassword(pwd):
        sql = "INSERT INTO user (Username, Password) VALUES (%s, %s);"
        cursor.execute(sql, (usu, pwd))
        conn.commit()
        print("Se ha creado el nuevo usuario")

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
    print(dicc_ch_recu)

def getAdventures():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM adventure")
    adv_recu = cursor.fetchall()
    dicc_get_adventures = {}
    for adv in adv_recu:
        dicc_get_adventures[adv["idAdventure"]] = { "Name": adv["Name"], "Description": adv["Description"]}
    print(dicc_get_adventures)

def getGame_States_Master():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM game_states_master")
    gsm_recu = cursor.fetchall()
    dicc_get_gsm = {}
    for gsm in gsm_recu:
        dicc_get_gsm[gsm["idState"]] = { "Name": gsm["Name"], "initial_value": gsm["initial_value"]}
    print(dicc_get_gsm)

def getAdventure_States():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM adventure_states")
    advs_recu = cursor.fetchall()
    dicc_get_advs = {}
    for advs in advs_recu:
        dicc_get_advs[advs["idAdventure"]] = advs["idState"]
    print(dicc_get_advs)

def getAdventure_Context():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM adventure_context")
    advc_recu = cursor.fetchall()
    dicc_get_advc = {}
    for advc in advc_recu:
        dicc_get_advc[advc["idAdventure"]] = advc["context_text"]
    print(dicc_get_advc)

def getAnswers():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM answers")
    ans_recu = cursor.fetchall()
    dicc_get_ans = {}
    for ans in ans_recu:
        dicc_get_ans[ans["idAnswer"]] = { "idAdventure":ans["idAdventure"],"idStep":ans["idStep"],"description":ans["description"],"resolution_answer":ans["resolution_answer"],"crew_loss":ans["crew_loss"],"damage_ship":ans["damage_ship"],"salud":ans["salud"],"next_step":ans["next_step"]}
    print(dicc_get_ans)

def getAnswer_State_Effects():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM answer_state_effects")
    ase_recu = cursor.fetchall()
    dicc_get_ase = {}
    for ase in ase_recu:
        dicc_get_ase[ase["idAnswer"]] = { "idAdventure":ase["idAdventure"],"idState":ase["idState"],"value":ase["value"]}
    print(dicc_get_ase)

def getAnswer_Bysteps_Adventure():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM answers_bysteps_adventure")
    aba_recu = cursor.fetchall()
    dicc_get_aba = {}
    for aba in aba_recu:
        dicc_get_aba[aba["idAnswers_ByStep_Adventure"]] = { "idByStep_Adventure":aba["idByStep_Adventure"],"Description":aba["Description"],"Resolution_Answer":aba["Resolution_Answer"],"NextStep_Adventure":aba["NextStep_Adventure"]}
    print(dicc_get_aba)

def getByStep_Adventure():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM bystep_adventure")
    bsa_recu = cursor.fetchall()
    dicc_get_bsa = {}
    for bsa in bsa_recu:
        dicc_get_bsa[bsa["idByStep_Adventure"]] = {"idAdventure": bsa["idAdventure"], "Description": bsa["Description"], "Final_Step": bsa["Final_Step"]}
    print(dicc_get_bsa)

def getGame():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM game")
    game_recu = cursor.fetchall()
    dicc_get_game = {}
    for game in game_recu:
        dicc_get_game[game["idGame"]] = {"idUser": game["idUser"], "idCharacter": game["idCharacter"],"idAdventure": game["idAdventure"],"date": game["date"]}
    print(dicc_get_game)

def getSteps():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM steps")
    steps_recu = cursor.fetchall()
    dicc_get_steps = {}
    for steps in steps_recu:
        dicc_get_steps[steps["idStep"]] = {"idAdventure": steps["idAdventure"], "description": steps["description"],"final_step": steps["final_step"]}
    print(dicc_get_steps)

def getReplay_Adventures():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM replay_adventures")
    rep_recu = cursor.fetchall()
    dicc_get_rep = {}
    for rep in rep_recu:
        dicc_get_rep[rep["idReplay"]] = {"idUser": rep["idUser"],"idAdventure": rep["idAdventure"],"idCharacter": rep["idCharacter"], "adventure_name": rep["adventure_name"],"character_name": rep["character_name"]}
    print(dicc_get_rep)

def getUser():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user")
    user_recu = cursor.fetchall()
    dicc_get_user = {}
    for user in user_recu:
        dicc_get_user[user["idUser"]] = { "Username": user["Username"], "Password": user["Password"]}
    print(dicc_get_user)

