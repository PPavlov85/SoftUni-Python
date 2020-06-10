import os

while True:
    line = input().split("-")
    command = line[0]
    if command == "End":
        break
    file_name = line[1]

    if command == "Create":
        with open(file_name, "w") as file:
            file.write("")

    elif command == "Add":
        content = line[2]
        with open(file_name, "a") as file:
            file.write(content)
            file.write("\n")

    elif command == "Replace":
        old_str = line[2]
        new_str = line[3]
        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                text = file.read()
            text = text.replace(old_str, new_str)
            with open(file_name, "w") as file:
                file.write(text)
        else:
            print("An error occurred")

    elif command == "Delete":
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")
