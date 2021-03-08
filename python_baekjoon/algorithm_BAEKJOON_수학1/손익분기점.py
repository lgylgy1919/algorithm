"""
fix, var, price = map(int, input().split())
income = price - var
a = 0
if var >= price:
    print("-1")
else:
    while True:
        if income * a <= fix:
            a += 1
        else:
            break
print(a)
"""
fix, var, price = map(int, input().split())
income = price - var
if var >= price:
    a = -1
else:
    a = int(fix / income) + 1
print(a)
