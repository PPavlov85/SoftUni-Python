inventory = {name: {} for name in input().split(", ")}

while True:
    line = input().split("-")
    name = line[0]
    if name == "End":
        break
    item = line[1]
    cost = int(line[2])

    if item not in inventory[name]:
        inventory[name][item] = cost


[print(f"{name} -> Items: {len(inventory[name])}, Cost: {sum(inventory[name].values())}") for name in inventory]
