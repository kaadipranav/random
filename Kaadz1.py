x: list = []
inp1 = input("Enter a list of numbers separated by spaces: ")
for m in inp1.split():
    x.append(int(m))
def add(add1: int) -> None:
    x.append(add1)
    x.sort()
def delete(del1: int) -> None:
    if del1 in x:
        x.remove(del1)
    else:
        print(f'The element {del1} is not in the list')
def asc():
    x.sort()
    print(x)
def des():
    x.sort(reverse=True)
    print(x)
def reverse():
    x1: list = []
    for i in x:
        x1.append(i)
    x1.reverse()
    print(x1)
def display():
    print(x)
while True:
    y = int(input('''
1. Add element
2. Remove element
3. Display in ascending order
4. Display in descending order
5. Display reverse of elements
6. Display list
7. Exit
----
Enter your choice: '''))
    if y == 1:
        add2 = int(input("Enter the element you want to add: "))
        add(add2)
    elif y == 2:
        del2 = int(input("Enter the element you want to delete: "))
        delete(del2)
    elif y == 3:
        print("LIST IN ASCENDING ORDER: ")
        asc()
    elif y == 4:
        print("LIST IN DESCENDING ORDER: ")
        des()
    elif y == 5:
        print("LIST IN REVERSED ORDER: ")
        reverse()
    elif y == 6:
        print("DISPLAYING LIST: ")
        display()
    else:
        print("Exiting.......... ")
        break
