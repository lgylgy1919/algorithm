arr = [10]

arr.remove(min(arr))
if len(arr) == 0:
    print([-1])
else:
    print(arr)

'''
def rm_small(mylist):
    print([i for i in mylist if i > min(mylist)] or [-1])
'''
