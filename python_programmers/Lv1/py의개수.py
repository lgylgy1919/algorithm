s = "Pyy"
'''
p = s.count("p") + s.count("P")
y = s.count("y") + s.count("Y")

if p == y or (p == 0 and y == 0):
    print(True)
else:
    print(False)
'''
s = s.lower()


def numPY(s):
    return s.count("y") == s.count("p")


print(numPY(s))
