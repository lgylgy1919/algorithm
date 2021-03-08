clothes = [["yellow_hat", "headgear"], [
    "blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

'''
clothes = [["crow_mask","face"],["blue_sunglasses","face"],["smoky_makeup","face"]]
'''


mat = {}
a = 0
clothes = sorted(clothes, key=lambda x: x[1])
#clothes = [['blue_sunglasses', 'eyewear'], ['yellow_hat', 'headgear'], ['green_turban', 'headgear']]
for i in clothes:
    if i[1] in mat.keys():
        a += 1
        mat[i[1]] = a
    else:
        a = 1
        mat[i[1]] = a

a = 1
for i in mat:
    a *= (mat[i]+1)

print(a-1)
