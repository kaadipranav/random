def largest(x: str) -> None:
    words: list = x.split()
    largest_1: str = ''
    largest_2: str = ''
    largest_1 = max(words, key = len)
    words.remove(largest_1)
    largest_2 = max(words, key = len)
    print(f"The largest word in the sentence is: {largest_1} and the second largest word is: {largest_2}")
    return 
def smallest(x: str) -> None:
    words: list = x.split()
    smallest_1: str = ''
    smallest_2: str = ''
    smallest_1 = min(words, key = len)
    words.remove(smallest_1)
    smallest_2 = min(words, key = len)
    print(f"The smallest word in the sentence is: {smallest_1} and the second smallest word is: {smallest_2}")
    return
def reverse_sentence(x: str) -> None:
    print(f"The reversed sentence is: {x[::-1]}")
    return
def title_case(x: str) -> None:
    words = x.split()
    new_str: str = ''
    for i in words:
        new_str += i.title() + ' '
    print(f"Your sentence in title case: {new_str}")
def starting_with(x: str) -> None:
    char = str(input("Enter a letter: "))
    words: list = x.split()
    new_str: str = ''
    for i in words:
        if i[0] == char:
            new_str += i + ', '
    print(f"Words starting with {char} are: {new_str}")
sentence = str(input("Enter a sentence: "))
while True:
    choice = int(input('''
1. Display the first and second largest words
2. Display the first and second smallest words
3. Display the reverse of the sentence
4. Convert all words to title case
5. Display words starting with the given character
6. Exit
---
Enter your choice here: '''))
    if choice == 1:
        largest(sentence)
    elif choice == 2:
        smallest(sentence)
    elif choice == 3:
        reverse_sentence(sentence)
    elif choice == 4:
        title_case(sentence)
    elif choice == 5:
        starting_with(sentence)


	

	
