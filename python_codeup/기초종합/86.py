w,h,b= map(int,input().split(" "))
bit_memory = w*h*b
mb = 8*(2**20)
mb_memory = bit_memory/mb
print('%.2f' %mb_memory,"MB")