alpha = input()
num = int(alpha, 16)
hex_num =hex(num)
a = 1
while(a < 16):
    hex_result = hex(a*num)
    print(f"{(hex_num).replace('0x','').upper()}*{(hex(a)).replace('0x','').upper()}={(hex_result).replace('0x','').upper()}")
    a += 1