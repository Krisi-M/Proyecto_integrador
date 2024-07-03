# Este código sirve para instalar Streamlit en tu computadora y hacer un primer programa en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# pip install Streamlit

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu computadora, no en Jupyter Notebook.
# streamlit hello

# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
#  streamlit run your_script.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# Creamos una barra lateral
sidebar = st.sidebar

# Si usas el siguiente código mostrará un título en la aplicación Streamlit. 
# st.title("Nombre de tu blog"): Esta línea está creando un título en la aplicación web.
# Pero, a diferencia de st.markdown, el texto estará alineado a la izquierda y no podrás cambiar el color del texto.

# La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
st.markdown("<h1 style='text-align: center;'>𖦹 Un acercamiento a las tendencias en asesinos seriales 𖦹</h1>", unsafe_allow_html=True)

# <h1 style='text-align: center;'>Nombre de tu blog</h1>: Esto es una cadena de código HTML. 
# La etiqueta <h1> se utiliza para el encabezado principal de una página web, y 
# el atributo style se utiliza para agregar estilos CSS. 
# En este caso, el texto está alineado al centro (text-align: center;). 
# El texto dentro de las etiquetas <h1> ("Aquí escribe un nombre creativo para tu blog") es el contenido del encabezado.

# unsafe_allow_html=True: Este es un argumento opcional en la función markdown. 
# Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad. 
# Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.

# Creamos dos columnas separadas para la imagen y el texto
col1, col2 = st.columns(2)

# col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
# La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
# Las columnas creadas se asignan a las variables col1 y col2.

# En la primera columna colocamos la imagen
col1.image("Ted_Bundy.jpg", caption='Ted Bundy confesó ser el autor de 30 asesinatos entre 1974 y 1978, pero se cree que fueron muchos más.', width=300)

# col1.image("ellie.png", caption='Ellie', width=300): Esta línea está colocando una imagen en la primera columna (col1). 
# La función image toma como primer argumento la ruta de la imagen que se va a mostrar. 
# En este caso, la imagen es "ellie.png". 
# El argumento caption se utiliza para proporcionar un pie de foto a la imagen, en este caso 'Ellie'. 
# El argumento width se utiliza para especificar el ancho de la imagen, en este caso 300 píxeles.

# En la segunda columna colocamos el texto: Debe contener una presentación de ustedes
# Deben presentarse: ¿Quién eres?, ¿De dónde eres?, ¿Qué estudias?, ¿Qué te gusta de tu carrera?, 
# ¿Qué te gustaría hacer en el futuro?, ¿Qué te gusta hacer en tu tiempo libre?

texto = """
Durante años, los crimenes mediaticos cometidos por asesinos seriales, catalogados como crueles y sin motivo, han captado la atención del ojo publico debido a su cruel y espantosa naturaleza, en algunos casos
 mas grotescos que otros. Sin embargo, la misma mediatez de los casos no permite en muchas ocasiones, explorar
 los motivos por los que sucedieron, no con respecto a las victimas, sino con respecto al perpetrador. En la presente investigación, reuniremos
 data para poder explicar en cierto grado el trasfondo de un asesino serial, desde aspectos en la infancia hasta las motivaciones por las que cometieron sus crimenes.
 De esta forma podremos tambien comparar esta data a traves de los años, viendo los picos de aumento y disminución.
 ✄┈┈┈┈
"""

# Las comillas triples (""") en Python se utilizan para definir cadenas multilínea.
# Mostramos el texto
col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

# <div style='text-align: justify; font-size: 15px;'>{texto}</div>: Esta es una cadena de código HTML. 
# La etiqueta <div> se utiliza para agrupar contenido en HTML. 
# En este caso, el texto está justificado (text-align: justify;). 
# El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
# El texto dentro de las etiquetas <div> es la variable texto.

