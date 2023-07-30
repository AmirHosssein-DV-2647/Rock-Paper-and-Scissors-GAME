# IMPORTS
from colorama import Fore, init
import subprocess
import time
import random
from random import choice
init()

subprocess.call("clear", shell=True)
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
        print(Fore.GREEN + "You're The WINNER :)")
        time.sleep(3)
        subprocess.call("clear", shell = True)

    elif (User.lower() == "rock" and R == "Paper") or (User.lower() == "paper" and R == "Scissors") or (User.lower() == "scissors" \
        and System == "Rock"):
        time.sleep(1)
        print("Your Choice: {} And The System's Choice: {}".format(User, R))
        print(Fore.LIGHTMAGENTA_EX + "System Is The WINNER :)")
        time.sleep(3)
        subprocess.call("clear", shell = True)
        
    elif User.lower() == R.lower():
        time.sleep(2)
        print(Fore.BLUE + "Same Choice.")
        time.sleep(3)
        subprocess.call("clear", shell = True)

    else:
        print(Fore.BLACK + "Choice A Word That Listed.")
        time.sleep(3)
        subprocess.call("cls", shell = True)
