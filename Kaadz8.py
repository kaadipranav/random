from typing import List, Any

def search_student(student_records: List[List[Any]], roll_to_find: int) -> Any:
    for student in student_records:
        if student[0] == roll_to_find:
            return student
    return "Student not found."

def filter_by_name(student_records: List[List[Any]]) -> str:
    filtered_list: List[List[Any]] = []
    
    for student in student_records:
        student_name: str = student[1]
        if student_name[0].lower() in ['a', 's']:
            filtered_list.append(student)
            
    return f"Details of names starting with A and S are: {filtered_list}"

student_database = eval(input("Enter student data (as a list of lists): "))

while True:
    print('''
    1. Search by roll
    2. Display details of names starting with "A" and "S"
    3. Exit
    ''')
    
    user_choice = int(input("Enter your choice: "))
    
    if user_choice == 1:
        roll_input = int(input("Enter roll: "))
        print(search_student(student_database, roll_input))
    elif user_choice == 2:
        print(filter_by_name(student_database))
    elif user_choice == 3:
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")


