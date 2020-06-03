words = input().split(", ")

result = [f"{words[i]} -> {len(words[i])}" for i in range(len(words))]

print(", ".join(result))
