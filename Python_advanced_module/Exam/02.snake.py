def is_valid(pos, size):
    return 0 <= pos[0] < size and 0 <= pos[1] < size


n = int(input())

matrix = []
food_count = 10
snake_pos = []
directions = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}
holes = []

for row in range(n):
    line = [x for x in input()]
    for col in range(n):
        if line[col] == "S":
            snake_pos = [row, col]
        if line[col] == "B":
            holes = [row, col]
    matrix.append(line)

while food_count:
    command = input()
    dir_changes = directions[command]
    new_pos = [snake_pos[0] + dir_changes[0], snake_pos[1] + dir_changes[1]]
    matrix[snake_pos[0]][snake_pos[1]] = "."

    if is_valid(new_pos, n):
        if matrix[new_pos[0]][new_pos[1]] == "-":
            matrix[new_pos[0]][new_pos[1]] = "."
            snake_pos = new_pos

        elif matrix[new_pos[0]][new_pos[1]] == "*":
            food_count -= 1
            matrix[new_pos[0]][new_pos[1]] = "."
            matrix[new_pos[0]][new_pos[1]] = "S"
            snake_pos = new_pos

        elif matrix[new_pos[0]][new_pos[1]] == "B":
            matrix[new_pos[0]][new_pos[1]] = "."
            snake_pos = [holes[0], holes[1]]

    else:
        print("Game over!")
        break

if food_count:
    print(f"Food eaten: {10 - food_count}")
else:
    print("You won! You fed the snake.")
    print("Food eaten: 10")

for row in matrix:
    print("".join(row))
