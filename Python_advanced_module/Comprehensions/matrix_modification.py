n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    line = input().split()
    command = line[0]
    if command == "END":
        break
    row = int(line[1])
    col = int(line[2])
    value = int(line[3])

    if 0 <= row < n and 0 <= col < n:

        if command == "Add":
            matrix[row][col] += value

        elif command == "Subtract":
            matrix[row][col] -= value

        else:
            print("Invalid coordinates")
    else:
        print("Invalid coordinates")

[print(" ".join([str(x) for x in row])) for row in matrix]
