n = int(input())
unique = set()

for _ in range(n):
    compounds = [x for x in input().split()]
    for element in compounds:
        unique.add(element)

[print(x) for x in unique]
