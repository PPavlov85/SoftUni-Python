divisor = int(input())
max_num = int(input())

for n in range(max_num, 0, -1):
    if n % divisor == 0:
        print(n)
        break
