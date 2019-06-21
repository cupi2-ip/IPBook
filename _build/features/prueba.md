---
title: 'Prueba Markdown'
prev_page:
  url: /features/notebooks
  title: 'Jupyter notebooks'
next_page:
  url: 
  title: ''
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Sintaxis de Markdown
> ¿Cómo le pongo  un título a la página?

Esta es una pequeña guía de **Markdown** para *probar* las capacidades del lenguaje (y la compatibilidad de la herramienta [Jupyter Books](https://jupyter.org/jupyter-book/intro.html)).


## Títulos de sección (#)
Los títulos de sección se demarcan en **Markdown** usando el caracter '#' al inicio de una línea. De esta manera, el título de mayor nivel estará en una línea que inicie con un caracter '#'. El título de las secciones del segundo nivel se describirán en líneas que inicien con '##' y así sucesivamente.

Por ejemplo, el título de esta sección está declarado de la siguiente manera:

```
## Títulos de sección (#)
```

Se puede llegar hasta el nivel **7**.

## Formato de texto
Se pueden formatear un texto para que aparezca en negrita o en itálicas.

* Para **negrita**, debe rodearse el texto con '**'
* Para *itálicas*, debe rodearse el texto con '*'
* Para _subrayado_ se puede usar *underscores*, pero no necesariamente funcione. Si no está activada la opción, se va a ver en italicas.

*Nota:* Los saltos de línea simples no se verán como un salto de línea en el archivo renderizado. Para iniciar un nuevo párrafo es necesario poner dos saltos de línea seguidos.

### Código entre líneas

Para poner código dentro de una línea se rodea un texto con el caracter ``(acentro grave)` . Por ejemplo, `print('Hello, World!)`.

### Código en bloque (genérico)
Un bloque de código se puede demarcar indentando al menos 4 espacios.

    def funcion(saludo: str)-> None:
        print('Hello, {}'.format(saludo))

El código también puede demarcarse usando tres acentos graves para abrir y para cerrar el bloque.

```
def funcion(saludo: str)-> None:
    print('Hello, {}'.format(saludo))
```

### Código en bloque (específico)

Si después de los tres acentos se especifica el nombre del lenguaje es posible que se vea el código con un formato aplicado. Sin embargo, esto depende de la herramienta y hay que probarlo.

```python
def funcion(saludo: str)-> None:
    print('Hello, {}'.format(saludo))
```


### Citas
Para introducir citas, se puede iniciar una línea usando el caracter `>`. Las citas se pueden anidar.

>>We know what we are, but know not what we may be

> William Shakespeare

### Matemáticas y fórmulas

#### Tex-Like

\\[
    A^T_S = B
\\]

#### MathML
<math display="block">
    <msubsup><mi>A</mi> <mi>S</mi> <mi>T</mi></msubsup>
    <mo>=</mo>
    <mi>B</mi>
</math>



### Otros formatos
Estos formatos es posible que no sean soportados por GitHub o por Jupyter Books. Se incluyen para probar:

Option name         | Markup           | Result if enabled     |
--------------------|------------------|-----------------------|
Intra-word emphasis | So A\*maz\*ing   | So A<em>maz</em>ing   |
Strikethrough       | \~~Much wow\~~   | <del>Much wow</del>   |
Underline [^under]  | \_So doge\_      | <u>So doge</u>        |
Quote [^quote]      | \"Such editor\"  | <q>Such editor</q>    |
Highlight           | \==So good\==    | <mark>So good</mark>  |
Superscript         | hoge\^(fuga)     | hoge<sup>fuga</sup>   |
Autolink            | http://t.co      | <http://t.co>         |
Footnotes           | [\^4] and [\^4]: | [^4] and footnote 4   |

[^4]: You don't have to use a number. Arbitrary things like `[^footy note4]` and `[^footy note4]:` will also work. But they will *render* as numbered footnotes. Also, no need to keep your footnotes in order, I will sort out the order for you so they appear in the same order they were referenced in the text body. You can even keep some footnotes near where you referenced them, and collect others at the bottom of the file in the traditional place for footnotes.



## Separadores

Se puede usar `***` o `---` para introducir un separador horizontal.

***


## Listas
Las listas pueden tener *bullets* o estar numeradas. Para listas con *bullets*, se deben tener líneas que inician con el caracter `*`. Para líneas numeradas, cada línea puede iniciar con un número seguido de un punto y un espacio.

### Ejemplo
1. Este es el primer item de una lista. Inicia con `1. `
2. Este es el segundo item.
  3. Esta es otra lista que está dentro de la primera. 
     Para lograrlo fue sólo necesario indentar un poco el texto.
     * Este es un item de la lista que está un nivel más adentro.
     * En este caso se está usando `*` para que la lista no esté numerada.

*Nota:* No es necesario que se usen los números correctamente (la herramienta calcula la numeración correcta) pero puede ser mucho más fácil la edición si se usa una buena numeración.


## Links e imágenes

### Links (inline)
Un link se puede incluir directamente dentro del texto rodeándolo con '<' y '>'. Por ejemplo, <http://www.google.com> debería llevar a la página de google usando el código: ` <http://www.google.com>`.

*Nota:* Es necesario poner el protocolo para que detecte el link.

### Links (estilo referencia)
Los links también pueden incluirse usando algún texto que los reemplace. Por ejemplo, este [link](https://jupyter.org/jupyter-book/intro.html) se produjo con el siguiente código:
`[link](https://jupyter.org/jupyter-book/intro.html)`

### Imagen 
Las imágenes se incluyen de forma similar. Por ejemplo, para la imagen siguiente este es el código que se utilizó:
`![Logo Jupyter Books](https://jupyter.org/jupyter-book/images/logo/logo.png)`

![Logo Jupyter Books](https://jupyter.org/jupyter-book/images/logo/logo.png)

## Tablas

Las tablas pueden tener un número variable de columnas y pueden tener encabezado. Los encabezados deben separarse del contenido usando guiones (-). Las columnas deben separarse usando pipes (|).

Titulo 1 | Titulo 2 | Titulo 3
:-------- | :--------: | -------:
Contenido a la izquierda | Contenido Centrado | Contenido a la derecha
Contenido 1 | Contenido 2 | Contenido 3
Contenido 1 | Contenido 2 | Contenido 3

