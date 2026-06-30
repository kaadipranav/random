def is_word_chain(word1: str) -> str:
    words = word1.split()
    if len(words) < 2:
        return False

    for i in range(len(words) - 1):
        if words[i][-1] != words[i + 1][0]:
            print('Not a word chain')
            return False

    print('Is a word chain')
    return True

y = input("Enter a sequence: ")
is_word_chain(y)
