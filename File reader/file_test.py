try:
    with open("File reader/notes.txt", "r") as file:
        content = file.read()

    print(content)

    with open("notes.txt", "a") as file:
        newContent = file.write("TypeScript\n")

    with open("notes.txt", "r") as file:
        newContentRead = file.read()

    print(newContentRead)
except FileNotFoundError:
    print("File not found!")
finally:
    print("Program finished!")
