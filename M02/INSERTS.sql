USE proyecto_bjr;

INSERT INTO user (Username, Password) VALUES
('Prueba', 'abc123.');

INSERT INTO adventure (idAdventure, Name, Description) VALUES
(1, 'Expedición al Sector Z-47','Una peligrosa misión espacial con decisiones críticas y encuentros inesperados.'),
(2, 'La carta anónima','En un pequeño pueblo marcado por el silencio y las viejas lealtades, un suceso inesperado despierta\nsecretos enterrados durante años y obliga a enfrentar decisiones del pasado que nunca llegaron a saldarse.');

INSERT INTO characters (idCharacter, CharacterName, codAdventure) VALUES
(1, 'Capitán: Shelton',1),
(2, 'Ingeniero Jefe: Ramirez',1),
(3, 'Médico de la Nave: Tanaka',1),
(4, 'Especialista en Comunicaciones: Kane',1),
(5, 'Médico de Vuelo: Patel',1),
(6, 'Elias Mercer – detective veterano, metódico.',2),
(7, 'Cleo Bradford – joven analista de crímenes, intuitiva.',2),
(8, 'Dante Ruiz – detective rebelde que sigue su instinto.',2),
(9, 'Colin Drake – oficial de policía rutinario, de moral ambigua.',2);


INSERT INTO game_states_master (idState, Name, initial_value) VALUES
(1, 'nave', 5),
(2, 'tripulacion', 5);


INSERT INTO adventure_states (idAdventure, idState) VALUES
(1, 1),  -- 'nave'
(1, 2);  -- 'tripulacion'



