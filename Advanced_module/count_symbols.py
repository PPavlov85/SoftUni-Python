text = input()

ch_dict = {}

for ch in text:
    if ch not in ch_dict:
        ch_dict[ch] = 0
    ch_dict[ch] += 1

for ch, count in sorted(ch_dict.items()):
    print(f"{ch}: {count} time/s")
