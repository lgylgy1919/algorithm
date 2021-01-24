c = int(input())
for i in range(c):
    n, char = input().split(" ")
    for j in range(len(char)):
        for _ in range(int(n)):
            print(char[j], end="")
    print()

