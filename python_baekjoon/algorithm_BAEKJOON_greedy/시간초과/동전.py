number, k = map(int,input().split(" "))
coin_list = []
for i in range(number):
    coin = int(input())
    coin_list.append(coin)

n = number-1
m = 0
while True:
    if coin_list[n] > k:
        n -= 1
    elif coin_list[n] <= k:
        k -= coin_list[n]
        m += 1
        if sum == k:
            break
        
print(m)