# f"": Esta es una cadena de formato en Python. 
# Permite la interpolación de variables, lo que significa que puedes insertar el valor de una variable directamente en la cadena. 
# En este caso, {texto} se reemplaza por el valor de la variable texto.


# Debajo de las columnas colocamos un subtítulo que describa tu experiencia aprendiendo a programar
# Deben presentar tu experiencia aprendiendo a programar: ¿Cómo te sentiste al principio?, 
# ¿Qué te ha enseñado la programación?, ¿Qué te gusta de programar?, 
# ¿Qué te gustaría hacer con la programación en el futuro? 

# Agregamos un subtítulo
st.markdown("<h2 style='text-align: center;'>𖦹 ¿Que es un asesino serial? 𖦹</h2>", unsafe_allow_html=True)

# <h2 style='text-align: center;'>𖦹 ¿Que es un asesino serial? 𖦹</h2>: Esta es una cadena de código HTML.
# La etiqueta <h2> se utiliza para el encabezado secundario de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h2> ("𖦹 ¿Que es un asesino serial? 𖦹") es el contenido del encabezado
# unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
# Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad.
# Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
# Puedes agregar emojis en el texto de Markdown utilizando códigos de emoji.

# Agregar un  texto para la respuesta
texto_2 = """
Lo primero que se debe tener en cuenta al hablar de este tipo de casos es la definición de las cosas. Comunmente se confunde el termino de asesino con asesino serial, la verdad 
es que la denominación asesino en serie o asesino serial se designa a un individuo que asesina a tres o más personas en un lapso de 30 días o más, con un período de «enfriamiento» entre cada asesinato, 
y cuya motivación usual es la gratificación psicológica que le proporciona cometer dicho crimen, aunque no necesariamente la única.
Asi mismo, los asesinos seriales son selectivos con sus victimas y son principalmente impulsados por alguna necesidad interna imperiosa. Las tendencias mas comunes de necesidad
son la de placer sexual, placer por control de poder y crimenes de odio.
La mayoría de los asesinos en serie tienen antecedentes enfermizos o trastornos mentales. 
Se sabe que, frecuentemente, fueron víctimas de abusos durante su infancia, ya sea física, sexual o psicológicamente,
 toda vez que existe una correlación entre los abusos de su infancia y los crímenes que cometen.
 Claro que, no necesariamente porque se cumplan estos requisitos en una mayoria de personas que cometieron crimenes 
 significa que cualquier persona que viva lo mismo vaya a convertirse en asesino.
 De ahi que el estudio psicologico de los mismos sea hasta la fecha tan interesante como intrigante, revela una pregunta incomoda a la sociedad, "¿un asesino nace o se hace?"
 La verdad es que hay muchisimos factores influyentes para que una persona cometa un crimen de tal magnitud, pero lo  que todos los asesinos tienen en común es la llegada de un "punto de quiebre".
 Las fantasias del asesino serial creadas por el deseo u motivación son lo que finalmente impulsa estos actos atroces, el punto de quiebre representa el paso de la ficción a la realidad, el ultimo paso antes de satisfacer aquellas necesidades. 
"""

# Mostramos el texto
st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_2}</div>", unsafe_allow_html=True)

# <div style='text-align: justify; font-size: 15px;'>{texto_2}</div>: Esta es una cadena de código HTML.
# La etiqueta <div> se utiliza para agrupar contenido en HTML.
# En este caso, el texto está justificado (text-align: justify;).
# El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
# El texto dentro de las etiquetas <div> es la variable texto_2.
# f"": Esta es una cadena de formato en Python.
# Permite la interpolación de variables, lo que significa que puedes insertar el valor de una variable directamente en la cadena.
# En este caso, {texto_2} se reemplaza por el valor de la variable texto_2.

# Agregamos un subtítulo en la barra lateral
sidebar.markdown("<h1 style='text-align: center;'>Graficos de data comparativa entre decadas</h1>", unsafe_allow_html=True)

