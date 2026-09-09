# The script of the game goes in this file.

# Initiates the typing effect of each word
define config.default_textshader = "typewriter"

# Gave the MC's thoughts its own animated dialogue box 
image animated_thoughtDialogueBox:

    "gui/thought_box1.png"
    pause 0.2
    "gui/thought_box2.png"
    pause 0.2
    "gui/thought_box3.png"
    pause 0.2
    "gui/thought_box4.png"
    pause 0.2
    "gui/thought_box5.png"
    repeat


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character("???", window_background="animated_thoughtDialogueBox")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg darkness

    t "Heavy."

    t "Unbearably heavy."

    t "An indescribable weight that presses your entire body into paralysis."

    t "It burns like fire,"
    
    t "yet it stings like ice too."

    t "You don't understand it. You never had. Nobody ever had. Nobody ever will."

    t "..."

    t "Crushing tension remains ensnared around the heart."

    t "Your heart."

    t "You can feel it beating weakly."

    t "Woefully."

    t "A pitiful cry to show that yes, it's still trying."

    t "You're still trying."

    t "And thats all anyone can expect from you."

    t "..."

    t "{shader=jitter:u__jitter=3.0, 3.0}It's agonizing.{/shader}"
    
    t "Not because of the sensations themselves, but the familiarity that comes with it."

    t "You know this routine well."

    t "It's become normalized at this point."

    t "Tomorrow, the day after that, the month after that, the decade after that, you know how it goes."

    t "This will all repeat."

    t "..."

    t "For as long as you live."

    t "{shader=jitter:u__jitter=8.0, 6.0}And there's nothing you can do to stop it.{/shader}"

    t "Wake up already."

    t "You don't have the time to rot anymore."

    scene bg bedroom 

    $ renpy.movie_cutscene("videos/riseandshine.webm")

    t "Rise and shine."

    # This ends the game.

    return
