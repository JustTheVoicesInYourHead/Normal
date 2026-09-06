# All of these are variables defining the characters
# along with the names that each character's name will be shown in

# Narrator is just a "character" with no name attached (aka the narrator)

define a = Character("Asher", color='#1529d6')
define p = Character("Player", color='#9C2007')
define s = Character("Alias", color='#FF84D8', window_background=Frame("gui/aliastextbox.png", 1, 1))
define narrator = Character(window_background=Frame("gui/narratortextbox.png", 0.5, 0.5))

# These are just for the easter egg I included in the demo
# We don't have to worry about that if we're not including an easter egg that forcefully changes the characters name

# default forcedname = ""
#default fullforcedname = "worm"

#init python:
    #def next_letter():
        #global forcedname
        #global fullforcedname
        #if fullforcedname:
            #forcedname+= fullforcedname[0]
            #fullforcedname = fullforcedname[1:]

# this function makes the screen shake a little bit for dramatic effect
image shake:
    Text("{size=+35}{b}{i}[word]!{/i}{/b}")
    pos (-4, -4)
    pause .01
    pos (8, 8)
    pause .1
    pos (0, 0)
    pause .01
    repeat 3

# This is where everything starts.
# This is the prologue, where an unknown character asks for the player's name in a dream,
label start:
    define prologue = True
    $ narrator = Character(window_background=Frame("gui/prologuetextbox.png", 0.5, 0.5))
    "Thank you."

    "Thank you so much for coming."

    "In all the time we've spent keeping it satisfied, in satiating its boundless ego, no one could have predicted that it'd grow so restless."

    "No one knows what it wants. No one can piece together what it stands to gain from wiping us out one by one, all under its cutesy guise."

    "We've already lost so much, and many more suffered before giving up entirely, but we can't be surprised. Dying for a hopeless cause, one with no end in the near future, isn't exactly motivating for most."

    "They don't want to die for results in the long run, when they can barely survive short-term."

    "But someone has to do it."

    "..."

    "And today, that someone is you."

    "Flattery, riches, charisma, kindness - all prior attempts to appeal to it have come short. All previous endeavors that involved direct contact or even indirect confrontation have resulted in disaster, thus sending our progress catapulting in the opposite direction."

    "..."

    ". . ."

    "...in short, we haven't succeeded."

    "But you still came."

    "Your sacrifice won't be in vain. You'll make a difference, one way or the other. We know this for certain. This time, things will change."

    "Progress will be made."

    "We will get rid of her.{nw}{done}"

    "But if you never come back..."

    "..."

    "Tell us."

    "Tell us your name."

    "Tell us who you are, or who you should have been."
	# this brings up a text box where the player puts their name
    $ player = renpy.input("Who is our savior?: ", length=32)
    $ player = player.strip()
    $ renpy.block_rollback()
	
	# these are the chances the player has to enter an actual name
	# if they don't put an actual name (because I added a few easter eggs),
	# and the chances are increased to 3,
	# the unknown character forces their name to be "worm"
    define chances = 0 

	# this is where the name is checked and determines whether a chance is added
	# for now, it only triggers when the player enters one of these names:
	# "Ulka" (character in the game), "Asher" (character in the game)
    label namecheck:
    while (player.lower() == "ulka") or (player.lower() == "asher"):
        "Huh."
        "How...inconvenient."
        "While we appreciate your cooperation, we request that you use a different name."
	"For personal reasons."
        $ chances += 1

	# this gives the player another chance to enter their name
        $ player = renpy.input("Who is our savior?: ", length=32)
        $ player = player.strip()

	# this forces the player to change their name again, but Aki shows signs of annoyance
        if chances == 3:
            "..."    
            "You're going to be a headache, aren't you?"
            $ player = renpy.input("Who are you?: ", length=32)
            $ player = player.strip()

		# this is the player's final chance, after which the name force is commenced
		if (player.lower() == "ulka") or (player.lower() == "asher") or (player.lower() == "aki") or (player.lower() == "alias"):
                "..."
                $ player = renpy.input("Who are you?: ", length=32)
                $ renpy.block_rollback()

		# calls the Force_Typing function from the screens.rpy file, changes the player's name to "worm", then jumps back to the namecheck from before
                call screen Force_Typing
                $ player = "worm"
                jump namecheck
        jump namecheck

	# another easter egg, where Aki ends the game if the player doesn't enter a name at all
    if player == "":
        "...Very well."
        "We understand. Sharing your name with strangers must be more difficult than we give it credit for."
        "But if you want a chance to return at all, you need something for it to refer to you as."
        $ player = renpy.input("If you won't tell us your name for the sake of it, at least do so for your own survival: ")
        if player == "":
            "...fine. If you can't be bothered to give your name, at the very least, you stand no chance against it."
            "This is a fight against a force beyond comprehension. Simply uttering the title of which you're referred to as should be the simplest step of this process."
            "But you can't even do that."
            "..."
            "This was a waste of our time. You shouldn't have come if you weren't capable of doing the bare minimum."
            "We need saviors, not cannon fodder."
            "Goodbye."
            return

	# another easter egg, where Aki immediately closes the game if they player enters the name "Alias" (the main protagonist of the game)
    if player.lower() == "alias":
        "..."
        "..."
        ". . ." 
        $ renpy.quit()  

	# another easter egg, where Aki doesn't allow the player to choose his name
    while player.lower() == "aki":
        "That is not your name."
        "If it is, then it is not now."
        "I won't allow it."
        $ player = renpy.input("Choose another title, for this instance only: ", length=32)
        $ player = player.strip()
        jump namecheck
        while player.lower() == "aki":
            "No."
            $ player = renpy.input("Choose another title, for this instance only: ", length=32)
            jump namecheck
      
    # this is when the game actually continues
    "Thank you."

    "Should you fail, and we are forced to mark your gravestone,"

    "we'll know now to encarve the name-"
	# this ends the prologue (player's dream) and prevents the player from being able to check the history from everything that happened prior
    $ _history_list = []
    $ renpy.block_rollback()
    $ narrator = Character(window_background=Frame("gui/narratortextbox.png", 0.5, 0.5))

    ## First scene: Asher, Player, Ulka

    scene bg park1
    with None
	# these are variables defined to choices the player can make
    $word = (player)
    $p = (player)
    define punch = False

    a "{image=shake}"

    p "AAAAH!"

    "Asher's voice was so loud that it nearly caused you to fall off your seat, startling the two pidgeons that had sat themselves upon your shoulders while you spaced out."

    "Your startled yelp wasn't anything quiet, either. It caught the attention of a passing couple and their dog, the former of which kindly requsted that you stop shouting by viciously barking in your direction while its owners pulled on its leash to shut it up."

    "Lots of noise happened in that short span of time, and none of them were particularly pleasant to you..."

    "...or maybe they were, who am I to say?"

    p "...huh? What happened? Where am I?"
    
    "Annoyed at your lack of attention, and your ignorant facade, Asher landed a harsh punch to your forearm. His scrawny arms wouldn't have done much harm if not for the arrangement of brass rings circling each finger. You can already feel a bruise forming."

    a "What're you talking about? YOU'RE the one that agreed to come out with me and fell asleep. What's the point of comin' to the park if you're gonna hit the sack anyway?!"

    p "..."

    p "...first of all, ow. Second of all, "

	# this is how you prompt the player into making a choice
    menu:

        "I didn't know I fell asleep.":
            jump know

        "No need to be so violent.":
            jump violent

        "{i}Punch him back{/i}":
            #you monster
            $ punch = True
            jump punch    

