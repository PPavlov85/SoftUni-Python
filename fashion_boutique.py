clothes = [int(x) for x in input().split()]
capacity_rack = int(input())
sum_clothes = []
sum_racks = 0

while clothes:
    clothes_pop = clothes.pop()
    if clothes_pop <= capacity_rack:
        sum_clothes.append(clothes_pop)
        capacity_rack -= clothes_pop

    else:
        sum_racks += 1
        capacity_rack =
        clothes.append(clothes_pop)


