"""
phone_book				return
["119", "97674223", "1195524421"]	false
["123","456","789"]			true
["12","123","1235","567","88"]		false

"""
phone_book = ["12", "123", "1235", "567", "88"]
phone_book.sort()
# ['12', '123', '1235', '567', '88']

for n in range(len(phone_book) - 1):
    if phone_book[n + 1].startswith(phone_book[n]):
        print(False)
    else:
        print(True)
