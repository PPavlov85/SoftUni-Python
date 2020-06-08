clothes = [int(x) for x in input().split()]
capacity_rack = int(input())
racks_count = 0
rack_sum = 0

while clothes:
    current_clothes = clothes.pop()
    if current_clothes + rack_sum <= capacity_rack:
        rack_sum += current_clothes

    else:
        racks_count += 1
        rack_sum = 0
        rack_sum += current_clothes

if rack_sum > 0:
    racks_count += 1

print(racks_count)
