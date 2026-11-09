---
title: "El código QR: el cuadradito que nació en una fábrica"
description: "Cómo un ingeniero japonés inventó el código QR mirando un tablero de Go, qué esconden sus tres cuadrados de las esquinas y por qué se puede leer aunque esté roto o manchado."
topic: tecnología / códigos QR
date: 2026-11-09
---

Hola, bienvenido a Veinte Minutos.

Pensá en la última vez que escaneaste un código QR. Capaz fue para ver el menú de un restaurante, para pagar un café, para entrar a un recital o para conectarte al wifi de la casa de un amigo. Levantaste el celular, apuntaste a un cuadradito lleno de manchas blancas y negras, y en menos de un segundo apareció lo que buscabas. Ni lo pensaste.

Pero ese cuadradito es una pequeña obra de ingeniería. Tiene partes con funciones precisas, tiene un sistema para orientarse solo, tiene una forma de protegerse contra los errores que es la misma que se usó para mandar fotos desde sondas espaciales, y además está diseñado para que lo puedas leer torcido, de costado, al revés o con una mancha de café encima.

Y lo más curioso es dónde nació. No nació en un laboratorio de Silicon Valley ni pensando en teléfonos. Nació en una fábrica de autopartes en Japón, a mediados de los años noventa, para resolver un problema bastante aburrido: llevar la cuenta de miles de piezas en una línea de montaje.

Hoy vamos a desarmar ese cuadradito pieza por pieza. Vamos a ver de dónde viene, cómo hace la cámara para encontrarlo, dónde guarda la información y por qué sigue funcionando aunque le falte un pedazo.

## Antes del cuadrado, estaban las rayas

Para entender al código QR hay que empezar por su abuelo, el código de barras. Ese que tienen todos los productos del supermercado, con sus rayitas verticales de distinto grosor.

La idea del código de barras se patentó en Estados Unidos a principios de los años cincuenta. Hay una anécdota muy linda sobre su origen. Uno de sus inventores, Joseph Woodland, estaba pensando cómo codificar información de una forma que una máquina pudiera leer. Estaba sentado en una playa, y se puso a dibujar en la arena los puntos y rayas del código Morse, que conocía de sus tiempos de boy scout. En un momento estiró los puntos y las rayas hacia abajo con los dedos, y quedaron líneas finas y líneas gruesas. Ahí tuvo la idea: un código Morse estirado, hecho de barras.

Pasaron más de veinte años hasta que la tecnología para leerlo estuvo lista y fue barata. El primer producto escaneado en la caja de un supermercado fue un paquete de chicles, en Ohio, en el año mil novecientos setenta y cuatro.

El código de barras fue una revolución para el comercio. Pero tiene un límite grande. Guarda muy poca información. En general, apenas un número de unos doce o trece dígitos, que sirve como una especie de documento de identidad del producto. El código no te dice qué es el producto ni cuánto cuesta. Solo te da un número, y la computadora de la caja busca ese número en su base de datos.

Además, el código de barras se lee en una sola dirección. La información está en el ancho de las barras, de izquierda a derecha. Es un código de una dimensión. Si querés guardar más datos, tenés que hacerlo más largo. Y un código de barras demasiado largo se vuelve incómodo de imprimir y difícil de leer.

## El problema de la fábrica

Ahora viajemos a Japón, a comienzos de los años noventa. Ahí hay una empresa llamada Denso, que fabrica componentes para autos y forma parte del grupo Toyota. Dentro de esa empresa había una división dedicada a lectores y sistemas de identificación, que con los años pasó a llamarse Denso Wave.

En las fábricas de autos de esa época se usaban muchísimos códigos de barras para seguir el recorrido de cada pieza. Cada caja, cada componente, cada etapa del armado. El problema era que un solo código de barras no alcanzaba para guardar todos los datos que necesitaban. Entonces pegaban varios códigos en la misma caja, uno al lado del otro. Los operarios tenían que escanear diez códigos distintos para registrar una sola cosa. Era lento, era tedioso y se cometían errores.

Los trabajadores le pidieron a la empresa algo mejor. Un código que guardara más información y que se pudiera leer rápido.

El encargado de resolverlo fue un ingeniero llamado Masahiro Hara. Junto con un equipo muy chico, se puso a pensar en un código de dos dimensiones. Es decir, un código que no guardara información solo de izquierda a derecha, como las barras, sino también de arriba hacia abajo. Una grilla. Un cuadrado lleno de casilleros, donde cada casillero puede ser blanco o negro.

Con una grilla así, en el mismo espacio entra muchísima más información. Pero aparece un problema nuevo, y es el problema más difícil de todos.

## Encontrar el código en medio del caos

