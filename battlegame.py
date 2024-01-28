wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150
dragon_hp = 300

wizard_damage = 150
elf_damage = 100
human_damage = 20
dragon_damage = 50

while True:
    print("1. " + wizard)
    print("2. " + elf)
    print("3. " + human)
    print('')
    character = input("Choose your character: ")
    if (character == "1"):
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        print("You have chosen the character: " + character)
        print ("Health: " + str(my_hp))
        print ("Damage: " + str(my_damage))
        print ('')
        break
    elif (character == "2"):
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        print("You have chosen the character: " + character)
        print ("Health: " + str(my_hp))
        print ("Damage: " + str(my_damage))
        break
    elif (character == "3"):
        character = human
        my_hp = human_hp
        my_damage = human_damage
        print("You have chosen the character: " + character)
        print ("Health: " + str(my_hp))
        print ("Damage: " + str(my_damage))
        print('')
        break
    else: 
        print("Unknown Character")
while True:
    dragon_hp = dragon_hp - my_damage 
    my_hp = my_hp - dragon_damage
    print("The", character, "damaged the dragon!")
    print("The Dragon's hitpoints are now: " + str(dragon_hp))
    print('')
    print("The Dragon strikes back at the " + character + "!")
    print("The", str(character) + "'s hitpoints are now: " + str(my_hp))
    print('')

    if (dragon_hp == 0 or dragon_hp < 0):
        print("The Dragon has lost the battle.")
        break
    elif (my_hp == 0 or my_hp < 0):
        print("The", character, "has lost the battle.")
        break

