command = input()
numbers = list(map(int, input().split()))

if command == "Odd":
    odd_nums = (sum(filter(lambda x: x % 2 != 0, numbers)))
    print(odd_nums * len(numbers))
else:
    even_nums = (sum(filter(lambda x: x % 2 == 0, numbers)))
    print(even_nums * len(numbers))
