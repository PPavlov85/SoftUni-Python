from collections import deque


def more_than_three(**created_bombs):
    return created_bombs["Datura Bombs"] >= 3 and created_bombs["Cherry Bombs"] >= 3 and created_bombs[
        "Smoke Decoy Bombs"] >= 3


effects = deque([int(x) for x in input().split(",")])
casings = [int(x) for x in input().split(",")]

bombs = {
    40: "Datura Bombs",
    60: "Cherry Bombs",
    120: "Smoke Decoy Bombs"
}

created_bombs = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0
}

while effects and casings:
    if more_than_three(**created_bombs):
        break
    first_effect = effects.popleft()
    last_casing = casings.pop()
    result = first_effect + last_casing

    if result in bombs:
        bomb = bombs[result]
        created_bombs[bomb] += 1

    else:
        effects.appendleft(first_effect)
        casings.append(last_casing - 5)


if more_than_three(**created_bombs):
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if not effects:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join([str(x) for x in effects])}")

if not casings:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join([str(x) for x in casings])}")

for bomb, count in sorted(created_bombs.items()):
    print(f"{bomb}: {count}")
