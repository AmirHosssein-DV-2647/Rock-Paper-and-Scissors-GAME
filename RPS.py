# IMPORTS
from colorama import Fore, init
import time
import random
from random import choice
init()

# APP CODES
while True:
    print(Fore.LIGHTCYAN_EX + "For Cancle Playing : CTRL + C")
    User = str(input("Rock, Paper or Scissors?  Write >> "))

    System = ["Rock", "Paper", "Scissors"]
    R = random.choice(System)
    if (User.lower() == "rock" and R == "Scissors") or (User.lower() == "paper" and R == "Rock") or (User.lower() == "scissors" \
        and System == "Paper"):
        time.sleep(1)
        print(Fore.YELLOW + "Your Choice: {} And The System Choice: {}".format(User, R))
        print(Fore.GREEN + "You're The WINNER :))

    elif (User.lower() == "rock" and R == "Paper") or (User.lower() == "paper" and R == "Scissors") or (User.lower() == "scissors" \
        and System == "Rock"):
        time.sleep(1)
        print("Your Choice: {} And The System's Choice: {}".format(User, R))
        print(Fore.LIGHTMAGENTA_EX + "System Is The WINNER :)")     
    elif User.lower() == R.lower():
        time.sleep(2)
        print(Fore.BLUE + "Same Choice.")
    else:
        print(Fore.BLACK + "Choice A Word That Listed.")
