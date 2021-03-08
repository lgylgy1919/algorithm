s = "a1234"
if len(s) == 4 or len(s) == 6:
    try:
        s = int(s)
        print(True)
    except:
        print(False)
else:
    print(False)


def checknum(s):
    return s.isdigit() and len(s) in (4, 6)


'''
isdigit : 문자열이 숫자인지 check
isalpha : 문자열이 문자인지 check 
'''
