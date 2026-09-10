import random
def roll_dice():
    return random.randint(1,6)
def love_game():
    print("Welcome to the Love Dice Adventure Mr.Nirajan")
    print("Roll the dice darling to see what you won!")
    dice=roll_dice()
    print("You rolled:",dice)
    if dice==1:
        print("Give me choclate")
    elif dice==2:
        print("Give me kiss")
    elif dice==3:
        print("Give me chura and mehendi")
    elif dice==4:
        print("You are hero")
    elif dice==5:
        print("You are my darling")
    else:
        print("Yay you are my Nirajan the don wowowo")
while True:
        love_game()
        again=input("Do you want to play again?(yes/no):")
        if again.lower()!="yes":
            break
        