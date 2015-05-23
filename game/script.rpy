# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.

# Declare images below this line, using the image statement.
# - Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.
# eg. image eileen happy = "eileen_happy.png"
image num3="num1.jpg"
image num2="num2.jpg"
image num4="num3.jpg"
image feliz="feliz.jpg"
# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el 
#   ejemplo.
define e = Character('tina', color="#FF0033")
define i= Character('Emy', color="#FFFFFF")
define a= Character('Elena', color="#c8ffc8")
define b= Character('Tom', color="#c8ffc8")


# The game starts here.
# - El juego comienza aquí.
label start:
    
    
    
    play music "Kangaroo Court.mp3"
    
    scene num3
    scene feliz
    


    e "Hola"

   
    e "Estoy feliz de que estes leyendo esto, espero te guste :)"
   
    stop music
    play music "number1.mp3"
    
    scene num1
   
    i " "
    
    a ""
    
    b ""

    return
