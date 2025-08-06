import random
import time
import os
employees = [
    {"id": f"id number {i+random.randint(1,1000)}", "name": f"employee {i+1}", "salary": 1000 + (i // random.randint(1,10)) * random.randint(100, 500)}
    for i in range(40)
]

def orders():
    print("")

def russian_roulette():
    print("are you sure?")
    time.sleep(3)
    clear_terminal()
    print("...")
    time.sleep(2)
    print("not that you have a choice")
    time.sleep(1)
    print("commencing...")
    time.sleep(2)
    clear_terminal()
    print("the gun. 6 chambers, 1 bullet")
    time.sleep(1)
    print("you will play against an opponent")
    time.sleep(1)
    print("you will both take turns pulling the trigger, or spin the chamber before pulling the trigger")
    time.sleep(1.5)
    clear_terminal()
    print("now commence.")
    time.sleep(2)
    clear_terminal()
    print("your turn first")
    time.sleep(1)
    print("pull the trigger, or spin the chamber?")
    choice = input("your answer: ").strip().lower()
    if choice == "pull" or choice == "trigger" or choice == "pull the trigger" or choice == "pull trigger" or choice == "trigger pull":
        print("you pull the trigger...")
        time.sleep(1)
        if random.randint(1, 6) == 1:
            quit()
            exit(0)
        else:
            print("click! you survived")
            print("now youll go back the main menu bcs i cant be bothered to code the opponent")
            time.sleep(3)
            clear_terminal()
    elif choice == "spin" or choice == "spin the chamber" or choice == "spin chamber" or choice == "chamber spin":
        print("you spin the chamber and pull the trigger...")
        time.sleep(1)
        if random.randint(1, 6) == 1:
            quit()
            exit(0)
        else:
            print("click! you survived")
            print("now youll go back the main menu bcs i cant be bothered to code the opponent")
            time.sleep(3)
            clear_terminal()
    else:
        print("invalid choice, you lose by default")
        time.sleep(1)
        quit()
        exit(0)
    




def clear_terminal():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

clear_terminal()
time.sleep(1)
print("hi")
time.sleep(2)
clear_terminal()
time.sleep(1)
print("loading.")
time.sleep(1)
clear_terminal()
print("loading..")
time.sleep(1)
clear_terminal()
print("loading...")
time.sleep(1)
clear_terminal()
print("-"*20)
print(" /$$                 /$$ /$$          \n| $$                | $$| $$          \n| $$$$$$$   /$$$$$$ | $$| $$  /$$$$$$ \n| $$__  $$ /$$__  $$| $$| $$ /$$__  $$\n| $$  \ $$| $$$$$$$$| $$| $$| $$  \ $$\n| $$  | $$| $$_____/| $$| $$| $$  | $$\n| $$  | $$|  $$$$$$$| $$| $$|  $$$$$$/\n|__/  |__/ \_______/|__/|__/ \______/ ")
print("-"*20)
time.sleep(2)
print("welcome to this program bro")
time.sleep(3)
clear_terminal()
while True:
    print("heres a list of ur options gro:")
    print("1. view employees")
    print("/"*20)
    opt_input=input("input your opt here vro (1-4): ")
    try:
        opt_input = int(opt_input)
    except ValueError:
        print("error: yo vro thats not a number, try again cro")
        time.sleep(2)
        clear_terminal()
        continue
    if opt_input == 1:
        clear_terminal()
        print("loading...")
        time.sleep(3)
        clear_terminal()
        for i, employee in enumerate(employees, start=1):
            print(f"{i}. {employee['name']} - {employee['id']} - ${employee['salary']}")
            time.sleep(0.1)
        print("---end of list---")
    elif opt_input == 2:
        print()
        clear_terminal()
    elif opt_input == 3:
        print()
        clear_terminal()
    elif opt_input == 4:
        print()
        clear_terminal()
    elif opt_input == 1997:
        russian_roulette()
    else:
        print("error: yo vro theres no opt like that, try again cro")
        time.sleep(2)
        clear_terminal()
        continue