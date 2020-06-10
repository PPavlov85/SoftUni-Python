result_text = ""

with open("text.txt", "r") as file:
    for index, line in enumerate(file):
        counter = 0
        length = len([x for x in line if x.isalpha()])
        for el in line:
            if el in ",.-!?':\";":
                counter += 1

        result_text += f"Line {index + 1}: {line[:-2]} ({length})({counter})\n"

with open("output.txt", "w") as file:
    file.write(result_text)
