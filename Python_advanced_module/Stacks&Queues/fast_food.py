from collections import deque

day_quantity = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

is_complete = True

while orders:
    order = orders.popleft()
    if order <= day_quantity:
        day_quantity -= order

    else:
        is_complete = False
        orders.appendleft(order)
        break

if is_complete:
    print("Orders complete")
else:
    print(f"Orders left: {''.join([str(x) for x in orders])}")
