---
title: "El GPS no funcionaría sin Einstein"
description: "Cómo sabe tu celular dónde estás, por qué hacen falta cuatro satélites, y por qué sin la teoría de la relatividad el GPS se desviaría unos diez kilómetros por día."
topic: tecnología / ciencia
date: 2026-10-14
---

Hola, bienvenido a Veinte Minutos. Hoy vamos a hablar de algo que usás todos los días, probablemente sin pensarlo demasiado: el GPS. Ese puntito azul en el mapa que te dice dónde estás, que te avisa que en doscientos metros tenés que doblar a la derecha, o que te calcula cuánto falta para llegar.

La idea de hoy es responder tres preguntas. Primero, cómo hace realmente tu celular para saber dónde está. Segundo, por qué un sistema militar terminó en el bolsillo de todo el mundo. Y tercero, la parte que más me gusta: por qué, si los ingenieros no hubieran tenido en cuenta la teoría de la relatividad de Einstein, el GPS dejaría de servir en cuestión de horas.

Vamos por partes.

## Una red de relojes en el cielo

Lo primero que hay que entender es que el GPS no es, en el fondo, un sistema de mapas. Es un sistema de relojes. Muy precisos, muy caros, y que dan vueltas alrededor de la Tierra.

El sistema tiene alrededor de treinta satélites en funcionamiento. Están a unos veinte mil doscientos kilómetros de altura, repartidos en seis planos orbitales distintos, y cada uno da una vuelta completa a la Tierra en aproximadamente doce horas. La distribución está pensada para que, desde casi cualquier punto del planeta y en casi cualquier momento, haya al menos cuatro satélites visibles en el cielo. Normalmente hay bastantes más.

Cada uno de esos satélites lleva a bordo relojes atómicos. Son relojes que miden el tiempo a partir de las oscilaciones de átomos de cesio o de rubidio, y son absurdamente precisos: pueden pasar miles o millones de años antes de que se desfasen un segundo, según el tipo.

¿Y qué hacen los satélites con esos relojes? Algo bastante simple, en realidad. Transmiten todo el tiempo una señal de radio que dice, más o menos: "Soy el satélite tal, estoy en tal posición, y en este momento exacto, según mi reloj, son tales horas, minutos, segundos y fracciones de segundo".

Eso es todo. Los satélites no saben dónde estás vos. No reciben nada de tu celular. Solo hablan, como un faro que emite luz para quien quiera mirarla. Por eso el GPS funciona aunque haya millones de personas usándolo al mismo tiempo: los satélites no tienen que atender a nadie.

## Midiendo distancias con el tiempo

Ahora, ¿cómo pasamos de "el satélite me dice qué hora es" a "estoy en esta esquina"?

La clave es que las ondas de radio viajan a la velocidad de la luz, que son casi trescientos mil kilómetros por segundo. Es rapidísimo, pero no es instantáneo. Desde un satélite a veinte mil kilómetros, la señal tarda alrededor de siete centésimas de segundo en llegarte.

Entonces tu receptor hace esto: recibe el mensaje que dice "esto se envió a tal hora", lo compara con la hora a la que lo recibió, y la diferencia es el tiempo que tardó la señal en viajar. Multiplicás ese tiempo por la velocidad de la luz, y tenés la distancia al satélite.

Pensalo así: si un amigo te grita desde lejos y vos sabés exactamente a qué hora gritó, y sabés la velocidad del sonido, podés calcular a qué distancia está. Es la misma lógica, pero con luz en vez de sonido.

Con un solo satélite sabés que estás a cierta distancia de él. Eso te ubica en algún lugar de una esfera gigante alrededor del satélite. No sirve de mucho.

Con dos satélites, tenés dos esferas, y vos estás en algún punto donde se cruzan. La intersección de dos esferas es un círculo. Todavía no alcanza.

Con tres satélites, la intersección de tres esferas se reduce a dos puntos. Y normalmente uno de esos dos puntos está en el espacio o dentro de la Tierra, así que se descarta solo. Listo, ya sabés dónde estás.

Este método se llama trilateración. No confundir con triangulación, que usa ángulos. Acá todo se basa en distancias.

## El problema del reloj barato

