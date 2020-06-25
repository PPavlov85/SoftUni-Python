def fix_calendar(numbers):
    for _ in range(len(numbers)):
        for i in range(len(numbers) - 1):
            n = numbers[i]
            if numbers[i + 1] > len(numbers):
                break
            next_number = numbers[i + 1]
            if n > next_number:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    return numbers


numbers = [3, 2, 1]
fixed = fix_calendar(numbers)
print(fixed)
