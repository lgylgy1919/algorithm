"""
clothes											                                        	return
[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]	5
[["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]		    	3
"""

clothes = [
    ["yellowhat", "headgear"],
    ["bluesunglasses", "eyewear"],
    ["green_turban", "headgear"],
]
hash_map = {}
for cloth in clothes:
    if cloth[1] in hash_map:
        hash_map[cloth[1]] += 1
    else:
        hash_map[cloth[1]] = 1

# {'eyewear': 1, 'headgear': 2}

answer = 1
for kind in hash_map.values():
    print(kind)
    answer *= kind + 1

print(answer - 1)
