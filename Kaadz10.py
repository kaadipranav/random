filename = 'myfile.txt'

def appendLine(new_line: str) -> None:
    with open(filename, 'a') as f:
        f.write(new_line + '\n')
    print("Line added!")

def displayStats() -> None:
    with open(filename, 'r') as f:
        lines = f.readlines()
        content = "".join(lines)
        
        num_lines = len(lines)
        num_words = len(content.split())
        num_chars = len(content)
        
        print(f"Stats: {num_lines} lines, {num_words} words, {num_chars} characters.")

def displayContent() -> None:
    with open(filename, 'r') as f:
        print("--- File Content ---")
        print(f.read())
        print("--------------------")

def editLine(line_number: int, new_text: str) -> None:
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    if 0 <= line_number - 1 < len(lines):
        lines[line_number - 1] = new_text + '\n'
        with open(filename, 'w') as f:
            f.writelines(lines)
        print("Line edited!")
    else:
        print("That line doesn't exist.")

def deleteLine(line_number: int) -> None:
    with open(filename, 'r') as f:
        lines = f.readlines()
        
    if 0 <= line_number - 1 < len(lines):
        del lines[line_number - 1]
        with open(filename, 'w') as f:
            f.writelines(lines)
        print("Line deleted!")
    else:
        print("That line doesn't exist.")

appendLine("Hello World")
displayStats()
displayContent()