Pensá en lo que ve una cámara cuando apunta a una caja en una fábrica. Ve la caja, ve el cartón, ve letras impresas, ve dibujos, ve sombras. Y en algún lugar de todo eso hay un código. La máquina tiene que darse cuenta de dónde está ese código, dónde empieza, dónde termina, y para qué lado está girado. Y tiene que hacerlo rápido.

Hara cuenta que la idea para resolver esto se le ocurrió jugando al Go, el antiguo juego de mesa de origen chino, muy popular en Japón. En el Go se colocan piedras blancas y negras sobre una cuadrícula. Mirando el tablero, pensó que una grilla de puntos blancos y negros podía guardar información de forma muy compacta. Esa fue la inspiración para el aspecto general del código.

Pero faltaba lo más importante: una marca que la cámara pudiera reconocer siempre, sin confundirse con nada.

Para eso, el equipo hizo algo muy ingenioso. Se pusieron a estudiar montones de material impreso. Diarios, revistas, folletos, cajas, etiquetas. Buscaban una figura, una proporción entre partes blancas y negras, que fuera lo más rara posible en el mundo impreso. Algo que casi nunca apareciera por casualidad.

Y la encontraron.

## Los tres ojos del código

Si mirás cualquier código QR, vas a ver que tiene tres cuadrados grandes en tres de sus esquinas. Arriba a la izquierda, arriba a la derecha y abajo a la izquierda. Cada uno de esos cuadrados es en realidad un cuadrado negro, adentro un anillo blanco, y adentro de ese anillo, un cuadrado negro más chico. Como una diana cuadrada.

Esos son los marcadores de posición. Y son la clave de todo.

Lo que tienen de especial es su proporción. Imaginate que trazás una línea recta que cruce uno de esos cuadrados por el medio, de un lado al otro. Lo que esa línea va a atravesar es: una franja negra, una franja blanca, una franja negra que es tres veces más ancha, otra franja blanca y otra franja negra. Uno, uno, tres, uno, uno.

Esa secuencia, uno, uno, tres, uno, uno, es la proporción que el equipo de Hara identificó como muy poco frecuente en los impresos comunes. Y tiene una ventaja enorme: la línea puede cruzar el cuadrado en horizontal, en vertical o en diagonal, y la proporción se mantiene. No importa cómo esté girado el código. La cámara barre la imagen buscando ese patrón, y cuando lo encuentra, sabe que ahí hay un ojo del código.

Y como hay tres ojos, y no cuatro, la cámara también sabe para qué lado está girado. La esquina que no tiene ojo es la de abajo a la derecha. Con eso alcanza para orientar todo el código, aunque lo estés mirando patas para arriba.

Gracias a este truco, el código se podía leer muchísimo más rápido que los sistemas anteriores. De hecho, el nombre viene de ahí. QR es la sigla en inglés de "respuesta rápida". Quick Response.

El código fue presentado en el año mil novecientos noventa y cuatro.

## Una decisión que cambió todo

Acá viene uno de los momentos más importantes de la historia del código QR, y no tiene nada que ver con la tecnología.

Denso Wave patentó el código. Pero decidió no cobrar por su uso. Cualquiera podía crear códigos QR, imprimirlos, leerlos y fabricar lectores, sin pagar nada. La empresa conservó la marca registrada, el nombre, pero dejó la tecnología libre para que todo el mundo la usara.

¿Por qué hicieron eso? La idea era que el código se difundiera lo más posible. Cuanta más gente lo usara, más se iban a vender los lectores y los sistemas que la propia empresa fabricaba. Y además, un estándar abierto genera confianza. Si una empresa tiene que pagarle a otra cada vez que usa un código, lo piensa dos veces. Si es gratis, lo adopta sin dudar.

Con los años, el código QR se convirtió en un estándar internacional. Eso significa que hay un documento oficial que describe exactamente cómo tiene que ser, de modo que cualquier lector del mundo pueda leer cualquier código del mundo.

Si Denso Wave hubiera cobrado por cada uso, probablemente hoy estaríamos usando otro sistema. Hubo otros códigos de dos dimensiones en esa época, algunos técnicamente muy buenos. Pero el QR combinó buena tecnología con una puerta abierta. Y eso fue lo que lo hizo ganar.

## La anatomía del cuadradito

Ya vimos los tres ojos. Pero un código QR tiene más partes, cada una con su trabajo. Vamos a recorrerlas.

Primero, la unidad mínima. Cada casillerito blanco o negro del código se llama módulo. Es como el píxel del código. Un módulo negro y un módulo blanco son, en el fondo, un uno y un cero. Información binaria, como la de cualquier computadora.

