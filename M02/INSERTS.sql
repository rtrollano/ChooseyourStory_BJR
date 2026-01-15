USE proyecto_bjr2;

INSERT INTO characters (idCharacter, CharacterName) VALUES
(1, 'Capitán: Shelton'),
(2, 'Ingeniero Jefe: Ramirez'),
(3, 'Médico de la Nave: Tanaka'),
(4, 'Especialista en Comunicaciones: Kane'),
(5, 'Médico de Vuelo: Patel'),
(6, 'Elias Mercer – detective veterano, metódico.'),
(7, 'Cleo Bradford – joven analista de crímenes, intuitiva.'),
(8, 'Dante Ruiz – detective rebelde que sigue su instinto.'),
(9, 'Colin Drake – oficial de policía rutinario, de moral ambigua.');

INSERT INTO adventure (idAdventure, Name, Description, idCharacter, codAdventure) VALUES
(1, 'Expedición al Sector Z-47','Una peligrosa misión espacial con decisiones críticas y encuentros inesperados.',1,1),
(2, 'Expedición al Sector Z-47','Una peligrosa misión espacial con decisiones críticas y encuentros inesperados.',2,1),
(3, 'Expedición al Sector Z-47','Una peligrosa misión espacial con decisiones críticas y encuentros inesperados.',3,1),
(4, 'Expedición al Sector Z-47','Una peligrosa misión espacial con decisiones críticas y encuentros inesperados.',4,1),
(5, 'Expedición al Sector Z-47','Una peligrosa misión espacial con decisiones críticas y encuentros inesperados.',5,1),
(6, 'La carta anónima','En un pequeño pueblo marcado por el silencio y las viejas lealtades, un suceso inesperado despierta\nsecretos enterrados durante años y obliga a enfrentar decisiones del pasado que nunca llegaron a saldarse.',6,2),
(7, 'La carta anónima','En un pequeño pueblo marcado por el silencio y las viejas lealtades, un suceso inesperado despierta\nsecretos enterrados durante años y obliga a enfrentar decisiones del pasado que nunca llegaron a saldarse.',7,2),
(8, 'La carta anónima','En un pequeño pueblo marcado por el silencio y las viejas lealtades, un suceso inesperado despierta\nsecretos enterrados durante años y obliga a enfrentar decisiones del pasado que nunca llegaron a saldarse.',8,2),
(9, 'La carta anónima','En un pequeño pueblo marcado por el silencio y las viejas lealtades, un suceso inesperado despierta\nsecretos enterrados durante años y obliga a enfrentar decisiones del pasado que nunca llegaron a saldarse.',9,2)
;


INSERT INTO game_states_master (idState, name, initial_value) VALUES
(1, 'nave', 10),
(2, 'tripulacion', 8),
(3, 'Salud', 5);


INSERT INTO adventure_states (idAdventure, idState) VALUES
(1, 1),  -- 'nave'
(1, 2),  -- 'tripulacion'
(2, 3); -- 'salud'


