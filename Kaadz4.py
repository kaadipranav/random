sentence: str = input("Enter a sentence: ")
def reverse_words(x: str) -> str:
    words: list = x.split()
    words2: str = ''
    for i in words:
        words2 += i[::-1] + ' '
    return words2
def characters(x: str) -> None:
    words: list = x.split()
    upper: int = 0
    lower: int = 0
    for i in words:
        for j in i:
            if j.isupper():
                upper += 1
            elif j.islower():
                lower += 1
    print(f'Number of uppercase words: {upper}, Number of lowercase words: {lower}')
    return
def palindrome_words(x: str) -> list:
    palindrome_words: list = []
    words: list = x.split()
    for i in words:
        if i == i[::-1]:
            palindrome_words.append(i)
    return palindrome_words
while True:
    choice = int(input('''
1. Display reverse of each word
2. Display number of lowercase and uppercase characters
3. Dispay palindrome words
---
Enter your choice: '''))
    if choice == 1:
        print(reverse_words(str(sentence)))
    elif choice == 2:
        characters(str(sentence))
    elif choice == 3:
        print(palindrome_words(str(sentence)))
    elif choice == 4:
        break
    else:
        print("Entered invalid choice kindly choose between 1,2,3 and 4")


        
                
                
