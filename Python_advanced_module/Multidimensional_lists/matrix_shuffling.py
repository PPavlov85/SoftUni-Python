def is_valid(pos, row_count, col_count):
    return 0 <= pos[0] < row_count and 0 <= pos[1] < col_count


row_count, col_count = [int(x) for x in input().split()]

matrix = []

for _ in range(row_count):
    matrix.append([x for x in input().split()])

line = input().split()

while line[0] != "END":
    if len(line) == 5 and line[0] == "swap":
        first_pos = [int(line[1]), int(line[2])]
        second_pos = [int(line[3]), int(line[4])]

        if is_valid(first_pos, row_count, col_count) and is_valid(second_pos, row_count, col_count):
            matrix[first_pos[0]][first_pos[1]], matrix[second_pos[0]][second_pos[1]] =\
                matrix[second_pos[0]][second_pos[1]], matrix[first_pos[0]][first_pos[1]]

            for row in matrix:
                print(" ".join(row))

        else:
            print("Invalid input!")

    else:
        print("Invalid input!")

    line = input().split()
