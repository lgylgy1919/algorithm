n = int(input())
p = 1
while True:
    if p<1000000:
        q=""    
        q_list = list(str(p))
        q_list.reverse()
        for i in q_list:
            q+=i
        if (p - (int(q))) == n:
            print(p)
            break
        else:
            p+=1
    else:
        print(-1)
        break

'''
문제
어떤 수를 뒤집는다는 것은 오른쪽부터 다시 쓰는것이다. 
예를 들어, 1234를 뒤집으면 4321이 되고, 
100을 뒤집으면 1이 된다. (앞에 0은 무시)

어떤 수 D가 주어질 때, 
x – (x를 뒤집은 수)가 D가 되는 
가장 작은 음이 아닌 정수 x를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 D가 주어진다. D는 1,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 가장 작은 x를 출력한다. 
만약 그러한 x가 없다면 -1을 출력한다.
'''