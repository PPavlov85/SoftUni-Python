budget = float(input())
floor_price_kg = float(input())

pack_of_eggs_price = floor_price_kg * 0.75
milk_price_l = floor_price_kg * 1.25
milk_price_250 = milk_price_l / 4

total_price_cozunak = pack_of_eggs_price + floor_price_kg + milk_price_250

cozunak_count = 0
color_eggs_count = 0

while total_price_cozunak <= budget:
    cozunak_count += 1
    color_eggs_count += 3

    if cozunak_count % 3 == 0:
        color_eggs_count -= cozunak_count - 2

    budget -= total_price_cozunak

print(f"You made {cozunak_count} cozonacs! Now you have {color_eggs_count} eggs and {budget:.2f}BGN left.")
