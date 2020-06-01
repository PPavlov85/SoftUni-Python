quantity = int(input())
days = int(input())

budget = 0
total_spirit = 0

for every_day in range(1, days + 1):
    if every_day % 11 == 0:
        quantity += 2
    if every_day % 2 == 0:
        total_spirit += 5
        budget += 2 * quantity
    if every_day % 3 == 0:
        total_spirit += 13
        budget += 8 * quantity
    if every_day % 5 == 0:
        total_spirit += 17
        budget += 15 * quantity
        if every_day % 3 == 0:
            total_spirit += 30
    if every_day % 10 == 0:
        total_spirit -= 20
        budget += 23
        if every_day == days:
            total_spirit -= 30

print(f"Total cost: {budget}\nTotal spirit: {total_spirit}")
