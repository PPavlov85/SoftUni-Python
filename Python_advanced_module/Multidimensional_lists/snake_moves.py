from collections import deque

row_count, col_count = [int(x) for x in input().split()]
matrix = []
text = deque(input())

for row in range(row_count):
    matrix.append([])
    for col in range(col_count):
        matrix[row].append("")

for row in range(row_count):
    for col in range(col_count):
        current_col = col
        current_char = text.popleft()
        if row % 2 != 0:
            current_col = col_count - 1 - col
        matrix[row][current_col] = current_char
        text.append(current_char)

for row in matrix:
    print(''.join(row))
