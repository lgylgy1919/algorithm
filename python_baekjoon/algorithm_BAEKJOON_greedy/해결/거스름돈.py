'''
지불한 돈 : 1000
지불할 돈 : x
거스름돈 : 1000-x
잔돈 종류 : 500/100/50/10/5/1
'''
price = int(input())
change = 1000-price
changes = [1, 5, 10, 50, 100, 500]
kinds_n = 6
n = 0
while True:
    if (changes[kinds_n - 1]) > change:
        kinds_n -= 1
    else:
        change -= changes[kinds_n -1]
        n += 1
        if change == 0:
            break

print(n)