Segundo, el margen. Alrededor de todo código QR tiene que haber un borde vacío, de color claro, de al menos cuatro módulos de ancho. Se llama zona de silencio. Parece un detalle, pero es fundamental. Sin ese margen, el lector no sabe dónde termina el código y dónde empieza el resto del mundo. Muchos códigos que fallan, fallan porque alguien los pegó demasiado cerca de un dibujo o del borde de una hoja.

Tercero, unas líneas punteadas. Entre los ojos del código hay dos hileras de módulos que alternan negro, blanco, negro, blanco, como una cinta métrica. Una va en horizontal y la otra en vertical. Se llaman patrones de sincronización. Le sirven al lector para medir el tamaño de cada módulo y saber cuántas filas y columnas tiene el código. Es la regla con la que se mide todo lo demás.

Cuarto, en los códigos más grandes aparecen unos cuadraditos chicos, como ojos en miniatura, repartidos por el interior. Se llaman patrones de alineación. Sirven para corregir las deformaciones. Si el código está impreso sobre una superficie curva, como una botella, o si lo estás mirando en ángulo, la grilla se ve torcida. Esos cuadraditos le permiten al lector enderezar la imagen, como quien estira un mantel arrugado.

Quinto, cerca de los ojos hay una franja de información de formato. Es como la etiqueta del código, que le dice al lector cómo está armado el resto. Qué nivel de protección contra errores tiene y qué máscara se usó. Ya vamos a llegar a qué es eso de la máscara. Esta información es tan importante que está guardada dos veces, en dos lugares distintos, por si una de las copias se daña.

Y todo lo que sobra, todo el resto del cuadrado, es el lugar donde van los datos de verdad.

## El superpoder: funcionar aunque esté roto

Llegamos a la parte que a mí me parece más fascinante. Un código QR puede leerse aunque esté sucio, rayado, despintado o le falte un pedazo. Hasta cierto punto, claro. Pero ese punto es sorprendentemente alto.

Esto se logra con algo que se llama corrección de errores. Y la idea de fondo es fácil de entender con un ejemplo.

Imaginate que le querés dictar un número de teléfono a alguien por una radio con mucha interferencia. Si lo decís una sola vez, capaz que se pierde un dígito. Una solución sería repetirlo tres veces. Si en una de las tres se pierde algo, las otras dos lo cubren. Funciona, pero es muy poco eficiente. Estás usando el triple de espacio.

La corrección de errores del código QR hace algo mucho más astuto. No repite los datos. Agrega información extra, calculada matemáticamente a partir de los datos originales. Esa información extra funciona como una especie de huella. Si después una parte de los datos se pierde o se daña, el lector puede usar esa huella para reconstruir lo que faltaba. No adivinando, sino haciendo cuentas.

El método que usa se llama Reed Solomon, por los apellidos de los dos matemáticos que lo crearon, en los años sesenta. Y es el mismo tipo de método que se usó en los discos compactos, para que un CD rayado siguiera sonando bien, y en comunicaciones espaciales, para que los datos de sondas lejanas llegaran a la Tierra completos a pesar del ruido del camino. El mismo principio matemático que protege una foto mandada desde el espacio protege el menú de tu bar favorito.

El código QR tiene cuatro niveles de protección. En el nivel más bajo, puede recuperarse si se daña alrededor del siete por ciento del código. En el siguiente, alrededor del quince por ciento. Después, alrededor del veinticinco. Y en el nivel más alto, puede reconstruirse aunque se dañe alrededor del treinta por ciento.

Pensalo. Casi un tercio del código puede estar arruinado, y igual se lee.

Claro que hay un precio. Cuanta más protección, más espacio ocupa esa información extra, y menos lugar queda para los datos. Entonces hay que elegir. En una fábrica, donde los códigos se ensucian con grasa y se golpean, conviene un nivel alto. En una pantalla limpia, alcanza con uno bajo.

Hay un detalle importante. La protección cubre los datos, pero no los ojos. Si tapás uno de los tres cuadrados de las esquinas, el lector tiene muchos más problemas para encontrar y orientar el código. Los ojos son los que permiten empezar a leer. Sin ellos, todo lo demás se complica.

## La máscara: evitar que el código se confunda a sí mismo

Antes prometí explicar qué es la máscara. Es un detalle técnico, pero es muy elegante.

Cuando uno convierte los datos en módulos blancos y negros, a veces quedan dibujos problemáticos. Por ejemplo, una zona enorme toda negra, o toda blanca. Eso le complica la vida al lector, porque pierde la referencia de dónde termina un módulo y empieza el otro. O peor, a veces por casualidad aparece en el medio de los datos algo parecido a la secuencia uno, uno, tres, uno, uno. Y el lector podría confundirlo con uno de los ojos.

Para evitar esto, el código aplica una máscara. Es un patrón fijo, como una plantilla, que invierte algunos módulos. Donde había negro pone blanco, y donde había blanco pone negro, siguiendo una regla matemática.

