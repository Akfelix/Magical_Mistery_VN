# Coloca el código de tu juego en este archivo.

 # Declara los personajes usados en el juego como en el ejemplo:

define v= Character("Valentine")
define c= Character("Cloe")

define sadTheme ="audio/music/magical_travel.ogg"

init:
    image bg Cafeteria = "images/background/Cafeteria.png"

    image val enfadada= Image("images/Characters/Women 1_Angry.png")
    image val emocionada= Image("images/Characters/Women 1_Excited.png")
    image val ligando= Image("images/Characters/Women 1_Flirting.png")
    image val sosa= Image("images/Characters/Women 1_Idle.png")
    image val triste = Image("images/Characters/Women 1_Sad.jpg")
    image val asustada = Image("images/Characters/Women 1_Asustada.jpg")
    image val en shock = Image("images/Characters/Women 1_Shocked.jpg")
    image val feliz = Image("images/Characters/Women 1_Smile.png")
    image val hablando = Image ("images/Characters/Women 1_Talking.png")
    image val pensando = Image ("images/Characters/Women 1_Thinking.png")

    image cloe enfadada= Image("images/Characters/Women 2_Angry.png")
    image cloe emocionada= Image("images/Characters/Women 2_Excited.png")
    image cloe ligando= Image("images/Characters/Women 2_Flirting.png")
    image cloe sosa= Image("images/Characters/Women 2_Idle.png")
    image cloe triste = Image("images/Characters/Women 2_Sad.jpg")
    image cloe asustada = Image("images/Characters/Women 2_Asustada.jpg")
    image cloe en shock = Image("images/Characters/Women 2_Shocked.jpg")
    image cloe feliz = Image("images/Characters/Women 2_Smile.png")
    image cloe hablando = Image ("images/Characters/Women 2_Talking.png")
    image cloe pensando = Image ("images/Characters/Women 2_Thinking.png")

    image cloe enfadada= Image("images/Characters/Women 2_Angry.png")
    image cloe emocionada= Image("images/Characters/Women 2_Excited.png")
    image cloe ligando= Image("images/Characters/Women 2_Flirting.png")
    image cloe sosa= Image("images/Characters/Women 2_Idle.png")
    image cloe triste = Image("images/Characters/Women 2_Sad.jpg")
    image cloe asustada = Image("images/Characters/Women 2_Asustada.jpg")
    image cloe en shock = Image("images/Characters/Women 2_Shocked.jpg")
    image cloe feliz = Image("images/Characters/Women 2_Smile.png")
    image cloe hablando = Image ("images/Characters/Women 2_Talking.png")
    image cloe pensando = Image ("images/Characters/Women 2_Thinking.png")


# El juego comienza aquí.
show screen onscreenmenubutton
label start:


   
    ##call prueba_afinidad

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    play music sadTheme fadein 2.5
    "Si me hubieran dicho en la academia que mi primer misterio sería resolviendo tu muerte."
    "Seguramente me habría echado a reír y habría dicho, que aquí nadie podría matar a una mosca."
    "Todas cuidamos de todas"
    "Habría sido una mentira fácil de creer, quien diría que en una academia de chicas mágicas se produjera tal afrenta"
    "Pero de nuevo aquí estoy: viendo tu cuerpo frío delante de mi sin vida"
    "Crueles fueron las manos que tallaron tu destino, y ahora me toca descifrar quién fue el artista que firmo con sangre tu final"
    stop music fadeout 2.0

    scene bg Cafeteria
    show val feliz at left
    v "JAJAJAJAJAJAJA"
    show cloe enfadada at right
    c "Val, no hace gracia"
    show val hablando at left
    v "Un poquito de gracia sí que hace, es una gran oportunidad, deberías estar dando saltos de alegría, no replanteandote si etá bien o está mal"
    show cloe triste at right
    c "No, sé todo el mundo aquí, tiene poderes que son la leche y yo estoy aquí"
    show val pensando at left
    v "A ver no voy a negarte que tus poderes son..."
    show cloe sosa at right
    c "inútiles, mediocres, bizarros, extravagantes..."
    show val hablando at left
    v "peculiares"
    show cloe sosa at right
    c "Sí porque ... es super útil, vamos lo mejor que me ha pasado en la vida."
    show val sosa at left        
    v "Noto algo de sarcasmo, en tus palabras."
    show cloe pensando at right
    c "Sólo digo que seria todo más fácil, si fuera cómo tú."
    show val hablando at left
    v "Creeme no quieres ser cómo yo."
    show cloe feliz at right 
    c "lo que me extraña es que TU no quieras ser tu."
    show val pensando at left
    v "Desde que adquirí los poderes, todo es más complicado..."
    show cloe pensando at right
    c "Lo siento Val, no sabía que te sentías así."
    

        
   
    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    #show eileen happy

    # Presenta las líneas del diálogo.


    # Finaliza el juego:

label prueba_afinidad:

    "Te encuentras con P1. Parece que necesita ayuda."

    menu:
        "Ayudar a P1":
            $ modificar_afinidad("P1", 10)
            "Has ayudado a P1. Su afinidad ha aumentado."

        "Ignorar a P1":
            $ modificar_afinidad("P1", -5)
            "Has ignorado a P1. Su afinidad ha disminuido."

    "La decisión ha terminado."

    $ afinidad_actual = personajes_datos["P1"]["afinidad"]

    "La afinidad actual de P1 es [afinidad_actual] puntos."

    return


    return