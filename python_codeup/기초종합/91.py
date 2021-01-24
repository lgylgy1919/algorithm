a,m,d,n = map(int,input().split(" "))
factor = a
for i in range(1,n):
   a= a*m + d
print(a)