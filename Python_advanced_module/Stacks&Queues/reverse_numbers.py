numbers_list = input().split()
stack = []

while numbers_list:
    stack.append(numbers_list.pop())

print(" ".join(stack))
