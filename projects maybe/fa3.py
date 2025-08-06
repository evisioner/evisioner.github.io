import random
import time
import os

employees = [
    {"id": f"id number {i+random.randint(1,1000)}", "name": f"employee {i+1}", "salary": 1000 + (i // random.randint(1,10)) * random.randint(100, 500)}
    for i in range(40)
]

def russian_roulette():
    print(">are you sure?")
    time.sleep(3)
    clear_terminal()
    print(">...")
    time.sleep(2)
    print(">not that you have a choice")
    time.sleep(1)
    print(">commencing...")
    time.sleep(2)
    clear_terminal()
    print(">the gun. 6 chambers, 1 bullet")
    time.sleep(1)
    print(">you will play against an opponent")
    time.sleep(1)
    print(">you will both take turns pulling the trigger, or spin the chamber before pulling the trigger")
    time.sleep(1.5)
    clear_terminal()
    print(">now commence.")
    time.sleep(2)
    clear_terminal()

    turn = 1
    remaining_chambers = 6
    oppo_stat=1
    while oppo_stat == 1:
        if turn == 1:
            print(">your turn")
            choice = input(">>pull the trigger, or spin the chamber?...or point the gun at your opponent? ").strip().lower()
            if choice in ["pull", "trigger", "pull the trigger", "pull trigger", "trigger pull"]:
                print(">you pull the trigger...")
                time.sleep(1)
                if random.randint(1, remaining_chambers) == 1:
                    print("only the dead has seen the end of war")
                    time.sleep(2)
                    clear_terminal()
                    quit()
                    exit(0)
                else:
                    remaining_chambers -= 1
                    print(">click! you survived")
                    time.sleep(1.5)
                    clear_terminal()
            elif choice in ["spin", "spin the chamber", "spin chamber", "chamber spin"]:
                print(">you spin the chamber and pull the trigger...")
                remaining_chambers = 6
                time.sleep(1)
                if random.randint(1, 6) == 1:
                    print("the truth lies rather obcsured")
                    time.sleep(2)
                    clear_terminal()
                    quit()
                    exit(0)
            elif choice in ["point", "point the gun", "point gun", "aim"]:
                print(">you point the gun at your opponent...")
                time.sleep(1)
                if random.randint(1, remaining_chambers) == 1:
                    oppo_stat = 0
                    print(">...")
                    time.sleep(3)
                    print(">you win")
                    time.sleep(2)
                    clear_terminal()
                    print(">...")
                    time.sleep(2)
                    print(">do you feel regret?")
                    time.sleep(1)
                else:
                    remaining_chambers -= 1
                    print(">click. lost your chance")
                    time.sleep(1.5)
                    clear_terminal()
                    turn = 0
            else:
                print(">invalid choice")
                print(">mindless violence is not the answer, but it is the question, and the answer is yes")
                time.sleep(1)
                clear_terminal()
                quit()
                exit(0)
        else:
            print(">opponent's turn...")
            time.sleep(1)
            opp_choice = random.choice(["pull", "spin", "aim"])
            if opp_choice == "pull":
                print(">opponent pulls the trigger...")
                time.sleep(1)
                if random.randint(1, remaining_chambers) == 1:
                    print(">...")
                    time.sleep(3)
                    print(">opponent lost. you win")
                    time.sleep(2)
                    clear_terminal()
                    print(">...")
                    time.sleep(2)
                    print("no one could judge you")
                    time.sleep(1)
                else:
                    print(">click! opponent survived")
                    time.sleep(1.5)
                    clear_terminal()
                    remaining_chambers -= 1
            elif opp_choice == "spin":
                remaining_chambers = 6
                print(">opponent spins the chamber and pulls the trigger...")
                time.sleep(1)
                if random.randint(1, 6) == 1:
                    print(">...")
                    time.sleep(3)
                    print(">opponent lost. you win")
                    time.sleep(2)
                    clear_terminal()
                    print(">...")
                    time.sleep(2)
                    print("odds are alaways biases")
                    time.sleep(1)
                    break
            else:
                print(">the opponent points the gun at you...")
                time.sleep(1)
                if random.randint(1, remaining_chambers) == 1:
                    print("nothing comes after death, but death itself")
                    time.sleep(1)
                    clear_terminal()
                    quit()
                    exit(0)
                else:
                    print(">click! you survived")
                    time.sleep(1.5)
                    clear_terminal()
                    remaining_chambers -= 1
                    turn = 1

def view_employees():
    clear_terminal()
    print("loading...")
    time.sleep(3)
    clear_terminal()
    for i, employee in enumerate(employees, start=1):
        print(f"||{i}. {employee['name']} - {employee['id']} - ${employee['salary']}")
        time.sleep(0.1)
    print("---end of list---")

def add_employee():
    clear_terminal()
    print("loading...")
    time.sleep(3)
    clear_terminal()
    name = input(">>enter the name of the employee: ").strip()
    id_number = input(">>enter the id number of the employee: ").strip()
    try:
        salary = float(input(">>enter the salary of the employee: ").strip())
        if salary < 0:
            raise ValueError("!>why u tryna give them a negative salary bro? evil ahh mofo")
    except ValueError as e:
        print(f"!>error: {e}, try again cro, you cant give a negative salary or non-numeric value, type shi like 'hello' or '1000.50' is fine tro")
        time.sleep(2)
        clear_terminal()
    print(">yo, you'll be adding an employee with the following details:")
    print(f">Name: {name}")
    print(f">ID: {id_number}")
    print(f">Salary: ${salary}")
    confirm = input(">>u sure gang? (y/n): ").strip().lower()
    if confirm == 'y':
        employees.append({"id": id_number, "name": name, "salary": salary})            
        print(">employee added successfully, homie!!, returning u to the main menu...")
        time.sleep(2)
        clear_terminal()
    elif confirm == 'n':
        print(">type shi gang, returning u to the main menu...")
        time.sleep(2)
        clear_terminal()
    else:
        print("!>error: yo vro thats not a valid input, try again cro")
        time.sleep(2)
        clear_terminal()

def remove_employee():
    clear_terminal()
    print("loading...")
    time.sleep(3)
    clear_terminal()
    if not employees:
        print("no employees to remove, returning u to the main menu...")
        time.sleep(2)
        clear_terminal()
    print("here are the current employees:")
    time.sleep(1)
    clear_terminal()
    for i, employee in enumerate(employees, start=1):
        print(f"{i}. {employee['name']} - {employee['id']} - ${employee['salary']}")
        time.sleep(0.1)
    print("---end of list---")
    time.sleep(0.5)
    try:
        remove_index = int(input("enter the number of the employee you want to remove: ")) - 1
        if remove_index < 0 or remove_index >= len(employees):
            raise IndexError("invalid index, enter a number between 1 and " + str(len(employees)), ", try again cro")
    except (ValueError, IndexError) as e:
        print(f"error: {e}, try again cro, you need to enter a valid number between 1 and {len(employees)}")
        time.sleep(2)
        clear_terminal()
    clear_terminal()
    confirm = input(f"are you sure you want to remove {employees[remove_index]['name']}? (y/n): ").strip().lower()
    if confirm == 'y':
        removed_employee = employees.pop(remove_index)
        print(f"removed employee: {removed_employee['name']} - {removed_employee['id']} - ${removed_employee['salary']}, returning u to the main menu...")
        time.sleep(2)
        clear_terminal()
    elif confirm == 'n':
        print("type shi gang, returning u to the main menu...")
        time.sleep(2)
        clear_terminal()
    else:
        print("error: yo vro thats not a valid input, try again cro")
        time.sleep(2)
        clear_terminal()

def edit_employee():
    clear_terminal()
    print("loading...")
    time.sleep(3)
    clear_terminal()
    if not employees:
        print(">no employees to edit, returning u to the main menu...")
        time.sleep(2)
        clear_terminal()
    print(">here are the current employees:")
    time.sleep(1)
    clear_terminal()
    for i, employee in enumerate(employees, start=1):
        print(f"||{i}. {employee['name']} - {employee['id']} - ${employee['salary']}")
        time.sleep(0.1)
    print("---end of list---")
    time.sleep(0.5)
    if len(employees) == 0:
        print(">no employees to edit, returning u to the main menu...")
        time.sleep(2)
        clear_terminal()
        return
    try:
        edit_index = int(input(">>enter the number of the employee you want to edit: ")) - 1
        if edit_index < 0 or edit_index >= len(employees):
            raise IndexError("!>invalid index, enter a number between 1 and " + str(len(employees)), ", try again cro")
    except (ValueError, IndexError) as e:
        print(f"!>error: {e}, try again cro, you need to enter a valid number between 1 and {len(employees)}")
        time.sleep(2)
        clear_terminal()
    print(">reenter the details for the employee:")
    time.sleep(1)
    clear_terminal()
    name = input(">>enter the new name of the employee: ").strip()
    id_number = input(">>enter the new id number of the employee: ").strip()
    salary = input(">>enter the new salary of the employee: ").strip()
    try:
        salary = float(salary)
        if salary < 0:
            raise ValueError("!>why u tryna give them a negative salary bro? evil ahh mofo")
    except ValueError as e:
        print(f"!>error: {e}, try again cro, you cant give a negative salary or non-numeric value, type shi like 'hello' or '1000.50' is fine tro")
        time.sleep(2)
        clear_terminal()
    print(">yo, you'll be editing the employee with the following details:")
    print(f">Name: {name}")
    print(f">ID: {id_number}")
    print(f">Salary: ${salary}")
    confirm = input(">>u sure gang? (y/n): ").strip().lower()
    if confirm == 'y':
        employees[edit_index] = {"id": id_number, "name": name, "salary": salary}
        print(">employee edited successfully, homie!!, returning u to the main menu...")
        time.sleep(2)
        clear_terminal()
    elif confirm == 'n':
        print(">type shi gang, returning u to the main menu...")
        time.sleep(2)
        clear_terminal()
    else:
        print("!>error: yo vro thats not a valid input, try again cro")
        time.sleep(2)
        clear_terminal()

def clear_terminal():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def slow_print(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

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
print("program version: 06.08.2025")
time.sleep(1)
print("os: " + os.name)
time.sleep(1)
print("python version: " + os.sys.version.split()[0])
time.sleep(1)
print("author: datpham")
time.sleep(3)
clear_terminal()
time.sleep(2)
for e in range(0,10):
    print("booting up...", end=e*'/', flush=True)
    time.sleep(0.5)
    clear_terminal()
clear_terminal()
print("booting up...", "/"*10, end="...Done!\n")
time.sleep(1)
clear_terminal()
time.sleep(1)
print("-"*20)
slow_print(" /$$                 /$$ /$$          \n| $$                | $$| $$          \n| $$$$$$$   /$$$$$$ | $$| $$  /$$$$$$ \n| $$__  $$ /$$__  $$| $$| $$ /$$__  $$\n| $$  \ $$| $$$$$$$$| $$| $$| $$  \ $$\n| $$  | $$| $$_____/| $$| $$| $$  | $$\n| $$  | $$|  $$$$$$$| $$| $$|  $$$$$$/\n|__/  |__/ \_______/|__/|__/ \______/ ")
print("-"*20)
time.sleep(2)
slow_print(">welcome to this program bro")
time.sleep(3)
clear_terminal()

while True:
    print(">heres a list of ur options gro:")
    print("||1. view employees")
    print("||2. add employee")
    print("||3. remove employee")
    print("||4. edit employee")
    print("||0. exit program")
    print("/"*20)
    opt_input=input(">>input your opt here vro (0-4): ")
    try:
        opt_input = int(opt_input)
    except ValueError:
        print("error: yo vro thats not a number, try again cro")
        time.sleep(2)
        clear_terminal()
        continue
    if opt_input == 1:
        view_employees()
    elif opt_input == 2:
        add_employee()
    elif opt_input == 3:
        remove_employee()
    elif opt_input == 4:
        edit_employee()
    elif opt_input == 1997:
        russian_roulette()
    elif opt_input == 0:
        clear_terminal()
        print("exiting program.")
        time.sleep(1)
        clear_terminal()
        print("exiting program..")
        time.sleep(1)
        clear_terminal()
        print("exiting program...")
        time.sleep(1)
        clear_terminal()
        quit()
        exit(0)
    else:
        print("error: yo vro theres no opt like that, try again cro")
        time.sleep(2)
        clear_terminal()
        continue