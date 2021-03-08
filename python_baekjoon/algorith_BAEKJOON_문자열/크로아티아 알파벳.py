char = input()
arr = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
ans = 0
for i in range(8):
    if arr[i] in char:
        count = char.count(arr[i])
        ans += count
        char = char.replace(arr[i], " ")

ans += len(char.replace(" ", ""))
print(ans)
"""
a = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
alpha = input()

for t in a:
    alpha = alpha.replace(t, "*")

print(alpha)
print(len(alpha))
"""

