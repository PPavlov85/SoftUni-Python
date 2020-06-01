len_of_sets = [int(x) for x in input().split()]
n = set()
m = set()

for _ in range(len_of_sets[0]):
    num = int(input())
    n.add(num)

for _ in range(len_of_sets[1]):
    num = int(input())
    m.add(num)

unique = n.intersection(m)

for x in unique:
    print(x)
