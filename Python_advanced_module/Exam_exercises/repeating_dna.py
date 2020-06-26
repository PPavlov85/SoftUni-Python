def get_repeating_DNA(text):
    result = []
    for idx in range(0, len(text) - 10):
        current = text[idx:idx+10]
        if current in text[idx+1:] and current not in result:
            result.append(current)
    return result


test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
result = get_repeating_DNA(test)
print(result)

test = "TTCCTTAAGGCCGACTTCCAAGGTTCGATC"
result = get_repeating_DNA(test)
print(result)

test = "AAAAAAAAAAA"
result = get_repeating_DNA(test)
print(result)
