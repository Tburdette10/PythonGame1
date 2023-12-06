import time

def intro():
    print("Welcome to Ravenflag.")
    print("You find yourself waking up in the early hours of the morning in the back of a cave")
    time.sleep(2)
    print("You have no recollection how you got there, or who you are for that matter.")
    time.sleep(2)
    print("You hear something approaching the mouth of the cave. Do you try to escape before it arrives, or do you search for a hiding spot in the cave?")

def choose_path():
    print("1. Escape before it arrives.")
    print("2. Hide in the cave.")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        escape_cave()
    elif choice == "2":
        hide_cave()
    else: 
        print("Invalid choice. Please enter 1 or 2.")
        choose_path()

def escape_cave():
    print("You escape just in time! The wretched creature appears to be dragging a large wolf into the cave.")
    time.sleep(2)
    print("Fighting this beast will surely result in death.")
    time.sleep(2)
    print("Now that you're out of the cave, you find two paths ahead of you.")
    time.sleep(2)
    print("The first path leads you to a large river, while the second path leads you to a dense forest.")
    time.sleep(2)
    print("Will you take the first path or the second?")
    time.sleep(2)
    print("1. Head to the river.")
    print("2. Head to the forest.")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        river_path()
    elif choice =="2":
        woods_path()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        escape_cave()

def hide_cave():
    print("You find a large gathering of boulders to hide behind. The air in the cave fills with the stench of death as the beast enters it's home.")
    time.sleep(2)
    print("You notice that the beast is dragging a large wolf into the cave. Do you continue to hide, or do you try to run?")
    time.sleep(2)
    print("1. Continue hiding.")
    print("2. Run.")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        continue_hide()
    elif choice == "2":
        flee_cave()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        hide_cave()

def continue_hide():
    print("You remain silent as you hide against the rocks. You notice the beast has let go of his meal as he starts to sniff the air. You hear an ear piercing roar just as the beast starts to charge toward your rock pile.")
    time.sleep(2)
    print("The beast brutally slaughters you for trespassing in his cave.")
    time.sleep(2)
    print("The end.")
    intro()
    choose_path()

def flee_cave():
    print("You frantically flee the cave. The beast does not pursue as it has already exhausted itself after it's combat with the large wolf.")
    time.sleep(2)
    print("Now that you're out of the cave, you find two paths ahead of you.")
    time.sleep(2)
    print("The first path leads you to a large river, while the second path leads you to a dense forest.")
    time.sleep(2)
    print("Will you take the first path or the second?")
    time.sleep(2)
    print("1. Head to the river.")
    print("2. Head to the forest.")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        river_path()
    elif choice == "2":
        woods_path()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        flee_cave()

def river_path():
    print("You walk towards the river. It appears to be too large and flowing too aggressively to swim across, and stretches for miles in either direction.")
    time.sleep(2)
    print("To the North, you find a city with a large concrete wall surrounding its border. To the South, you find a small camp. The camp is hoisting a flag of sorts, but you are unable to make out what it says.")
    time.sleep(2)
    print("Will you take the path to the North, or to the South?")
    time.sleep(2)
    print("1. Head North.")
    print("2. Head South.")   

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        head_north()
    elif choice == "2":
        head_south()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        river_path()

def woods_path():
    print("You walk towards the dense forest. As you near the entrance, you hear the screeches and groans of creatures much larger than yourself. You cautiously take your first few steps into the forest. The early morning sun light is unable to penetrate the thick canopy above, leaving dark shadows all over the forest floor.")
    time.sleep(2)
    print("Suddenly, a large owl like creature drops onto you from a branch above. It's sharp talons begin to sink into your skin and the light fades from your eyes.")
    time.sleep(2)
    print("The end.")
    intro()
    choose_path()

def head_north():
    print("You start to approach the large wall along the cities border. You look to see if there is an entrance nearby, but there does not appear to be one from this side. You do however, find a large crack in the wall. You climb inside the crack and find yourself inside the bustling city.")
    time.sleep(2)
    print("As you explore the city, the townfolk began to grow cautious of you. No one seems to recognize you, nor want your presence inside their walls. One individual approaches you. 'Halt!' he shouts.")
    time.sleep(2)
    print("Worried, you decide to turn the opposite direction and run back to the large crack in the wall. Before you can make it, you hear a loud thud and feel a rush of warm liquid run down your skin. You look down to find that you've been shot with an arrow. You fall to the ground, unable to move as you drift away into a timeless sleep.")
    time.sleep(2)
    print("The end.")
    intro()
    choose_path()

def head_south():
    print("You approach the small camp along the river. You find that the flag has a large raven drawn onto it. The camp seems to be heavily armed with bows and swords alike.")
    time.sleep(2)
    print("'Vasilis? Is that you?'. You turn towards the voice to find a man in purple waving you down. 'Bless the new Gods and the Old! We never thought we would find you! Where have you been?' he exclaims. The man seems to know who you are, but you are unable to recall who he is.")
    time.sleep(2)
    print("'You must be exhausted. Let's get you patched up so we can discuss what has happened. Welcome back to Ravenflag, warrior!'")
    time.sleep(2)
    print("The end.")

intro()
choose_path()     