#/// LONG INFOTURIAL SECTION

	# these are where you put the results of each choice
	# for future reference, the most common method of making choices is like this:
# menu:
	#"I am choice 1. The jump function forces the script to go to the named label after it. Don't forget the colon.":
	#jump choice1

	#I am choice 2. In the Ren'py vn community, quotation marks are left out for actions. So pretend this is a punch:
	#jump choice2

	#label choice1
		#p: "If the player chooses choice 1, the program will jump here and continue, ignoring the code between the choices"
	#label choice2
		#p: "If the player chooses choice 2, the program will jump here and continue, ignoring the choice1 label and continuing the script"

#/// end infoturial section :)

    label know:
        p "I didn't even know I was tired, let alone falling asleep."

        a "So you just felt your eyelids getting heavier and thought \"man, this is 100\% normal and not indicative of me needin' some rest?\""
        
        p "..."
        p "Well, yeah, I guess."

        a "Damn, dude. You're irregular."

        a "I don't know if I should be worried about your well-bein' or suspicious of how sketchy that sounds. So I'll take the neutral route of bein' mildly disappointed."

        p "..."

        "Somehow, that felt like the worst outcome of the two."

        jump onward

    label violent:
        p "Okay, okay! Sorry for nodding off. However, does that really warrant such violence on your end? It really hurt, FYI."

        a "Psh, no it didn't. Look at me! I'm all skin and bones! I literally couldn't have hurt you!..."

        "Asher took a moment to look himself up and down, as if unsure about his own figure. He was on the taller side when it came to height, and he was definitely thin, but not skin-and-bones thin."
        "Besides his 90's greaser-like sense of fashion and blueberry-colored hair, he was normal enough- in appearance, at least. His personality was an entirely different story."
        "Regardless of his appearance, he didn't seem to piece together that his figure wasn't the point of issue, but the spiked metal rings on the hand he punched you with."
        "He must've realized this after looking over his arms, as his cocky grin faltered once his eyes landed on the offending accessories."

        a "...I didn't hurt you, did I?"

        "In the blink of an eye, he had stopped smiling and turned to you with a small frown and guilt-ridden eyes. Think of a golden retriever that tore apart your slippers and, after you scolded it for being a bad boy, just sat on the floor and stared up at you with its beady eyes to silently beg for your forgiveness."
        "That's what Asher looked like."

        p "...No. No, you didn't hurt me that bad. I'm fine."

        "Because you weren't a heartless monster (hopefully), you reassured Asher that you were fine, to which his mile-wide grin returned, topped with those eager eyes of unearned confidence."

        a "See? Told you I couldn't hurt you!"

        "You nodded, subconsciously pushing your shoulder back so the forming bruise could hide behind your torso."

        jump onward


    label punch:  
        "Since you and Asher were such close companions, ones that have been through thick and thin, two individuals who cherished each other almost as much as you cherished yourselves, closer than any force on this planet,"
        "you decided the only appropriate retaliation was to thwack him back."
        "You know, like what a good friend would do."
        "{i}BAM!{/i}"

        "You threw your fist as hard as you could into his arm, hoping to do just as much damage to him as he did to your poor, fragile skin."

        a "..."
        "..."
        ". . ."
	# this enlarges the text and makes Asher scream like a little baby, lmao
        a "{size=+30}{b}WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH!!!!!{/b}"

        "Unfortunately, you forgot just how much of a massive pussy Asher was."

        a "W-WHY'D YOU HIT ME?! I DIDN'T DO ANYTHING WRONG TO YOU! WAAAAAAAAAH AAAAAAAAAAAAAAAAAAAAAAAA!!!"
        a "I CAN'T BELIEVE YOU'D HIT ME! I THOUGHT WE WERE FRIENDS!"
        a "IT HURTS SO MUCH! I FEEL LIKE I'M DYING!"
        a "OH LORD, SAVE ME FROM THIS WRETCHED CREATURE!"

        "At this point, almost everyone in the park was staring you down like you were the devil reincarnated. Even the group of teenagers drowning out the noise with their earbuds on the nearby swings had raised their heads to eye you. Some people were even giving you dirty looks."
        "But oh, the worst part of it all...was the god-forsaken sound of Asher's crying."
        "It wasn't as heart-breaking as it was ear-shattering, like scratching your nails on a chalkboard while sitting on a chair with a squeaky leg."
        "It was obnoxious to the point of harm, where you could've sworn you felt blood leaking out your ears like a faucet."

        p "Okay, okay, OKAY! I'M SORRY! PLEASE, FOR THE LOVE OF EVERYTHING, STOP CRYING!"

        "Your desperate pleas were enough to satisfy Asher's cruel sense of humor, at which his mouth zipped shut as he smiled down at you. The other park inhabitants were still judging you two from afar, but Asher didn't seem to notice."
        "That, or he was too amused by your desperation to care."

        a "Heh. Thought so."

        jump onward

    label onward:

    a "Anyways, what was I talking about earlier before you oh so rudely fell asleep on me? Oh, right."
    a "I called Ulka a couple minutes ago and she said she was on her way here right now. Something, something, \"a bird flew into her face while she was riding on her bike and she swerved down a hill,\" is what she said."
    a "Kinda weird, since she called me an hour ago and said a similar thing, but y'know how Ulka is!"
    a "To be honest, I'd be more concerned if she WAS on time."

    "Asher's words, despite his playful demeanor, made Ulka seem like the most unreliable and suspicious human on the planet. In all honestly, he really wasn't doing her justice."
    "Every day since the three of you met, misfortune plagued Ulka's every waking moment. From mildly unfortunate things like dropping her ice cream on a summer day to borderline cartoonish scenarios where the wind would blow a bag of illegal substances in through her bedroom window while her mom was looking through her room,"
    "almost every situation she got into was just as, if not more, comically unlucky than the last. And if her lack of fortune wasn't enough to make your head spin, her utter lack of grace certainly was."
    "To put her clumsiness into perspective, one day, while trying to throw away her food in high school, Ulka somehow managed to \"accidentally\" knock the food trays out the hands of every single person in a crowded cafeteria..."
    "...during ONE lunch period..."
    "...before somehow setting the trashcan on fire."
    "Incidents like these were what made up the majority of Ulka's life."
    "It was ironic, really. For someone as intelligent and paranoid as her, you'd expect her life to be less...silly."

    a "We've got a couple minutes before Ulka gets here. And I don't know about you, but I am B-O-R-E-D, BORED!"
    if punch == True:
        a "And shreddin' your eardrums for punching me wasn't fun for as long as I thought it'd be."
        a "..."
	# the tags here make the text appear for, like, half a second so the player barely has time to process it
        a "...dick{nw}{done}"
    a "I'm gonna head to the hot-dog stand on the other side of the park. You should come with me!"
    a "Hopefully Ulka won't slip on a banana peel and slide into the road while we're gone or somethin'."   
    "In classic Asher fashion, you were given no time to accept or refuse his proposal before he slipped on his tacky leather jacket and sassily skipped down the sidewalk."
    "Better follow him then before he somehow manages to get lost."

	# everything from here on out is for the navigation system I added
    call screen NavigatePark()
    
    label Park:
    scene bg park1
    call screen NavigatePark()

    label NorthPark:
    scene bg parkplaceholder2
    call screen NavigateNorthPark()

    label NorthEastPark:
    scene bg parkplaceholder3
    call screen NavigateNorthEastPark()

    label NorthWestPark:
    scene bg parkplaceholder4
    call screen NavigateNorthWestPark()

    label NorthWestNorthPark:
    scene bg parkplaceholder5
    call screen NavigateNorthWestNorthPark() 

    label NortherPark:
    scene bg parkplaceholder6
    call screen NavigateNortherPark()

    # Story continues here, but it's not done and still on hiatus soooooooooooooooooooo
    label NorthestPark:
    scene bg parkplaceholder7

    "to be continued :)" 


	# also, return brings you back to the main menu
    return
