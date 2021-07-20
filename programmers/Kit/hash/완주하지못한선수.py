"""
participant						completion					return
["leo", "kiki", "eden"]					["eden", "kiki"]				"leo"
["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
["mislav", "stanko", "mislav", "ana"]			["stanko", "ana", "mislav"]			"mislav"
"""

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

dict = {}
for part in participant:
    if part in dict:
        dict[part] += 1
    else:
        dict[part] = 1

# {'mislav': 2, 'stanko': 1, 'ana': 1}
for com in completion:
    dict[com] -= 1

for key in dict:
    if dict[key] != 0:
        answer = key
