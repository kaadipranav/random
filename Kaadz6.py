from colorama import init, Fore, Style

RED    = "\033[31m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
BLUE   = "\033[34m"
RESET  = "\033[0m"

print(f"{RED}This is red{RESET}")
print(f"{GREEN}This is green{RESET}")
print(f"{YELLOW}This is yellow{RESET}")
print(f"{BLUE}This is blue{RESET}")


import time
dict1: dict = {}

numberofStudents = int(input("Enter the number of students you would like to store: "))
for i in range(numberofStudents):
    name1 = str(input(f"\nEnter name of student {i+1}: "))
    age1 = int(input(f"Enter age of student {i+1}: "))

    dict1[name1] = age1

def add_element(x: dict) -> None:
    new_name = str(input("Enter the name of the new student: "))
    new_age = int(input("Enter the age of the new student: "))

    x[new_name] = new_age
    print('\n------------- UPDATED DICTIONARY -------------\n\n')
    print('▬' * 50)
    print(f"{'N A M E':<15} \t {'A G E':<15}")
    print('▬' * 50)
    for key, value in x.items():
        print(f'‖ {str(key):<15} ‖ {str(value):<15}')

    print('\n\n-----------------------------------------------')


def search_name(x: dict) -> bool:
    name = str(input("Enter the name of the student: "))
    
    if name in x.keys():
        print(f'''
-----------------------------------------------
{name} found in the dictionary
-----------------------------------------------''')
        return True
    else:
        print(f'''
-----------------------------------------------
{name} not found in the dictionary
-----------------------------------------------''')
        return False
    return False

def edit_byname(x: dict) -> None:
    name = str(input("Enter the name of the student: "))
    
    if name in x.keys():
        choice = int(input('Enter the updated age: '))
        x[name] = choice
    
        print('\n------------- UPDATED DICTIONARY -------------\n\n')
        print('·' * 25)
        print(f"{'⁌ N A M E ⁍':<15} {'⁌ A G E ⁍':<15}")
        print('·' * 25)
        for key, value in x.items():
            print(f'{str(key):<15} {str(value):<15}')

        print('\n\n-----------------------------------------------')
        
    else:
        print(f'''
-----------------------------------------------
Name {name} is not in the dictionary currently
-----------------------------------------------''') 
        return
    
def delete_element(x: dict) -> None:
    name = str(input("Enter the name of the student: "))
    
    if name in x.keys():
        del x[name]
        print(f'''
-----------------------------------------------
{name} has been removed from the dictionary
-----------------------------------------------''')
        return
    
    else:
        print(f'''
-----------------------------------------------
Name {name} not found in the dictionary
-----------------------------------------------''')
        return

def average_age(x: dict) -> None:
    total: int = 0
    average: int = 0
    
    for i in x.values():
        total += i

    average = total / len(x.keys())
    print(f'''
-----------------------------------------------
Average age is {average}
-----------------------------------------------''')
    return

while True:
    user_choice = int(input('''
1. Add element to the dictionary
2. Search element by name in the dictionary
3. Edit by name from the dictionary
4. Delete element from the dictionary
5. Display average age of students
6. Exit the application
===================================================
Enter your choice: '''))

    if user_choice == 1:
        add_element(dict1)
    elif user_choice == 2:
        search_name(dict1)
    elif user_choice == 3:
        edit_byname(dict1)
    elif user_choice == 4:
        delete_element(dict1)
    elif user_choice == 5:
        average_age(dict1)
    elif user_choice == 6:
        print('Exiting program', end = '')
        for i in range(20):
            time.sleep(0.1)
            print('.', end = '')
        break
    
    else:
        print("Invalid choice, please choose between 1/2/3/4/5/6 only")
        
