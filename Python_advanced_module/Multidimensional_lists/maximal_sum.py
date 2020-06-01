row_count, col_count = [int(x) for x in input().split()]

matrix = []

for _ in range(row_count):
    line = [int(x) for x in input().split()]
    matrix.append(line)

best_sum = -999999999
best_matrix = []

for row in range(row_count - 2):
    for col in range(col_count - 2):
        sub_matrix = []
        current_sum = 0
        row_counter = 0
        for r in range(row, row + 3):
            sub_matrix.append([])
            for c in range(col, col + 3):
                sub_matrix[row_counter].append(matrix[r][c])
                current_sum += matrix[r][c]
            row_counter += 1

        if current_sum > best_sum:
            best_sum = current_sum
            best_matrix = sub_matrix

print(f"Sum = {best_sum}")
for row in best_matrix:
    print(' '.join([str(x) for x in row]))
