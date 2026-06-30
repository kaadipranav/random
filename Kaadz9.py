print("Enter 5 proverbs:")
proverbs = []
for i in range(5):
    p = input("Proverb " + str(i+1) + ": ")
    proverbs.append(p)

file1 = open("proverbs.txt", "w")
for p in proverbs:
    file1.write(p + "\n")
file1.close()

word = input("Enter a starting word to filter: ")

file2 = open("filtered.txt", "w")
matches = []

for p in proverbs:
    if p.lower().startswith(word.lower()):
        file2.write(p + "\n")
        matches.append(p)

file2.close()

print("\nFiltered results:")
if len(matches) == 0:
    print("• No matches found.")
else:
    for p in matches:
        print("• " + p)

