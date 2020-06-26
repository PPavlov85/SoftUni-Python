def get_magic_triangle(num):
    triangle = [[1] * x for x in range(1, num + 1)]
    for row in range(2, num):
        for col in range(1,  row):
            triangle[row][col] = triangle[row - 1][col - 1] + triangle[row - 1][col]
    return triangle


for row in get_magic_triangle(5):
    print(row)