Pero hay una trampa. Para que esto funcione, tu receptor tiene que saber la hora con una precisión tremenda. Y el reloj que tiene tu celular es un cristal de cuarzo común, de esos que cuestan centavos. Es bueno para mostrarte la hora en la pantalla, pero para el GPS es un desastre.

¿Por qué importa tanto? Porque la luz recorre trescientos metros en un microsegundo, es decir, en una millonésima de segundo. Si tu reloj se equivoca por una millonésima de segundo, la distancia calculada se equivoca por trescientos metros. Y si se equivoca por una milésima de segundo, que para un reloj de cuarzo no es nada, el error es de trescientos kilómetros.

La solución es muy elegante, y es la razón por la que siempre se habla de cuatro satélites y no de tres.

El receptor trata la hora como si fuera una incógnita más. En vez de resolver solo tres valores, que serían la posición en tres dimensiones, resuelve cuatro: las tres coordenadas de posición y el error de su propio reloj. Y para resolver un sistema con cuatro incógnitas necesitás cuatro ecuaciones, o sea, cuatro satélites.

El resultado es fascinante: tu celular, con un reloj de cuarzo barato, termina sabiendo la hora casi con la precisión de un reloj atómico, porque la "toma prestada" de los satélites. De hecho, muchas redes de telecomunicaciones, sistemas bancarios y redes eléctricas usan el GPS justamente para sincronizar sus relojes, más que para saber dónde están.

## De arma militar a herramienta de todos

Hagamos una pausa en la física y vamos un poco a la historia.

El GPS lo desarrolló el Departamento de Defensa de los Estados Unidos. El primer satélite del sistema se lanzó en 1978, y la constelación completa se declaró plenamente operativa recién en 1995. La idea original era militar: poder guiar barcos, aviones, tropas y, eventualmente, misiles con precisión en cualquier parte del mundo.

¿Cómo terminó en tu celular? Hay un episodio que fue un punto de quiebre. En 1983, un avión de pasajeros de Korean Air Lines, el vuelo 007, se desvió de su ruta por errores de navegación y terminó entrando en el espacio aéreo de la Unión Soviética. Fue derribado, y murieron las 269 personas que iban a bordo.

Poco después, el gobierno de Ronald Reagan anunció que el GPS, cuando estuviera listo, se iba a poder usar para la aviación civil, justamente para evitar que algo así volviera a pasar.

Pero había un detalle. Durante años, la señal para uso civil tenía un error introducido a propósito. Se llamaba "disponibilidad selectiva". Básicamente, el ejército degradaba la precisión de la señal pública para que nadie pudiera usarla con fines militares. Con eso, un receptor civil podía equivocarse por unos cien metros.

En mayo del año 2000 se desactivó ese error intencional, y de un día para el otro la precisión civil pasó a ser de unos diez metros o menos. Ese cambio es, en buena medida, lo que hizo posible toda la industria que vino después: navegadores para auto, aplicaciones de mapas, delivery, transporte por aplicación, relojes deportivos que te miden el ritmo cuando salís a correr. Todo eso depende de que la señal sea precisa y gratuita.

Hoy, además, el GPS no está solo. Rusia tiene su propio sistema, que se llama GLONASS. La Unión Europea tiene Galileo. China tiene BeiDou. Y la mayoría de los celulares modernos escuchan a varios de estos sistemas al mismo tiempo. Más satélites visibles significa una posición más rápida y más precisa, sobre todo en lugares difíciles, como una ciudad con edificios altos que tapan buena parte del cielo.

## Y acá entra Einstein

Bien. Volvamos a los relojes, porque acá viene lo más interesante.

Dijimos que todo el sistema depende de que los relojes de los satélites estén perfectamente sincronizados con el tiempo en la Tierra. Un error de una millonésima de segundo son trescientos metros de error en la posición.

El problema es que, según Einstein, el tiempo no pasa igual para todos. Y no lo digo en sentido poético. Lo digo literalmente: un reloj en un satélite GPS y un reloj en tu muñeca no marcan el tiempo al mismo ritmo. Y hay dos efectos distintos que lo explican, que además van en direcciones opuestas.

### Primer efecto: la velocidad

