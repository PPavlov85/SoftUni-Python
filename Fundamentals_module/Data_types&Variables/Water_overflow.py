lines_count = int(input())

current_liters = 0

for i in range(lines_count):
    liters = int(input())
    current_liters += liters

    if current_liters > 255:
        current_liters -= liters
        print("Insufficient capacity!")

print(current_liters)