INSERT INTO adventure_context (idAdventure, context_text) VALUES
(1, 'Tras años de exhaustiva preparación, cinco tripulantes de la Base Helios se disponen a embarcarse en una misión sin precedentes: explorar el sector Z-47, una región del espacio jamás cartografiada.
Los estudios preliminares sugieren que se trata de una zona rica en recursos energéticos capaces de transformar para siempre la forma en que la Tierra produce y utiliza la energía.
Confiados en el éxito de la expedición y en la solidez de su entrenamiento, la nave Astraeon despega sin incidentes, adentrándose en lo desconocido…'),
(2, 'Todo comienza un martes de abril, a las dos de la madrugada, en Eldralva, un pueblo aislado de apenas setecientos habitantes.\nRodeado de campos y antiguas explotaciones agrícolas, es un lugar donde todos se conocen, los silencios pesan más que las palabras y el pasado nunca termina de desaparecer.');



INSERT INTO steps (idStep, idAdventure, description, final_step) VALUES
(1, 1, 'Durante las primeras horas del viaje, un ruido metálico irregular comienza a escucharse desde una de las secciones externas de la nave.\n
Los sensores no detectan nada concluyente, pero la tripulación empieza a inquietarse.', 0),
(2, 1, 'Tras evaluar la situación, la tripulación debate si aterrizar en un planeta cercano para revisar sistemas y descansar,\no continuar el viaje sin desviarse del plan original.', 0),
(3, 1, 'Al avanzar por el sector, detectan señales de vida inteligente.\nPronto se encuentran frente a una forma de vida alienígena desconocida,cuyo comportamiento es difícil de interpretar.', 0),
(4, 1, 'Las comunicaciones con los alienígenas evolucionan hacia una posible negociación.\nAmbas partes parecen desconfiar, pero una alianza podría traer beneficios… o graves consecuencias.', 0),
(5, 1, 'En la superficie de un pequeño planeta, el equipo detecta un objeto brillante parcialmente enterrado.\nSu origen parece ser desconocido y llama su atención.', 0),
(6, 1, 'Antes de continuar, surge la duda sobre el estado real del combustible.\nUna revisión podría prevenir problemas futuros, aunque también implica perder más tiempo.', 0),
(7, 1, 'Una tormenta atmosférica inesperada golpea la nave. Los sistemas tiemblan y el margen de error es mínimo.', 0),
(8, 1, 'El deterioro progresivo fuerza al equipo a ejecutar una reparación vital de la nave.', 0),
(9, 1, 'Durante la exploración, se descubre una caverna iluminada por cristales naturales que emiten energía.', 0),
(10, 1, 'Las alarmas se activan: los niveles de oxígeno de los trajes fluctúan peligrosamente. Una mala decisión podría ser fatal.', 0),
(11, 1, 'La nave recibe una señal desconocida de origen incierto que podría ser una trampa o una oportunidad.', 0),
(12, 1, 'Tras todo lo ocurrido, la tripulación debe tomar la decisión final:\nAbortar la misión y regresar a casa o continuar hasta el final, asumiendo todos los riesgos.', 1);



INSERT INTO steps (idStep, idAdventure, description, final_step) VALUES
(1, 2, 'Una explosión sacude las afueras del pueblo de madrugada mientras vas de camino a casa.\nAl acercarte al lugar, reconoces un viejo local cerrado desde hace casi dos década, ahora reducido a escombros.
El edificio perteneció a una familia influyente y reservada.\nMientras rodeas los restos, un olor extraño se queda suspendido en el aire y te obliga a detenerte.', 0),
(2, 2, 'Permaneces cerca del lugar mientras la zona aún está desierta. El silencio es incómodo y cada sonido parece fuera de lugar.\nAlgo en ese sitio no encaja del todo, pero no logras concretar qué es exactamente.', 0),
(3, 2, 'Con el paso de las horas, el pueblo despierta. Las miradas se cruzan más de lo habitual y notas conversaciones que se cortan cuando te acercas.\nEmpiezas a sentir que la explosión ha removido algo más que ruinas.', 0),
(4, 2, 'Ese mismo día, un rumor se extiende con rapidez: varias personas han recibido un paquete en la puerta de casa.\nEntre esas personas estás tú, que encuentras el paquete en la puerta principal cuando te dipones a salir de casa.', 0),
(5, 2, 'Mientras caminas por el pueblo, empiezas a notar una presencia que parece mantenerse siempre a cierta distancia.', 0),
(6, 2, 'Las dudas empiezan a acumularse y, casi sin querer, piensas en tu padre.\nHace tiempo que no vas a la residencia a visitarlo, pero algo te dice que deberías hacerlo… o quizá no.', 0),
(7, 2, 'Los acontecimientos se precipitan. La residencia te llama a primera hora: tu padre ha sufrido un accidente durante la noche.\nUn fallo en la medicación, dicen. Cuando llegas, ya es demasiado tarde.
Mientras recoges sus pocas pertenencias encuentras varias cartas antiguas.\nUna de ellas está marcada con tu nombre y una frase escrita a mano que te deja helado/a:
"La VERDAD que no quiero llevarme conmigo".', 0),
(8, 2, 'El ambiente del pueblo cambia de forma visible.\nAlgunas personas me evitan, otras parecen buscarme. La tensión se palpa en cada conversación.', 0),
(9, 2, 'Empiezo a fijarme en detalles que antes pasaban desapercibidos.\nCiertas personas parecen saber más de lo que dicen, y algunas preguntas generan silencios demasiado largos.', 0),
(10, 2, 'Revisas mentalmente todo lo ocurrido desde la explosión.\nHay conexiones que empiezan a formarse, aunque todavía no logras ver el cuadro completo.', 0),
(11, 2, 'Las advertencias dejan de ser sutiles.
Mensajes indirectos, gestos, comentarios que parecen decirme que siga adelante… o que me detenga.', 0),
(12, 2, 'Llegas a un punto en el que ya no puedes seguir fingiendo que no entiendes lo que ocurre.\nHagas lo que haga a partir de ahora, nada volverá a ser igual.', 1),
(13, 2, 'Tras varios días de molestias musculares y punzadas en la cabeza, y considerando todo lo sucedido,\ncontemplas la idea de ir al médico para que te examinen y te receten algo que calme los síntomas.', 0);

INSERT INTO answers (idAnswer, idAdventure, idStep, Description, Resolution_Answer, crew_loss, damage_ship,  next_step) VALUES
(1, 1, 1, 'Enviar al ingeniero al exterior de la nave para investigar el origen del ruido.', 'El mecánico localiza una placa suelta antes de que cause daños mayores y refuerza la zona.', 0, 0, 2),
(2, 1, 1, 'Enviar al ingeniero al exterior de la nave para investigar el origen del ruido.', 'Durante la reparación, una pieza se desplaza bruscamente y le atrapa la mano al ingeniero del equipo, dejándole la mano gravemente herida. Tripulación -2', 2, 0, 2),
(3, 1, 1, 'Ignorar el ruido y continuar el viaje confiando en que no sea grave.', 'El fallo resulta ser menor y no vuelve a manifestarse durante el trayecto.', 0, 0, 2),
(4, 1, 1, 'Ignorar el ruido y continuar el viaje confiando en que no sea grave.', 'El problema se agrava con el tiempo y provoca una pequeña fuga de combustible. Nave -2', 0, 2, 2),

(5, 1, 2, 'Aterrizar en un planeta cercano para revisar sistemas y permitir que la tripulación descanse.', 'El aterrizaje es estable y el entorno resulta seguro.', 0, 0, 3),
(6, 1, 2, 'Aterrizar en un planeta cercano para revisar sistemas y permitir que la tripulación descanse.', 'El terreno es muy inestable; la nave sufre daños y un tripulante resulta herido durante el descenso. Tripulación -1. Nave -3', 1, 3, 3),
(7, 1, 2, 'Continuar el viaje sin desviarse para no perder tiempo.', 'Avanzan según lo previsto sin incidentes inmediatos.', 0, 0, 5),
(8, 1, 2, 'Continuar el viaje sin desviarse para no perder tiempo.', 'Un desperfecto menor en el motor se intensifica por el exceso de calor generado tras un vuelo prolongado. Nave -2', 0, 2, 5),

(9, 1, 3, 'Intentar comunicarse y confiar en los seres alienígenas.', 'Los alienígenas comparten tecnología que mejora el rendimiento de la nave. Nave +3', 0, -3, 4),
(10, 1, 3, 'Intentar comunicarse y confiar en los seres alienígenas.', 'Un malentendido provoca un ataque a distancia por parte de los alienígenas con una tecnología extraña que hiere a uno de los tripulante. Tripulación -2', 2, 0, 4),
(11, 1, 3, 'Retirarse con cautela y evitar cualquier contacto.', 'La tripulación evita posibles riesgos y continúa el viaje.', 0, 0, 5),
(12, 1, 3, 'Retirarse con cautela y evitar cualquier contacto.', 'Los alienígenas interpretan la retirada como hostilidad y atacan brevemente la nave. Nave -1', 0, 1, 5),

(13, 1, 4, 'Ceder parte de los recursos para mantener la paz.', 'La relación se fortalece y los alienígenas prometen no interferir en su camino.', 0, 0, 5),
(14, 1, 4, 'Ceder parte de los recursos para mantener la paz.', 'El capitán entrega un recurso clave para evitar el conflicto con los alienígenas.\nLa decisión deja una sensación de duda en la tripulación y debilita la confianza del equipo. Tripulación -1', 1, 0, 5),
(15, 1, 4, 'Negarse a ceder recursos y mantener una postura firme.', 'Al percibir la determinación de la tripulación, los alienígenas optan por retirarse, evitando un conflicto directo.', 0, 0, 5),
(16, 1, 4, 'Negarse a ceder recursos y mantener una postura firme.', 'La negativa provoca represalias que dañan la nave y a la tripulación. Tripulación -1, Nave -3', 1, 3, 5),

(17, 1, 5, 'Recoger el mineral brillante para analizarlo.', 'El mineral resulta ser una fuente energética útil que aumenta la capacidad de los sistemas de la nave,\nproporcionándole una estabilidad jamás registrada en una nave de esas características. Nave +10', 0, -10, 6),
(18, 1, 5, 'Recoger el mineral brillante para analizarlo.', 'El mineral emite toxinas que afectan con fuerza al capitán de la tripulación. Tripulación -2', 2, 0, 6),
(19, 1, 5, 'Ignorar el mineral y no interferir.', 'Evitan cualquier riesgo innecesario.', 0, 0, 6),
(20, 1, 5, 'Ignorar el mineral y no interferir.', 'El capitán decide finalmente ignorar el mineral y no asumir riesgos.\nParte de la tripulación, en desacuerdo, inicia una trifulca verbal y física que deja una profunda brecha en la confianza y la lealtad dentro del equipo. Tripulación -2', 2, 0, 6),

(21, 1, 6, 'Revisar cuidadosamente el sistema de combustible.', 'Se detecta una fuga menor antes de que sea crítica.', 0, 0, 7),
(22, 1, 6, 'Revisar cuidadosamente el sistema de combustible.', 'Un descuido durante la revisión provoca un accidente grave en una sección del motor, poniendo en riesgo toda la nave. Nave -2', 0, 2, 7),
(23, 1, 6, 'Continuar sin revisar para ahorrar tiempo.', 'El sistema aguanta y sufre desgaste casi imperceptible.', 0, 0, 7),
(24, 1, 6, 'Continuar sin revisar para ahorrar tiempo.', 'El sistema de combustible sufre un fallo crítico, obligando al equipo a realizar una reparación parcial, bajo condiciones extremadamente difíciles. Tripulación -1, Nave -3', 1, 3, 7),

(25, 1, 7, 'Realizar maniobras agresivas para atravesar la tormenta.', 'Las maniobras permiten atravesar la tormenta más rápido de lo previsto, reduciendo la exposición y salvando a la nave de daños mayores.\nEste hecho logra levantar el ánimo de la tripulación en un momento crítico. Tripulación +1', -1, 0, 8),
(26, 1, 7, 'Realizar maniobras agresivas para atravesar la tormenta.', 'Las maniobras sobrecargan los sistemas de control, causando daños estructurales que agravan aún más la situación de la nave. Nave -2', 0, 2, 8),
(27, 1, 7, 'Buscar una ruta más segura alrededor de la tormenta.', 'Evitáis el peligro directo y conseguís no aumentar el desgaste de la nave.', 0, 0, 8),
(28, 1, 7, 'Buscar una ruta más segura alrededor de la tormenta.', 'Logran evitar el peligro directo, pero durante las maniobras de evasión de la tormenta consumen más combustible del previsto. Nave -2', 0, 2, 8),

(29, 1, 8, 'Usar materiales obtenidos de los alienígenas para la reparación.', 'La nave queda reforzada. Nave +2', 0, -2, 9),
(30, 1, 8, 'Usar materiales obtenidos de los alienígenas para la reparación.', 'La tecnología no es compatible y la reparación no se puede completar.', 0, 0, 9),
(31, 1, 8, 'Reparar con el equipo estándar de la nave.', 'La reparación es estable y se realiza con éxito. Nave +2', 0, -2, 9),
(32, 1, 8, 'Reparar con el equipo estándar de la nave.', 'Un error provoca un accidente leve en el motor secundario de la nave. Nave -1', 0, 1, 9),

(33, 1, 9, 'Explorar la caverna luminosa.', 'El hallazgo de cristales energéticos abre nuevas posibilidades y podría tener un impacto decisivo en el futuro.', 0, 0, 11),
(34, 1, 9, 'Explorar la caverna luminosa.', 'Un derrumbe repentino bloquea la salida principal de la caverna, dejando a parte del equipo atrapado en su interior.', 0, 0, 10),
(35, 1, 9, 'Continuar sin explorar.', 'Evitan riesgos innecesarios y continúan la ruta hacia otra zona más al norte.', 0, 0, 11),
(36, 1, 9, 'Continuar sin explorar.', 'La decisión genera frustración, pero el capitán prioriza la exploración de una zona situada más al sur.', 0, 0, 11),

(37, 1, 10, 'Ir en busca de recambios de oxígeno e intentar hacerlos llegar a la tripulación atrapada entre las runas.', 'El oxígeno llega a tiempo y la tripulación atrapada logra resistir hasta ser rescatada.', 0, 0, 12),
(38, 1, 10, 'Ir en busca de recambios de oxígeno e intentar hacerlos llegar a la tripulación atrapada entre las runas.', 'Parte del equipo sufre agotamiento o heridas durante el traslado del oxígeno. Tripulación -3', 3, 0, 12),
(39, 1, 10, 'Confiar en que el nivel de oxígeno sea suficiente, dando prioridad a la movilización de la runa', 'La runa se moviliza con éxito y permite liberar a la tripulación antes de que el oxígeno se agote.\nEl éxito refuerza la confianza en la misión. Tripulación +1', -1, 0, 12),
(40, 1, 10, 'Confiar en el sistema automático.', 'El sistema falla gravemente.', 1, 2, 12),

(41, 1, 11, 'Responder a la señal misteriosa recibida por la nave.', 'La señal proviene de una inteligencia amistosa que proporciona coordenadas para obtener recursos valiosos. Nave +1, Tripulación +1.', -1, -1, 12),
(42, 1, 11, 'Responder a la señal misteriosa recibida por la nave.', 'La señal era una trampa: se activa una interferencia que daña parcialmente los sistemas de comunicación. Nave -1', 0, -1, 12),
(43, 1, 11, 'Analizar la señal sin responder, estudiando su origen desde lejos.', 'La información obtenida permite anticipar riesgos futuros y optimizar la ruta de la nave.', 0, 0, 12),
(44, 1, 11, 'Analizar la señal sin responder, estudiando su origen desde lejos.', 'Se evita cualquier posible trampa y se enfocan en el siguiente paso de la misión.', 0, 0, 12),

(45, 1, 12, 'Abortar misión.', 'Deciden abortar la misión y girar la nave de regreso hacia la Tierra.\nAunque sienten la decepción de no haber completado la expedición, todos los sistemas permanecen estables y la tripulación llega sana y salva.\nTras regresar a su base, pueden planear futuras aventuras con más experiencia y precaución.', 0, 0, NULL),
(46, 1, 12, 'Abortar misión.', 'De regreso a la Tierra, la nave atraviesa inesperadamente una lluvia de meteoritos.\nLos escudos apenas resisten y cada impacto sacude la nave con violencia, provocando fallos en los sistemas vitales.\nFinalmente, la nave queda convertida a cenizas, y la tripulación sobrevive solo en los recuerdos de lo que pudo haber sido.', 0, 0, NULL),
(47, 1, 12, 'Continuar misión.', 'Tras explorar los confines del espacio, la tripulación logra recuperar un mineral o tecnología alienígena de gran valor.\nAunque algunos miembros presentan pequeñas heridas, la nave permanece intacta.\nLa misión culmina con éxito parcial, y el hallazgo es celebrado por científicos y líderes de la expedición.', 0, 0, NULL),
(48, 1, 12, 'Continuar misión.', 'Una serie de accidentes críticos destruye la nave por completo mientras la tripulación lucha por sobrevivir.\nLamentablemente, nadie sobrevive a la misión y la nave queda irreparable.\nLa historia concluye como una tragedia que sirve de advertencia sobre los peligros del espacio y los riesgos de la exploración.', 0, 0, NULL);





INSERT INTO steps (idAdventure, idStep, description, final_step)
VALUES
(1, 999, 'FINAL_TRIPULACION', 1),
(1, 1000, 'FINAL_NAVE', 1);

INSERT INTO answers (idAnswer, idAdventure, idStep, description, resolution_answer, crew_loss, damage_ship, salud, next_step)
VALUES
(999, 1, 999, 'FINAL_TRIPULACION','Los tripulantes caen, víctimas del agotamiento, las enfermedades y los daños físicos sufridos durante la misión;\nla nave flota en el vacío sin rumbo ni destino.', 0, 0, 0, NULL), 
(1000, 1, 1000, 'FINAL_NAVE', 'Con los sistemas al borde del colapso y la nave irreparablemente dañada, la misión fracasa;\nun estallido final consume la nave, borrando toda esperanza de supervivencia.', 0, 0, 0, NULL);


-- Aventura 2, Paso 1
INSERT INTO answers (idAnswer, idAdventure, idStep, description, resolution_answer, crew_loss, damage_ship, next_step)
VALUES
(1,2, 1, 'Investigar personalmente los restos del local para intentar averiguar el origen de la explosión.',
 'Mientras inspeccionas el lugar, descubres una habitación oculta llena de documentación parcialmente quemada.', 0, 0, 2),
(2,2, 1, 'Investigar personalmente los restos del local para intentar averiguar el origen de la explosión.',
 'Documentas el lugar sin incidentes, pero no encuentras nada concluyente antes de escuchar las sirenas de la policía acercándose.', 0, 0, 3),
(3,2, 1, 'Avisar a las autoridades para que se hagan cargo de la investigación.',
 'La policía acordona la zona y limita tu acceso, pero al hablar con los vecinos surgen rumores sobre enfermedades extrañas tras el cierre del local.', 0, 0, 3),
(4,2, 1, 'Avisar a las autoridades para que se hagan cargo de la investigación.',
 'Las autoridades controlan la situación y el asunto se enfría rápidamente, aunque algunos vecinos muestran un nerviosismo evidente.', 0, 0, 3);

-- Aventura 2, Paso 2
INSERT INTO answers (idAnswer, idAdventure, idStep, description, resolution_answer, crew_loss, damage_ship, next_step)
VALUES
(5,2, 2, 'Revisar la documentación encontrada antes de que alguien más llegue al lugar.',
 'Entre los papeles aparecen nombres, fechas y referencias a envíos poco claros.', 0, 0, 4),
(6,2, 2, 'Revisar la documentación encontrada antes de que alguien más llegue al lugar.',
 'La mayoría de documentos están demasiado dañados para sacar conclusiones claras.', 0, 0, 3),
(7,2, 2, 'Guardar la documentación sin revisarla y abandonar el lugar.',
 'Decides no arriesgarte y marcharte, pero la duda empieza a crecer.', 0, 0, 5),
(8,2, 2, 'Guardar la documentación sin revisarla y abandonar el lugar.',
 'Al salir apresuradamente, pierdes parte del material sin darte cuenta.', 0, 0, 3);

-- Aventura 2, Paso 3
INSERT INTO answers (idAnswer, idAdventure, idStep, description, resolution_answer, crew_loss, damage_ship, next_step)
VALUES
(9,2, 3, 'Hablar con vecinos que vivieron el cierre del negocio.',
 'Algunos vecinos mencionan rumores sobre enfermedades inexplicables y acuerdos de silencio que tuvieron lugar años atrás.', 0, 0, 4),
(10,2, 3, 'Hablar con vecinos que vivieron el cierre del negocio.',
 'La mayoría evita el tema o finge no recordar nada.', 0, 0, 4),
(11,2, 3, 'Observar discretamente el ambiente del pueblo sin intervenir.',
 'Notas nerviosismo en ciertas familias relacionadas con el antiguo local.', 0, 0, 4),
(12,2, 3, 'Observar discretamente el ambiente del pueblo sin intervenir.',
 'No detectas nada fuera de lo normal y pierdes tiempo valioso.', 0, 0, 4);

-- Aventura 2, Paso 4
INSERT INTO answers (idAnswer, idAdventure, idStep, description, resolution_answer, crew_loss, damage_ship, next_step)
VALUES
(13,2, 4, 'Abrir el paquete y examinar su contenido.',
 'Encuentras informes médicos antiguos y documentos antiguos que sugieren sin gran claridad que alguien encubrio esos informes para esconder la verdad.', 0, 0, 5),
(14,2, 4, 'Abrir el paquete y examinar su contenido.',
 'Los documentos son confusos y difíciles de interpretar.', 0, 0, 5),
(15,2, 4, 'Guardar el paquete sin abrirlo.',
 'Prefieres no implicarte todavía, pero la tensión aumenta, así que decides salir a dar una vuelta para calmar los nérvios.', 0, 0, 5),
(16,2, 4, 'Guardar el paquete sin abrirlo.',
 'Alguien parece notar tu interés y comienzas a sentirte observado. Dejas el paquete en casa y sales en busca de aire fresco y un poco de claridad.', 0, 0, 5);

-- Aventura 2, Paso 5
INSERT INTO answers (idAnswer, idAdventure, idStep, description, resolution_answer, crew_loss, damage_ship, next_step)
VALUES
(17,2, 5, 'Intentar perder a la persona que te sigue.',
 'Logras despistarlo, pero confirmas que alguien vigila tus movimientos.', 0, 0, 6),
(18,2, 5, 'Intentar perder a la persona que te sigue.',
 'Te tropiezas y te golpeas la cabeza al caer sin entender muy bien que acaba de pasar. Cuando te giras ya lo hay nadie allí.', 0, 0, 13),
(19,2, 5, 'Confrontar directamente a la persona sospechosa.',
 'Al darte la vuelta, sale corriendo. A los pocos metros cae violentamente; el sonido del impacto resuena en la calle vacía. Lo ves levantarse con dificultad, sujetándose el costado, antes de perderse en la oscuridad. Días después, recordarás esa forma de cojear.', 0, 0, 13),
(20,2, 5, 'Confrontar directamente a la persona sospechosa.',
 '“Te asesta un golpe que te derriba. Des del suelo, ves cómo la persona que te seguía tropieza con un bordillo y cae al suelo. Rápidamente se reincorpora cojeando, y desaparece entre los callejones estrechos mientras tu corazón late con fuerza.', 0, 0, 13);

-- Aventura 2, Paso 6
INSERT INTO answers (idAnswer, idAdventure, idStep, description, resolution_answer, crew_loss, damage_ship, next_step)
VALUES
(21,2, 6, 'Visitar a tu padre en la residencia.',
 'Te habla de decisiones pasadas y errores, pero evita entrar en detalles.', 0, 0, 7),
(22,2, 6, 'Visitar a tu padre en la residencia.',
 'La conversación es breve y confusa; percibes un profundo arrepentimiento en sus palabras, aunque la historia que te cuenta resulta inconexa y difícil de seguir.', 0, 0, 7),
(23,2, 6, 'Decidir no visitar a tu padre por el momento.',
 'Te concentras en la investigación, pero sientes que evitas algo importante.', 0, 0, 7),
(24,2, 6, 'Decidir no visitar a tu padre por el momento.',
 'Al día siguiente recibes noticias preocupantes desde la residencia.', 0, 0, 11);

-- Aventura 2, Paso 7
INSERT INTO answers (idAnswer, idAdventure, idStep, description, resolution_answer, crew_loss, damage_ship, next_step)
VALUES
(25,2, 7, 'Leer la carta encontrada entre las pertenencias de tu padre.',
 'La carta menciona promesas, silencios y una culpa que nunca se reparó.', 0, 0, 11),
(26,2, 7, 'Leer la carta encontrada entre las pertenencias de tu padre.',
 'El contenido es ambiguo y deja más preguntas que respuestas.', 0, 0, 10),
(27,2, 7, 'No leer la carta todavía.',
 'Decides esperar, pero la sensación de urgencia aumenta.', 0, 0, 8),
(28,2, 7, 'No leer la carta todavía.',
 'Alguien parece interesado en esa carta más que tú.', 0, 0, 9);

-- Aventura 2, Paso 8
INSERT INTO answers (idAnswer, idAdventure, idStep, description, resolution_answer, crew_loss, damage_ship, next_step)
VALUES
(29,2, 8, 'Hablar públicamente con algunas familias afectadas.',
 'El pueblo comienza a dividirse y surgen bandos.', 0, 0, 12),
(30,2, 8, 'Hablar públicamente con algunas familias afectadas.',
 'La conversación se descontrola y genera miedo.', 0, 0, 12),
(31,2, 8, 'Seguir investigando en silencio.',
 'Descubres conexiones entre ciertas familias y el antiguo negocio.', 0, 0, 11),
(32,2, 8, 'Seguir investigando en silencio.',
 'Pierdes apoyo social y te quedas solo.', 0, 0, 11);



-- Aventura 2, Paso 9
INSERT INTO answers (idAnswer, idAdventure, idStep, description, resolution_answer, crew_loss, damage_ship, next_step)
VALUES
(33,2, 9, 'Hablar con el médico del centro de salud.',
 'Te menciona patrones de enfermedades sin causa clara.', 0, 0, 12),
(34,2, 9, 'Hablar con el médico del centro de salud.',
 'Evita responder con claridad y parece nervioso.', 0, 0, 11),
(35,2, 9, 'Evitar al médico y observar sus movimientos.',
 'Descubres visitas nocturnas sospechosas.', 0, 0, 12),
(36,2, 9, 'Evitar al médico y observar sus movimientos.',
 'Pierdes su rastro y alertas a alguien.', 0, 0, 11);

-- Aventura 2, Paso 10
INSERT INTO answers (idAnswer, idAdventure, idStep, description, resolution_answer, crew_loss, damage_ship, next_step)
VALUES
(37,2, 10, 'Cruzar toda la información recopilada.',
 'Empiezas a ver un patrón inquietante.', 0, 0, 12),
(38,2, 10, 'Cruzar toda la información recopilada.',
 'Los datos no encajan del todo.', 0, 0, 11),
(39,2, 10, 'Descartar parte de la información.',
 'Simplificas el caso, pero pierdes matices importantes.', 0, 0, 11),
(40,2, 10, 'Descartar parte de la información.',
 'Tomas una decisión precipitada.', 0, 0, 11);

-- Aventura 2, Paso 11
INSERT INTO answers (idAnswer, idAdventure, idStep, description, resolution_answer, crew_loss, damage_ship, next_step)
VALUES
(41,2, 11, 'Ignorar las amenazas recibidas.',
 'El riesgo aumenta, pero sigues adelante.', 0, 0, 12),
(42,2, 11, 'Ignorar las amenazas recibidas.',
 'Alguien cercano sufre las consecuencias.', 0, 0, 12),
(43,2, 11, 'Responder de alguna forma a las amenazas.',
 'Provocas una reacción inesperada.', 0, 0, 12),
(44,2, 11, 'Responder de alguna forma a las amenazas.',
 'Te expones demasiado.', 0, 0, 12);

-- Aventura 2, Paso 12 (Finales)
INSERT INTO answers (idAnswer, idAdventure, idStep, description, resolution_answer, crew_loss, damage_ship, next_step)
VALUES
(45,2, 12, 'Decides revelar toda la verdad al público a través de un amigo propietario del periódico provincial.',
 'Decides publicar toda la información a través del periódico provincial.\nRevelas cómo tu padre y algunos trabajadores permitieron que los químicos dañaran a varias familias y cómo los hermanos Brunde, (Hugo Brunde – Médico del pueblo y Lorenzo Brunde – Empresario y gestor de tierras),\ntras la muerte de sus padres, extorsionaron a las ex trabajadoras para quedarse con sus tierras. El pueblo estalla en debates y conflictos; unos exigen justicia mientras otros sienten traición.\nAun así, la luz de la verdad permite que algunas víctimas obtengan reconocimiento y apoyo. Has expuesto todo, pero el precio ha sido la paz del pueblo.', 0, 0, NULL),
(46,2, 12, 'Decides revelar toda la verdad al público a través de un amigo propietario del periódico provincial.',
 'Optas por no implicar a tu padre y concentras tu investigación en los hermanos Brunde (Hugo Brunde – Médico del pueblo y Lorenzo Brunde – Empresario y gestor de tierras).\nPublicas pruebas sobre sus extorsiones a ex trabajadoras de la empresa y su especulación de terrenos.\nLa comunidad se revuelve contra ellos, y finalmente son juzgados o expulsados del pueblo. Aunque los secretos de tu padre permanecen guardados, sientes un alivio moral al proteger su memoria y exponer a quienes realmente manipulaban y amenazaban a los vecinos.\nLa justicia parcial llega, y algunas familias pueden respirar sin miedo, mientras tú cargas con la complejidad del silencio y la verdad incompleta.', 0, 0, NULL),
(47,2, 12, 'Decides guardar todos los secretos y marcharte del pueblo, sin implicarte en nada.',
 'Decides no hacer pública ninguna información.\nGuardas los secretos de tu padre y de los hermanos Brunde (Hugo Brunde – Médico del pueblo y Lorenzo Brunde – Empresario y gestor de tierras), pero abandonas el pueblo, llevándote contigo la memoria de lo sucedido.\nLas familias extorsionadas y enfermas continúan enfrentando las consecuencias, pero tú eliges alejarte del resentimiento y el conflicto. El tiempo será juez de las cicatrices abiertas y de las injusticias no reparadas.\nMientras te alejas, piensas en la vida que podrías reconstruir lejos de Valdemora, con la certeza de que algunas verdades son demasiado pesadas para compartir, y que tu propia paz depende de tu silencio.', 0, 0, NULL),
(48,2, 12, 'Decides guardar todos los secretos y marcharte del pueblo, sin implicarte en nada.',
 'Decides guardar el secreto y abandonar Valdemora, llevándote contigo la carga de todo lo ocurrido.\nDurante dos años intentas rehacer tu vida lejos del pueblo, con la memoria de los abusos de los hermanos Brunde y las injusticias contra las familias ex trabajadoras siempre presentes.\nUn día, recibes una llamada de un amigo propietario del diario provincial: al día siguiente se publicará toda la verdad. Los hermanos seguirán enfrentando las consecuencias, y finalmente se conocerá el papel de tu padre y de quienes silenciaron los daños.\nTe quedas en silencio, observando cómo el tiempo revela lo que tú decidiste proteger.', 0, 0, NULL);

-- Aventura 2, Paso 13
INSERT INTO answers (idAnswer, idAdventure, idStep, description, resolution_answer, crew_loss, damage_ship, next_step)
VALUES
(49,2, 13, 'Decides ir al centro médico del pueblo para que te revisen',
 'El médico más respetado del pueblo te atiende, pero hoy parece estar de mal humor.\nApenas te examina y te despacha con una receta, sin comprobar tu estado real, dejándote con dudas sobre su profesionalidad.', 0, 0, 6),
(50,2, 13, 'Decides ir al centro médico del pueblo para que te revisen',
 'Al llegar, descubres que el médico habitual no está disponible. Te atiende una doctora nueva, amable y profesional, que te receta medicación para aliviar el dolor.\nAl salir, ves a un hombre conocido cojeando, preguntando por el médico principal. Su actitud te resulta extraña y te pone en alerta.', 0, 0, 6),
(51,2, 13, 'Decides no ir al médico y quedarte descansando en casa',
 'El reposo no ayuda y el dolor se intensifica, lo que afecta tu concentración y capacidad para analizar los documentos y pistas que ya tienes.', 0, 0, 9),
(52,2, 13, 'Decides no ir al médico y quedarte descansando en casa',
 'Pasas la tarde descansando y notas que el dolor disminuye.\nAprovechas para revisar mentalmente los sucesos recientes y empiezas a conectar pequeños detalles que antes habías ignorado', 0, 0, 9);

INSERT INTO adventure_characters (idAdventure, idCharacter) VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(1, 5);


INSERT INTO adventure_characters (idAdventure, idCharacter) VALUES
(2, 6),
(2, 7),
(2, 8),
(2, 9);