Hay ocho máscaras posibles. El programa que genera el código prueba las ocho, evalúa cuál deja el dibujo más equilibrado, más parejo, con menos zonas problemáticas, y elige esa. Después anota en la franja de información de formato cuál máscara usó. Así el lector, cuando lee el código, sabe qué plantilla tiene que aplicar para deshacer el cambio y recuperar los datos originales.

Es como si el código se pusiera un disfraz para que lo vean mejor, y dejara anotado cómo sacárselo.

## Un código que no despegaba

Algo que sorprende es que el código QR existió durante muchos años sin que la mayoría de la gente le prestara atención.

En Japón se popularizó bastante temprano, a comienzos de los dos mil, cuando aparecieron los primeros celulares con cámara y con programas para leer códigos. Allá se usaba en publicidad, en revistas, en carteles.

En el resto del mundo la cosa tardó mucho más. Durante años, para leer un código QR había que bajarse una aplicación especial. Y eso era una barrera. Mucha gente veía el cuadradito en un cartel, no tenía la aplicación, y seguía de largo. Por un tiempo el QR tuvo fama de cosa rara, de recurso de marketing que nadie usaba.

Dos cosas cambiaron la historia.

La primera fue que los teléfonos empezaron a leer códigos QR directamente desde la cámara, sin aplicaciones extra. El sistema del iPhone lo incorporó en el año dos mil diecisiete, y en los teléfonos Android también se fue volviendo algo de fábrica. De golpe, cualquier persona con un celular podía leer un código con solo apuntar.

La segunda fue algo que nadie esperaba: la pandemia. En el año dos mil veinte, de un día para el otro, todo el mundo quería evitar tocar cosas. Las cartas de los restaurantes, los formularios en papel, el dinero en efectivo. Y el código QR apareció como la solución perfecta. Lo pegabas en la mesa, la gente lo escaneaba con su propio teléfono, y listo. Sin contacto.

En pocos meses, el cuadradito que llevaba más de veinticinco años esperando su momento pasó a estar en todas partes.

## El lado oscuro del cuadradito

Toda tecnología popular atrae a quienes quieren aprovecharse, y el QR no es la excepción.

El problema de fondo es simple. Un código QR es ilegible para los humanos. Vos no podés mirar un código y saber a dónde te va a llevar. Tenés que confiar.

Y hay gente que se aprovecha de esa confianza. Una de las estafas más conocidas consiste en pegar un código falso encima de uno verdadero. Por ejemplo, en un parquímetro, en un cartel o en un local. La persona escanea creyendo que va a la página oficial, pero termina en una página trucha que imita a la real y le pide datos o un pago. Este tipo de engaño tiene hasta un nombre propio en inglés, una mezcla entre las palabras QR y la palabra que se usa para las estafas por correo electrónico.

Algunas costumbres simples ayudan a cuidarse. Antes de abrir un enlace, la mayoría de los teléfonos te muestran la dirección. Vale la pena mirarla y fijarse si tiene sentido. Desconfiar de los códigos que parecen pegados encima de otros, o que están en lugares raros. Y tener cuidado especial cuando un código te pide datos personales o te lleva a pagar algo.

El código en sí no es peligroso. Es solo un dibujo que guarda texto. El riesgo está en a dónde te lleva ese texto.

## Lo que nos deja el cuadradito

Masahiro Hara ha contado en entrevistas que nunca imaginó que su código iba a terminar en las manos de miles de millones de personas. Él estaba resolviendo un problema concreto de una fábrica. Quería que los operarios no tuvieran que escanear diez etiquetas por caja.

Y sin embargo, en esa solución había ideas muy poderosas. Buscar una forma que casi nunca aparece por casualidad, para que la máquina la encuentre siempre. Usar matemáticas para que un código dañado se pueda reparar solo. Disfrazar los datos para que se vean mejor. Y, quizás la más importante de todas, dejar la tecnología abierta para que cualquiera la pudiera usar.

La próxima vez que levantes el celular frente a uno de esos cuadraditos, acordate de que estás mirando tres ojos que te dicen dónde está todo, una regla punteada que mide cada casillero, una máscara que se pone y se saca, y un escudo matemático que aguanta que le falte casi un tercio. Y acordate de que todo empezó con un ingeniero mirando un tablero de Go, pensando en cómo ahorrarle trabajo a la gente de una fábrica.

A veces las cosas que cambian el mundo no nacen queriendo cambiarlo. Nacen queriendo arreglar algo chiquito, y lo arreglan tan bien que el resto del mundo termina adoptándolo.

Esto fue Veinte Minutos. Gracias por escuchar, buen viaje, y nos encontramos mañana con un tema nuevo.
