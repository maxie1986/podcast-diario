# Guía para escribir episodios

La sigue la tarea programada que escribe un episodio por día.

## Formato

Archivo nuevo en `episodes/AAAA-MM-DD-slug.md` (fecha del día, slug corto en minúsculas con guiones):

```
---
title: "Título atractivo, menos de 60 caracteres"
description: "Una o dos oraciones que resuman el episodio."
topic: categoría / subcategoría
date: AAAA-MM-DD
---

Texto del episodio...
```

Un push a `main` con un archivo nuevo dispara la Action que genera el MP3 y actualiza el feed. No hace falta nada más.

## Elección del tema

- Categorías en rotación: tecnología, naturaleza, salud, finanzas, actualidad, deportes, historia, ciencia, espacio, curiosidades.
- Mirar los `topic` de los últimos episodios en `episodes/` y no repetir categoría hasta completar la vuelta.
- No repetir un tema ya tratado.
- Preferir temas atemporales, que no requieren búsquedas. Actualidad, finanzas o deportes como máximo dos veces por semana, y solo esos llevan búsqueda web (pocas búsquedas, solo para verificar datos recientes).

## Estilo

- Entre 3.100 y 3.300 palabras (la voz lee unas 160 por minuto, así que da unos 20 minutos).
- Castellano rioplatense, con voseo natural, tono de divulgación cercano. Pensado para escucharse manejando.
- Escrito para el oído: oraciones cortas o medianas, sin tablas, listas, paréntesis ni símbolos (escribir "microsegundos", no "µs"; "por ciento", no "%").
- Números redondeados y fáciles de seguir. Pocas cifras por párrafo.
- Encabezados `##` para separar secciones: se leen como pausa, así que tienen que funcionar como frase.
- Arranque: "Hola, bienvenido a Veinte Minutos." más el gancho del tema. Cierre: "Esto fue Veinte Minutos. Gracias por escuchar, buen viaje, y nos encontramos mañana con un tema nuevo."
- Solo datos de los que haya seguridad. Ante la duda, omitir el dato.
- Salud y finanzas: información general, sin recomendaciones personales.
