result = [ch for l in input().split("|")[::-1] for ch in l.split(" ") if ch != ""]

print(' '.join(result))
