males = [int(x) for x in input().split()]
females = [int(x) for x in input().split()]

matches_count = 0

while males and females:
    current_male = males[-1]
    current_female = females[0]

    if current_male <= 0:
        males.pop()
    elif current_female <= 0:
        females.pop(0)

    elif current_male == current_female:
        matches_count += 1
        males.pop()
        females.pop(0)

    elif current_male % 25 == 0:
        males.pop(-1)
        if males:
            males.pop(-1)

    elif current_female % 25 == 0:
        females.pop(0)
        if females:
            females.pop(0)

    else:
        females.pop(0)
        males[-1] -= 2

print(f"Matches: {matches_count}")

if males:
    print(f"Males left: {', '.join(reversed([str(x) for x in males]))}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join([str(x) for x in females])}")
else:
    print("Females left: none")
