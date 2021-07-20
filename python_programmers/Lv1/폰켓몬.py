nums = [3, 3, 3, 2, 2, 2]
dic = {}
# set(nums)과정과 동일
for num in nums:
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1
# dic = {3:2, 1:1, 2:1}

sorted(dic, key=lambda x: dic[x])
if len(dic) <= len(nums) / 2:
    print(len(dic))
else:
    print(int(len(nums) / 2))
