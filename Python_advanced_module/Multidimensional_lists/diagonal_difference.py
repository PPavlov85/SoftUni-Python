n = int(input())

matrix = []
primary_sum = 0
secondary_sum = 0

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

for row in range(n):
    primary_sum += matrix[row][row]
    col = n - 1 - row
    secondary_sum += matrix[row][col]

difference = abs(primary_sum - secondary_sum)
print(difference)