El primero viene de la relatividad especial, la teoría que Einstein publicó en 1905. Una de sus consecuencias es que, cuanto más rápido se mueve un reloj respecto de vos, más lento lo ves avanzar. Se llama dilatación temporal por velocidad.

Para las velocidades de la vida cotidiana, el efecto es tan chico que no se nota. Pero los satélites GPS se mueven a casi cuatro kilómetros por segundo, que son unos catorce mil kilómetros por hora. A esa velocidad, el efecto ya se puede medir.

El resultado es que, visto desde la Tierra, el reloj del satélite se atrasa unos siete microsegundos por día. Siete millonésimas de segundo. Parece nada, ¿no?

### Segundo efecto: la gravedad

El segundo efecto viene de la relatividad general, que Einstein publicó una década después, en 1915. Esta teoría dice que la gravedad también afecta el paso del tiempo: cuanto más intenso es el campo gravitatorio, más lento pasa el tiempo.

Acá en la superficie de la Tierra estamos más "metidos" en el campo gravitatorio del planeta. Los satélites, a veinte mil kilómetros de altura, sienten una gravedad bastante más débil. Entonces, para ellos, el tiempo pasa un poco más rápido que para nosotros.

¿Cuánto más rápido? Unos cuarenta y cinco microsegundos por día.

### La cuenta final

Ahora juntamos los dos efectos. La velocidad hace que el reloj del satélite se atrase unos siete microsegundos por día. La gravedad hace que se adelante unos cuarenta y cinco. Gana la gravedad, y el resultado neto es que el reloj del satélite se adelanta unos treinta y ocho microsegundos por día respecto de un reloj en la Tierra.

Ahora hagamos la cuenta que importa. Dijimos que un microsegundo equivale a unos trescientos metros de error. Treinta y ocho microsegundos son más de once kilómetros.

Es decir: si nadie corrigiera estos efectos relativistas, el GPS acumularía un error de alrededor de diez u once kilómetros por día. Al terminar la primera mañana ya estaría desviado varios cientos de metros. Al día siguiente, te mandaría a otro barrio. En una semana, a otra ciudad. El sistema sería completamente inútil.

## Cómo lo corrigen

La solución que se eligió es bastante ingeniosa en su simpleza.

Los relojes atómicos de los satélites funcionan a partir de una frecuencia de referencia. En el GPS, esa frecuencia nominal es de diez coma veintitrés megahertz. Lo que se hace es ajustar esa frecuencia antes del lanzamiento, en tierra, para que el reloj funcione deliberadamente un poquito más lento.

Ese "un poquito" es un valor diminuto, del orden de cuatro partes y media en diez mil millones. Una vez en órbita, los efectos relativistas aceleran el reloj exactamente lo necesario para que, visto desde la Tierra, marque el ritmo correcto.

Es como afinar una guitarra un tono más abajo porque sabés que el calor del escenario la va a desafinar hacia arriba durante el concierto.

Además de esta corrección fija, hay otras. Las órbitas no son círculos perfectos, sino ligeramente elípticas. Entonces el satélite a veces está un poco más cerca y a veces un poco más lejos de la Tierra, y va un poco más rápido o un poco más lento. Eso genera pequeñas variaciones adicionales que el propio receptor corrige con una fórmula. Y hay un efecto más, relacionado con la rotación de la Tierra mientras la señal viaja, que también se tiene en cuenta.

## Los que no le creían a Einstein

Hay una historia muy linda alrededor de todo esto.

Cuando se estaba desarrollando el sistema, en los años setenta, la relatividad ya llevaba décadas de confirmaciones experimentales. En 1971, por ejemplo, dos científicos llamados Joseph Hafele y Richard Keating subieron relojes atómicos de cesio a aviones comerciales, dieron la vuelta al mundo hacia el este y hacia el oeste, y compararon esos relojes con otros que habían quedado en tierra. Las diferencias coincidieron con lo que predecía Einstein.

Aun así, entre algunos ingenieros y militares había dudas. Una cosa es una teoría elegante en un pizarrón, y otra es apostar un sistema de navegación militar carísimo a que esa teoría funciona exactamente como dice.

Entonces, en 1977, se lanzó un satélite experimental de prueba, llamado NTS-2, con un reloj atómico a bordo. Y se hizo algo muy astuto: se incluyó un mecanismo para poder activar o no la corrección relativista desde tierra. Al principio la dejaron apagada, para ver qué pasaba.