INSERT INTO adventure_context (idAdventure, context_text) VALUES
(1, 'Tras años de exhaustiva preparación, cinco tripulantes de la Base Helios se disponen a embarcarse en una misión sin precedentes: explorar el sector Z-47, una región del espacio jamás cartografiada.
Los estudios preliminares sugieren que se trata de una zona rica en recursos energéticos capaces de transformar para siempre la forma en que la Tierra produce y utiliza la energía.
Confiados en el éxito de la expedición y en la solidez de su entrenamiento, la nave Astraeon despega sin incidentes, adentrándose en lo desconocido…'),
(2, 'Texto de introducción para la aventura 2');



-- Aventura 1
INSERT INTO steps (idStep, idAdventure, description, final_step) VALUES
(1, 1, 'Durante las primeras horas del viaje, un ruido metálico irregular comienza a escucharse desde una de las secciones externas de la nave. Los sensores no detectan nada concluyente, pero la tripulación empieza a inquietarse.', 0),
(2, 1, 'Tras evaluar la situación, la tripulación debate si aterrizar en un planeta cercano para revisar sistemas y descansar, o continuar el viaje sin desviarse del plan original.', 0),
(3, 1, 'Al avanzar por el sector, detectan señales de vida inteligente. Pronto se encuentran frente a una forma de vida alienígena desconocida, cuyo comportamiento es difícil de interpretar.', 0),
(4, 1, 'Las comunicaciones con los alienígenas evolucionan hacia una posible negociación. Ambas partes parecen desconfiar, pero una alianza podría traer beneficios… o graves consecuencias.', 0),
(5, 1, 'En la superficie de un pequeño planeta, el equipo detecta un objeto brillante parcialmente enterrado. Su origen parece ser desconocido y llama su atención.', 0),
(6, 1, 'Antes de continuar, surge la duda sobre el estado real del combustible. Una revisión podría prevenir problemas futuros, aunque también implica perder más tiempo.', 0),
(7, 1, 'Una tormenta atmosférica inesperada golpea la nave. Los sistemas tiemblan y el margen de error es mínimo.', 0),
(8, 1, 'El deterioro progresivo fuerza al equipo a ejecutar una reparación vital de la nave.', 0),
(9, 1, 'Durante la exploración, se descubre una caverna iluminada por cristales naturales que emiten energía.', 0),
(10, 1, 'Las alarmas se activan: los niveles de oxígeno de los trajes fluctúan peligrosamente. Una mala decisión podría ser fatal.', 0),
(11, 1, 'La nave recibe una señal desconocida de origen incierto que podría ser una trampa o una oportunidad.', 0),
(12, 1, 'Tras todo lo ocurrido, la tripulación debe tomar la decisión final: Abortar la misión y regresar a casa o continuar hasta el final, asumiendo todos los riesgos.', 1);

-- Aventura 2
INSERT INTO steps (idStep, idAdventure, description, final_step) VALUES
(1, 2, 'Ha llegado la primera carta anónima al pueblo, con amenazas veladas hacia los vecinos. ¿Qué hacer primero?', 0),
(2, 2, 'Deciden revisar los buzones y rastrear la procedencia de la carta. ¿Investigar personalmente o pedir ayuda a las autoridades?', 0),
(3, 2, 'Alguien del pueblo parece nervioso y esquiva las preguntas. ¿Confrontarlo directamente o observarlo en secreto?', 0),
(4, 2, 'Se encuentra una segunda carta, con detalles que solo alguien cercano podría saber. ¿Difundir la noticia para generar presión o mantener la confidencialidad?', 0),
(5, 2, 'Un vecino ofrece información a cambio de protección. ¿Aceptar la información o sospechar de una trampa?', 0),
(6, 2, 'Se descubre un escondite con pruebas del autor. ¿Interrogar a los posibles culpables o recopilar pruebas discretamente?', 0),
(7, 2, 'Una carta amenaza con revelar un secreto personal del protagonista. ¿Ignorar la amenaza o investigarla de inmediato?', 0),
(8, 2, 'El pueblo se divide: algunos apoyan al protagonista y otros desconfían. ¿Organizar una reunión pública o actuar en privado?', 0),
(9, 2, 'Se recibe una pista final que apunta al culpable. ¿Seguir la pista de inmediato o planear un seguimiento más seguro?', 0),
(10, 2, 'El autor está cerca de ser descubierto. ¿Confrontarlo directamente o preparar una estrategia para atraparlo con evidencia?', 1);




INSERT INTO answers (idAnswer, idAdventure, idStep, description, resolution_answer, crew_loss, damage_ship, salud, next_step) VALUES
-- ===== Paso 1 =====
(1, 1, 1, 'Enviar al ingeniero al exterior de la nave para investigar el origen del ruido.',
 'El mecánico localiza una placa suelta antes de que cause daños mayores y refuerza la zona.',
 0, 0, 0, 2),

(2, 1, 1, 'Enviar al ingeniero al exterior de la nave para investigar el origen del ruido.',
 'Durante la reparación, una pieza se desplaza bruscamente y le atrapa la mano al ingeniero del equipo, dejándole la mano gravemente herida. Tripulación -2',
 2, 0, 0, 2),

(3, 1, 1, 'Ignorar el ruido y continuar el viaje confiando en que no sea grave.',
 'El fallo resulta ser menor y no vuelve a manifestarse durante el trayecto.',
 0, 0, 0, 2),

(4, 1, 1, 'Ignorar el ruido y continuar el viaje confiando en que no sea grave.',
 'El problema se agrava con el tiempo y provoca una pequeña fuga de combustible. Nave -2',
 0, 2, 0, 2),

-- ===== Paso 2 =====
(5, 1, 2, 'Aterrizar en un planeta cercano para revisar sistemas y permitir que la tripulación descanse.',
 'El aterrizaje es estable y el entorno resulta seguro.',
 0, 0, 0, 3),

(6, 1, 2, 'Aterrizar en un planeta cercano para revisar sistemas y permitir que la tripulación descanse.',
 'El terreno es muy inestable; la nave sufre daños y un tripulante resulta herido durante el descenso. Tripulación -1. Nave -3',
 1, 2, 0, 3),

(7, 1, 2, 'Continuar el viaje sin desviarse para no perder tiempo.',
 'Avanzan según lo previsto sin incidentes inmediatos.',
 0, 0, 0, 5),

(8, 1, 2, 'Continuar el viaje sin desviarse para no perder tiempo.',
 'Un desperfecto menor en el motor se intensifica por el exceso de calor generado tras un vuelo prolongado.. Nave -2',
 0, 2, 0, 5),

-- ===== Paso 3 =====
(9, 1, 3, 'Intentar comunicarse y confiar en los seres alienígenas.',
 'Los alienígenas comparten tecnología que mejora el rendimiento de la nave. Nave +3',
 0, -3, 0, 4),

(10, 1, 3, 'Intentar comunicarse y confiar en los seres alienígenas.',
 'Un malentendido provoca un ataque a distancia por parte de los alienígenas con una tecnologia extraña que hiere a uno de los tripulante. Tripulación -2',
 2, 0, 0, 4),

(11, 1, 3, 'Retirarse con cautela y evitar cualquier contacto.',
 'La tripulación evita posibles riesgos y continúa el viaje.',
 0, 0, 0, 5),

(12, 1, 3, 'Retirarse con cautela y evitar cualquier contacto.',
 'Los alienígenas interpretan la retirada como hostilidad y atacan brevemente la nave. Nave -1',
 0, 1, 0, 5),

-- ===== Paso 4 =====
(13, 1, 4, 'Ceder parte de los recursos para mantener la paz.',
 'La relación se fortalece y los alienígenas prometen no interferir en su camíno.',
 0, 0, 0, 5),

(14, 1, 4, 'Ceder parte de los recursos para mantener la paz.',
 'El capitán entrega un recurso clave para evitar el conflicto con los alienígenas.\nLa decisión deja una sensación de duda en la tripulación y debilita la confianza del equipo. Tripulación -1',
 1, 0, 0, 5),

(15, 1, 4, 'Negarse a ceder recursos y mantener una postura firme.',
 'Al percibir la determinación de la tripulación, los alienígenas optan por retirarse, evitando un conflicto directo.',
 0, 0, 0, 5),

(16, 1, 4, 'Negarse a ceder recursos y mantener una postura firme.',
 'La negativa provoca represalias que dañan la nave y a la tripulación. Tripulación -1, Nave -3',
 1, 3, 0, 5),
 
-- ===== Paso 5 =====
(17, 1, 5, 'Recoger el mineral brillante para analizarlo.', 
'El mineral resulta ser una fuente energética útil que aumenta la capacidad de los sistemas de la nave,\nproporcionándole una estabilidad jamás registrada en una nave de esas características. Nave +10', 
0, -10, 0, 6),

(18, 1, 5, 'Recoger el mineral brillante para analizarlo.', 
'El mineral emite toxinas que afectan con fuerza al capitán de la tripulación. Tripulación -2', 
2, 0, 0, 6),

(19, 1, 5, 'Ignorar el mineral y no interferir.', 
'Evitan cualquier riesgo innecesario.', 
0, 0, 0, 6),

(20, 1, 5, 'Ignorar el mineral y no interferir.', 
'El capitán decide finalmente ignorar el mineral y no asumir riesgos.\nParte de la tripulación, en desacuerdo, inicia una trifulca verbal y física que deja una profunda brecha en la confianza y la lealtad dentro del equipo. Tripulación -2', 
2, 0, 0, 6),

-- ===== Paso 6 =====
(21, 1, 6, 'Revisar cuidadosamente el sistema de combustible.', 
'Se detecta una fuga menor antes de que sea crítica.', 0, 0, 0, 7),

(22, 1, 6, 'Revisar cuidadosamente el sistema de combustible.', 'Un descuido durante la revisión provoca un accidente grave en una sección del motor, poniendo en riesgo toda la nave. Nave -2', 
0, 2, 0, 7),

(23, 1, 6, 'Continuar sin revisar para ahorrar tiempo.', 
'El sistema aguanta y sufre desgaste casi imperceptible.',
 0, 0, 0, 7),
 
(24, 1, 6, 'Continuar sin revisar para ahorrar tiempo.',
 'El sistema de combustible sufre un fallo crítico, obligando al equipo a realizar una reparación parcial, bajo condiciones extremadamente difíciles. Tripulación -1, Nave -3',
 1, 3, 0, 7),

-- ===== Paso 7 =====
(25, 1, 7, 'Realizar maniobras agresivas para atravesar la tormenta.', 
'Las maniobras permiten atravesar la tormenta más rápido de lo previsto, reduciendo la exposición y salvando a la nave de daños mayores. Este hecho logra levantar el ánimo de la tripulación en un momento crítico. Tripulación +1', 
-1, 0, 0, 8),

(26, 1, 7, 'Realizar maniobras agresivas para atravesar la tormenta.', 
'Las maniobras sobrecargan los sistemas de control, causando daños estructurales que agravan aún más la situación de la nave. Nave -2', 
0, 2, 0, 8),

(27, 1, 7, 'Buscar una ruta más segura alrededor de la tormenta.', 
'Evitais el peligro directo y conseguis no augmentar el desgaste de la nave.', 
0, 0, 0, 8),

(28, 1, 7, 'Buscar una ruta más segura alrededor de la tormenta.',
 'Logran evitar el peligro directo, pero durante las maniobras de evasión de la tormenta consumen más combustible del previsto. Nave -2', 
 0, 2, 0, 8),

-- ===== Paso 8 =====
(29, 1, 8, 'Usar materiales obtenidos de los alienígenas para la reparación.', 
'La nave queda reforzada. Nave +2', 
0, -2, 0, 9),

(30, 1, 8, 'Usar materiales obtenidos de los alienígenas para la reparación.', 
'La tecnología no es compatible y la reparación no se puede completar.',
 0, 0, 0, 9),
 
(31, 1, 8, 'Reparar con el equipo estándar de la nave.', 
'La reparación es estable y se realiza con éxito. Nave +2',
 0, -2, 0, 9),
 
(32, 1, 8, 'Reparar con el equipo estándar de la nave.', 
'Un error provoca un accidente leve en el motor secundario de la nave. Nave -1',
 0, 1, 0, 9),

-- ===== Paso 9 =====
(33, 1, 9, 'Explorar la caverna luminosa.', 
'El hallazgo de cristales energéticos abre nuevas posibilidades y podría tener un impacto decisivo en el futuro.', 
0, 0, 0, 11),

(34, 1, 9, 'Explorar la caverna luminosa.',
 'Un derrumbe repentino bloquea la salida principal de la caverna, dejando a parte del equipo atrapado en su interior.',
 0, 0, 0, 10),
 
(35, 1, 9, 'Continuar sin explorar.', 
'Evitan riesgos innecesarios y continúan la ruta hacia otra zona más al norte.',
 0, 0, 0, 11),
 
(36, 1, 9, 'Continuar sin explorar.', 
'La decisión genera frustración, pero el capitán prioriza la exploración de una zona situada más al sur.', 
0, 0, 0, 11),

-- ===== Paso 10 =====
(37, 1, 10, 'Ir en busca de recambios de oxígeno e intentar hacerlos llegar a la tripulación atrapada entre las runas.',
 'El oxígeno llega a tiempo y la tripulación atrapada logra resistir hasta ser rescatada.', 
 0, 0, 0, 12),
 
(38, 1, 10, 'Ir en busca de recambios de oxígeno e intentar hacerlos llegar a la tripulación atrapada entre las runas.', 
'Parte del equipo sufre agotamiento o heridas durante el traslado del oxígeno. Tripulación -3',
 3, 0, 0, 12),
 
(39, 1, 10, 'Confiar en que el nivel de oxígeno sea suficiente, dando prioridad a la movilización de la runa',
 'La runa se moviliza con éxito y permite liberar a la tripulación antes de que el oxígeno se agote. El éxito refuerza la confianza en la misión. Tripulación +1',
 1, 0, 0, 12),
 
(40, 1, 10, 'Confiar en el sistema automático.', 
'El sistema falla gravemente.', 
1, 2, 0, 12),

-- ===== Paso 11 =====
(41, 1, 11, 'Responder a la señal misteriosa recibida por la nave.', 
'La señal proviene de una inteligencia amistosa que proporciona coordenadas para obtener recursos valiosos. Nave +1, Tripulación +1.',
 -1, -1, 0, 12),
 
(42, 1, 11, 'Responder a la señal misteriosa recibida por la nave.', 
'La señal era una trampa: se activa una interferencia que daña parcialmente los sistemas de comunicación. Nave -1', 
0, -1, 0, 12),

(43, 1, 11, 'Analizar la señal sin responder, estudiando su origen desde lejos.', 
'La información obtenida permite anticipar riesgos futuros y optimizar la ruta de la nave.', 
0, 0, 0, 12),

(44, 1, 11, 'Analizar la señal sin responder, estudiando su origen desde lejos.', 
'Se evita cualquier posible trampa y se enfocan en el siguiente paso de la misión.', 
0, 0, 0, 12),

-- ===== Paso 12 =====
(45, 1, 12, 'Abortar misión.', 
'Deciden abortar la misión y girar la nave de regreso hacia la Tierra. Aunque sienten la decepción de no haber completado la expedición, todos los sistemas permanecen estables y la tripulación llega sana y salva. Tras regresar a su base, pueden planear futuras aventuras con más experiencia y precaución.',
 0, 0, 0, NULL),
 
(46, 1, 12, 'Abortar misión.', 
'De regreso a la Tierra, la nave atraviesa inesperadamente una lluvia de meteoritos. Los escudos apenas resisten y cada impacto sacude la nave con violencia, provocando fallos en los sistemas vitales. Finalmente, la nave queda convertida a cenizas, y la tripulación sobrevive solo en los recuerdos de lo que pudo haber sido.', 
0, 0, 0, NULL),

(47, 1, 12, 'Continuar misión.',
 'Tras explorar los confines del espacio, la tripulación logra recuperar un mineral o tecnología alienígena de gran valor. Aunque algunos miembros presentan pequeñas heridas, la nave permanece intacta. La misión culmina con éxito parcial, y el hallazgo es celebrado por científicos y líderes de la expedición.',
 0, 0, 0, NULL),
 
(48, 1, 12, 'Continuar misión.',
 'Una serie de accidentes críticos destruye la nave por completo mientras la tripulación lucha por sobrevivir. Lamentablemente, nadie sobrevive a la misión y la nave queda irreparable. La historia concluye como una tragedia que sirve de advertencia sobre los peligros del espacio y los riesgos de la exploración.',
 0, 0, 0, NULL);
 
 
 
 
 
 
 
 INSERT INTO answers VALUES
-- ===== Paso 1 =====
(101, 2, 1, 'Leer la carta cuidadosamente y analizar el contenido.',
 'Descubres pistas sobre la posible fuente de la carta. Confianza +1',
 0, 0, -1, 2),

(102, 2, 1, 'Leer la carta cuidadosamente y analizar el contenido.',
 'Interpretas mal las pistas y pierdes tiempo valioso. Confianza -1',
 0, 0, 1, 2),

(103, 2, 1, 'Ignorar la carta por considerarla una broma.',
 'La carta era seria; pierdes información crítica. Confianza -1',
 0, 0, 1, 2),

(104, 2, 1, 'Ignorar la carta por considerarla una broma.',
 'Evitas entrar en pánico y te concentras en otras pistas. Confianza +0',
 0, 0, 0, 2),

-- ===== Paso 2 =====
(105, 2, 2, 'Investigar personalmente los buzones.',
 'Encuentras rastros que apuntan al autor de las cartas. Confianza +1',
 0, 0, -1, 3),

(106, 2, 2, 'Investigar personalmente los buzones.',
 'Te descubren husmeando y sospechan de ti. Confianza -1',
 0, 0, 1, 3),

(107, 2, 2, 'Pedir ayuda a las autoridades.',
 'Recibes apoyo y la investigación avanza más rápido. Confianza +1',
 0, 0, -1, 3),

(108, 2, 2, 'Pedir ayuda a las autoridades.',
 'Las autoridades distraen la investigación con procedimientos burocráticos. Confianza -1',
 0, 0, 1, 3);