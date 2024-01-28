import random

high_score = 0

def dice_game():
    while True:
        global high_score
        print("Current High Score: " + str(high_score))
        print("1) Roll Dice")
        print("2) Leave Game") 
        option = input("Enter your choice: ")
        if option == "1":
            dice_roll = random.randint(1, 6)
            dice_roll2 = random.randint(1, 6)
            total = dice_roll + dice_roll2
            print("")
            print("You roll a... " + str(dice_roll))
            print("You roll a... " + str(dice_roll2))
            print("You have rolled a total of " + str(total))
            print("")
            if total > high_score:
                high_score = total
                print("You have achieved a new high score!")
        elif option == "2":
                print("You have left the game!")
                break
dice_game()
