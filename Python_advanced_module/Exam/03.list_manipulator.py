def list_manipulator(numbers, *parameters):
    result = []
    if parameters[0] == "remove" and parameters[1] == "end":
        if len(parameters) > 2:
            n = parameters[2]
            result = numbers[:-n]
        else:
            numbers.pop()
            result = numbers

    elif parameters[0] == "remove" and parameters[1] == "beginning":
        if len(parameters) > 2:
            n = parameters[2]
            result = numbers[n:]
        else:
            numbers.pop(0)
            result = numbers

    elif parameters[0] == "add" and parameters[1] == "beginning":
        if len(parameters) > 2:
            new_list = []
            for n in range(2, len(parameters)):
                new_list.append(parameters[n])
            result = new_list + numbers

    elif parameters[0] == "add" and parameters[1] == "end":
        if len(parameters) > 2:
            new_list = []
            for n in range(2, len(parameters)):
                new_list.append(parameters[n])
            result = numbers + new_list

    return result


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
