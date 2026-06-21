# Obras Completas de Rubén Sada — sitio de búsqueda

Sitio estático (sin servidor, sin costo) con buscador instantáneo
sobre toda tu obra. Vive enteramente en el navegador: no necesita
base de datos ni backend.

## Archivos

- `index.html` — la página completa (diseño + buscador, todo en un solo archivo)
- `poems.json` — los 635 poemas en formato de datos (lo lee `index.html`)
- `OBRAS_COMPLETAS_LIMPIO.txt` — tu archivo fuente, sin los renglones
  vacíos de más, codificado en UTF-8
- `generar_poems_json.py` — script para regenerar `poems.json` cada vez
  que agregues poemas nuevos al .txt

## Cómo publicarlo en GitHub Pages (gratis)

1. Creá un repositorio nuevo en GitHub (puede ser público o privado;
   si es privado, GitHub Pages requiere plan pago — para que sea
   gratis, hacelo público).
2. Subí estos 4 archivos a la raíz del repositorio (podés arrastrarlos
   desde la web de GitHub, o por línea de comandos con `git add` /
   `git commit` / `git push`).
3. En el repositorio, andá a **Settings → Pages**.
4. En "Source", elegí la rama `main` y la carpeta `/ (root)`. Guardá.
5. GitHub te va a dar una URL como
   `https://tu-usuario.github.io/nombre-del-repo/` — en uno o dos
   minutos el sitio va a estar online ahí.

No hace falta build, ni Node, ni nada más: son archivos estáticos.

## Cómo agregar la fecha en que escribiste cada poema (opcional)

Si querés, podés agregar debajo de los versos de cualquier poema una
línea con esta forma exacta:

```
@FECHA: 1971
```

(o con la fecha completa, `@FECHA: 15/03/1998`, o como la sepas,
`@FECHA: Marzo de 2005`). Tiene que empezar siempre con `@FECHA:`
— eso es lo único que el script necesita reconocer igual cada vez.
Va en su propio renglón, después del último verso del poema:

```
§ TERMINAN LAS CLASES

Terminan las clases
comienzan las vacaciones
...
chau amiguito,
que pases de grado,
te felicito.
@FECHA: 1971


§ SIGUIENTE POEMA
...
```

No es obligatorio: los poemas sin esa línea simplemente no muestran
fecha en el sitio, no rompe nada. Cuando corras
`generar_poems_json.py`, la fecha se separa automáticamente del texto
del poema y se muestra junto al número de poema, tanto en los
resultados de búsqueda como al abrir el poema completo.

## Cómo agregar los ~2000 poemas que faltan

1. Sumá los poemas nuevos a `OBRAS_COMPLETAS_LIMPIO.txt`, respetando
   el mismo formato: cada poema empieza con una línea `§ TÍTULO`.
2. Corré `python3 generar_poems_json.py` en esa misma carpeta. Esto
   regenera `poems.json` con todos los poemas (viejos + nuevos).
3. Subí los dos archivos actualizados (`OBRAS_COMPLETAS_LIMPIO.txt` y
   `poems.json`) al repositorio (`git add`, `git commit`, `git push`,
   o arrastrándolos de nuevo en la web de GitHub).
4. GitHub Pages se actualiza solo, no hay que tocar nada más.

## Sobre el tamaño

635 poemas pesan ~820 KB en `poems.json`. Con los ~2000 que faltan
(2.635 poemas en total) va a pesar entre 3 y 4 MB — sigue siendo un
archivo liviano para un sitio web: carga en menos de un segundo y la
búsqueda en el navegador sigue siendo instantánea. No hace falta
ningún motor de búsqueda externo (como Algolia) a este volumen.

## Cómo funciona la búsqueda

Es una búsqueda de texto simple, todo en el navegador (no envía nada
a ningún servidor): a medida que escribís, filtra los poemas cuyo
texto o título contiene la frase, ignorando mayúsculas/minúsculas y
acentos (por ejemplo "papa" encuentra "papá"). Al hacer clic en un
resultado, se abre el poema completo con la frase resaltada.

## Si querés probarlo en tu computadora antes de subirlo

Abrir `index.html` haciendo doble clic puede no funcionar (el
navegador bloquea la carga de `poems.json` por seguridad al abrir un
archivo local directamente). Para probarlo localmente, abrí una
terminal en esta carpeta y corré:

```
python3 -m http.server 8000
```

y entrá a `http://localhost:8000` en el navegador.
