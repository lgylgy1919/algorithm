n, l = map(int, input().split(" "))
lists = []
for i in range(n):
    a = input()
    lists.append(a)
x = []
for j in range(l):
    can = []
    for k in range(n):
        can.append(lists[k][j])
    a = can.count("T")
    b = can.count("A")
    c = can.count("G")
    d = can.count("C")
    if max(a, b, c, d) == a:
        x.append("T")
    elif max(a, b, c, d) == b:
        x.append("A")
    elif max(a, b, c, d) == c:
        x.append("G")
    else:
        x.append("C")

print(x)
"""
Hamming Distance란 길이가 같은 두 DNA가 있을 때, 
각 위치의 뉴클오티드 문자가 다른 것의 개수이다

우리가 할 일은 다음과 같다. 
n개의 길이가 같은 DNA가 주어져 있을 때(이 DNA를 a1a2a3a4...이라고 하자) 
Hamming Distance의 합이 가장 작은 DNA s를 구하는 것이다. 
즉, s와 a1의 Hamming Distance + s와 a2의 Hamming Distance + s와 a3의 
Hamming Distance ... 의 합이 최소가 된다는 의미이다.

입력
첫 줄에 DNA의 수 N과 문자열의 길이 M이 주어진다. 
그리고 둘째 줄부터 N+1번째 줄까지 N개의 DNA가 주어진다. 
N은 1,000보다 작거나 같은 자연수이고, 
M은 50보다 작거나 같은 자연수이다.

출력
첫째 줄에 Hamming Distance의 합이 가장 작은 DNA 를 출력하고, 
둘째 줄에는 그 Hamming Distance의 합을 출력하시오. 
그러한 DNA가 여러 개 있을 때에는 사전순으로 가장 앞서는 것을 출력한다.

5 8
TATGATAC
TAAGCTAC
AAAGATCC
TGAGATAC
TAAGATGT
--
TAAGATAC
7


4 10
ACGTACGTAC
CCGTACGTAG
GCGTACGTAT
TCGTACGTAA
--
ACGTACGTAA
6

6 10
ATGTTACCAT
AAGTTACGAT
AACAAAGCAA
AAGTTACCTT
AAGTTACCAA
TACTTACCAA
--
AAGTTACCAA
12
"""

