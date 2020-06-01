start_num = int(input())
final_num = int(input())

for i in range(start_num, final_num + 1):
    ascii_symbol = chr(i)
    print(ascii_symbol, end=" ")
