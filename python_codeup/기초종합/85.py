q,w,e,r=input().split(" ")
h = int(q)
b = int(w)
c = int(e)
s = int(r)
memory = h*b*c*s
divide = (8*(2**20))
mb_memory = memory/divide
print(round(mb_memory,1),"MB")