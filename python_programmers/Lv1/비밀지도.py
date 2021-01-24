n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
arr1_list = []
arr2_list = []
answer = []

for i in arr1:
    arr = [0]*n
    a = format(i, 'b')
    for j in range(len(a)):
        arr[n-j-1] = a[len(a)-j-1]
    arr1_list.append(arr)

for i in arr2:
    arr = [0]*n
    a = format(i, 'b')
    for j in range(len(a)):
        arr[n-j-1] = a[len(a)-j-1]
    arr2_list.append(arr)


for i in range(n):
    ans = []
    for j in range(n):
        if arr1_list[i][j] == '1' or arr2_list[i][j] == '1':
            ans.append("#")
        else:
            ans.append(" ")
    answer.append(''.join(ans))


print(answer)

'''
import re

def solution(n, arr1, arr2):
    answer = ["#"]*n
    for i in range(0, n):
        answer[i] = str(bin(arr1[i]|arr2[i]))[2:]
        answer[i] = re.sub('1', '#', '0'*(n-len(answer[i]))+answer[i])
        answer[i] = re.sub('0', ' ', answer[i])
    return answer
'''
'''
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
'''