# <h1 style='text-align: center;'>Los análisis de Ellie</h1>: Esta es una cadena de código HTML.
# La etiqueta <h1> se utiliza para el encabezado principal de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h1> ("Los análisis de Ellie") es el contenido del encabezado.

# Creamos una lista de gráficos
graficos = ['♰ Tipos de abuso sufridos en la infancia de asesinos seriales', '♰ Motivación subconsciente del asesinato', '♰ Abuso de sustancias por parte de asesinos seriales']

# Creamos un cuadro de selección en la barra lateral
grafico_seleccionado = sidebar.selectbox('♰ Selecciona un gráfico', graficos)
# El cuadro de selección se crea con la función selectbox.
# El primer argumento es el texto que se muestra en el cuadro de selección.
# El segundo argumento es una lista de opciones que se pueden seleccionar.
# En este caso, las opciones son los elementos de la lista graficos.
# La opción seleccionada se asigna a la variable grafico_seleccionado.
# La variable grafico_seleccionado se utiliza para mostrar el gráfico correspondiente en la aplicación web.
# La función selectbox se utiliza para crear un cuadro de selección en la barra lateral.

# Mostramos el gráfico seleccionado
if grafico_seleccionado == '♰ Tipos de abuso sufridos en la infancia de asesinos seriales':
    sidebar.markdown("<div style='text-align: justify; font-size: 20px;'>Este grafico muestra la comparativa entre decadas de los distintos tipos de abuso que sufrieron en la infancia muchos de los asesinos seriales que se encontraron en la data. El abuso en la niñez puede afectar gravemente las relaciones y desarrollo de una persona y eventualmente llevar a un posible desarrollo de La triada de Mcdonald</div>", unsafe_allow_html=True)
    sidebar.image("tipos_de_abuso_por_decada.png", caption='♰ Tipos de abuso sufridos en la infancia de asesinos seriales', width=500)
    pass
elif grafico_seleccionado == '♰ Motivación subconsciente del asesinato':
    sidebar.markdown("<div style='text-align: justify'>Las motivaciones se divideron y clasificaron en dos. Por placer y por enojo. La primera se refiere a un deseo del subcosciente que se divide en obtener placer sexual u obtener placer por poder mediante el acto. Mientras que los crimenes por enojo son los que a grandes rasgos conocemos como crimenes de odio </div>", unsafe_allow_html=True)
    sidebar.image("tipos_de_asesinatos_por_decada.png", caption='♰ Motivación subconsciente del asesinato', width=500)
    pass
elif grafico_seleccionado == '♰ Abuso de sustancias por parte de asesinos seriales':
    sidebar.markdown("<div style='text-align: justify'>Finalmente, el abuso de sustancias resulta muchas veces crucial para que un asesino termine por  realizar el acto, pues hubo una tendencia de declaraciones que al tener el deseo de repetir la experiencia del asesinato, pero saber que esta mal, abusaban de sustancias como el alcohol o alguna droga para tener el coraje de realizarlo.</div>", unsafe_allow_html=True)
    sidebar.image("tipos_de_sustancia_por_decada.png", caption='♰ Abuso de sustancias por parte de asesinos seriales', width=500)
    pass

# if grafico_seleccionado == 'Gráfico de Macroareas':: Esta línea verifica si la opción seleccionada es 'Gráfico de Macroareas'.
# Si es así, se ejecuta el código dentro del bloque if.
# En este caso, se muestra un texto y una imagen correspondientes al gráfico de Macroareas.
# El texto y la imagen se muestran en la barra lateral.
# La función markdown se utiliza para mostrar el texto en la barra lateral.
# La función image se utiliza para mostrar la imagen en la barra lateral.
# El argumento caption se utiliza para proporcionar un pie de foto a la imagen.
# El argumento width se utiliza para especificar el ancho de la imagen.
# La palabra clave pass se utiliza para indicar que no se debe hacer nada en caso de que la opción seleccionada no sea 'Gráfico de Macroareas'.
