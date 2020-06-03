bunker = {category: {} for category in input().split(", ")}
n = int(input())

for _ in range(n):
    line = input().split(" - ")
    category = line[0]
    item = line[1]
    quantity = int(line[2].split(";")[0].split(":")[1])
    quality = int(line[2].split(";")[1].split(":")[1])

    bunker[category][item] = quantity, quality

count_items = sum([sum([x[0] for x in list(bunker[category].values())]) for category in bunker])
print(f"Count of items: {count_items}")

average_quality = sum([sum([x[1] for x in list(bunker[category].values())]) for category in bunker]) / len(bunker)
print(f"Average quality: {average_quality:.2f}")

[print(f"{category} -> {', '.join(bunker[category].keys())}") for category in bunker]