Durante unas tres semanas midieron el reloj del satélite. Y efectivamente, se adelantaba al ritmo que predecía la teoría, con una diferencia de menos del uno por ciento respecto del valor calculado. Después de eso, encendieron la corrección. Y desde entonces, todos los satélites GPS se lanzan con ese ajuste incorporado de fábrica.

Me gusta esta historia porque muestra algo muy sano de la ingeniería: no alcanza con que algo sea cierto en teoría. Hay que medirlo. Y en este caso, la medición le dio la razón a un señor que había publicado sus ideas setenta años antes, sin imaginar ni de lejos que iban a servir para que alguien encuentre una farmacia abierta un domingo.

## Por qué a veces el GPS falla igual

Ahora, si todo esto está tan bien resuelto, ¿por qué a veces el puntito azul se vuelve loco? ¿Por qué en el centro de la ciudad te dice que estás en la vereda de enfrente, o que estás dentro de un edificio?

Hay varias razones, y ninguna tiene que ver con Einstein.

La primera es la atmósfera. Dijimos que la señal viaja a la velocidad de la luz, pero eso es en el vacío. Cuando atraviesa la ionosfera, que es una capa de la atmósfera cargada eléctricamente, y después la troposfera, que es la parte más baja donde está el clima, se frena un poquito. Ese retraso varía según la hora del día, la actividad solar y el clima. Los receptores usan modelos para estimarlo, y los equipos más avanzados reciben señales en dos frecuencias distintas, porque la ionosfera afecta de manera diferente a cada una, y comparándolas se puede calcular y eliminar buena parte del error.

La segunda razón es el rebote. En una ciudad con edificios altos, la señal muchas veces no te llega en línea recta, sino rebotando contra paredes y vidrios. Ese camino es más largo, entonces el receptor calcula una distancia equivocada. Esto se llama efecto multitrayecto, y es la razón principal por la que el GPS anda peor entre edificios.

La tercera es simplemente la falta de cielo visible. Dentro de un túnel, de un estacionamiento subterráneo o de una casa, las señales llegan muy débiles o directamente no llegan. Por eso los celulares combinan el GPS con otras fuentes: las antenas de telefonía, las redes WiFi cercanas, e incluso los sensores de movimiento del propio teléfono, para estimar dónde estás mientras no tienen buena señal satelital.

Y hay un dato curioso: la señal GPS que llega al suelo es extremadamente débil. Se suele comparar con intentar ver, desde miles de kilómetros, la luz de una lamparita. Los receptores logran captarla gracias a técnicas de procesamiento de señales muy sofisticadas, porque el mensaje se repite de una forma conocida y eso permite "pescarlo" en medio del ruido.

## Lo que hay detrás del puntito azul

Cerremos con una reflexión.

La próxima vez que abras el mapa en el auto y veas ese puntito azul moviéndose, pensá en todo lo que está pasando para que eso funcione.

Hay una treintena de satélites a veinte mil kilómetros de altura, cada uno con relojes atómicos que fueron desafinados a propósito antes del lanzamiento. Están corrigiendo un efecto que predijo un físico en 1905, y otro que predijo diez años después, cuando no existían ni los aviones comerciales. Tu celular está escuchando señales tan débiles que casi se pierden en el ruido, resolviendo un sistema de ecuaciones con cuatro incógnitas varias veces por segundo, y descontando el retraso que le mete la atmósfera.

Y todo eso, para decirte que en doscientos metros tenés que doblar a la derecha.

Hay algo muy lindo en eso. La relatividad suele presentarse como algo lejano, de agujeros negros, viajes espaciales y paradojas con gemelos. Pero en realidad es una de las teorías físicas más útiles en la vida cotidiana. Sin ella, no tendrías navegación en el auto, ni seguimiento del pedido que estás esperando, ni el registro de tu última salida a correr.

Así que, de alguna manera, cada vez que usás el GPS estás haciendo un pequeño experimento que confirma, una vez más, que Einstein tenía razón.

Esto fue Veinte Minutos. Gracias por escuchar, buen viaje, y nos encontramos mañana con un tema nuevo.
