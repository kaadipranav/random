def averageTuple(exampleTuple: tuple) -> None:
    for iteration_1 in exampleTuple:
        totalSum: int = 0
        average: int = 0
        for iteration_2 in iteration_1:           
            totalSum += iteration_2

        average = totalSum / len(iteration_1)
        print(average)
        return
    return
while True:
    choice = int(input('''
1. Run the code with your tuple
2. Exit
Enter your choice: '''))
    if choice == 1:
        inputTuple = eval(input("Enter a tuple here: "))
        averageTuple(inputTuple)
    elif choice == 2:
        print('Exiting program ....')
        # time.sleep(1)
    else:
        print('Invalid choice, kindly choose between 1/2 ONLY')

    
