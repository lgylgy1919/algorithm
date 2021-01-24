'''
pypy3로 틀렸다고 나옴
'''
n,l=map(int,input().split(" "))
t=0
while t==0 :
    a=0
    if l>100:
        print("-1")
        break
    elif n!=a:
        for i in range(1,l+1):
            a+=i
        while True:
            if a<n:
                a+=l
            elif a==n:
                x=int((n/l)+((1-l)/2))
                for i in range(l):
                    print(x+i,end=" ")
                t=1
                break
            elif a>n:
                break
        l+=1
'''
N과 L이 주어질 때, 
합이 N이면서, 
길이가 적어도 L인 
가장 짧은 연속된 음이 아닌 정수 리스트를 
구하는 프로그램을 작성하시오.
조건1) N <10억
조건2) 2<=L<=100
조건3)
만약 리스트의 길이가 100보다 작거나 같으면, 
    연속된 수를 첫째 줄에 공백으로 구분하여 출력한다. 
만약 길이가 100보다 크거나 그러한 수열이 없을 때는 
    -1을 출력한다.
--
예) 
18(N) 2(L)  /  5 6 7 

'''