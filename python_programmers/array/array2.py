numbers = [3, 30, 34, 5, 9]
# return = "9534330"

new_numbers = []

for num in numbers:
    num = str(num)
    new_numbers.append(num)

new_numbers = sorted(new_numbers, reverse=True)
print(new_numbers)

print("".join(new_numbers))
