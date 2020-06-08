n = int(input())
stack = []

for _ in range(n):
    quarry = [int(x) for x in input().split()]

    if quarry[0] == 1:
        stack.append(quarry[1])

    elif quarry[0] == 2:
        if stack:
            stack.pop()

    elif quarry[0] == 3:
        print(max(stack))

    elif quarry[0] == 4:
        print(min(stack))

print(", ".join([str(x) for x in stack[::-1]]))
