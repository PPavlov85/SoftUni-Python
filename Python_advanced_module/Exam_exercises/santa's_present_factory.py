from collections import deque

materials = deque([int(x) for x in input().split()])
magic_level = deque([int(x) for x in input().split()])

toys = {
    "Doll":	150,
    "Wooden train":	250,
    "Teddy bear": 300,
    "Bicycle": 400
}

create_toys = {
    "Doll": 0,
    "Wooden train":	0,
    "Teddy bear": 0,
    "Bicycle": 0}

while materials and magic_level:
    last_material = materials.pop()
    first_magic = magic_level.popleft()
    result = last_material * first_magic
    is_equal = False

    for toy, level in toys.items():
        if result == toys[toy]:
            create_toys[toy] += 1
            is_equal = True

    if result < 0:
        result = last_material + first_magic
        materials.append(result)

    elif not is_equal and result > 0:
        materials.append(last_material + 15)

    if last_material and magic_level == 0:
        magic_level.popleft()

    if last_material == 0:
        magic_level.appendleft(first_magic)
        continue

    if first_magic == 0:
        materials.append(last_material)
        continue

if create_toys["Doll"] and create_toys["Wooden train"] or create_toys["Teddy bear"] and create_toys["Bicycle"]:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in reversed(materials)])}")
if magic_level:
    print(f"Magic left: {', '.join([str(x) for x in magic_level])}")

if create_toys:
    for key, value in sorted(create_toys.items()):
        if value:
            print(f"{key}: {value}")
