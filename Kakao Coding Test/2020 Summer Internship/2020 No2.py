import re


answer = 0
operators_set = [
    ["+", "-", "*"],
    ["+", "*", "-"],
    ["-", "+", "*"],
    ["-", "*", "+"],
    ["*", "+", "-"],
    ["*", "-", "+"],
]
    


expression = "100-200*300-500+20"
new_expression = expression.replace("-", ",").replace("+", ",").replace("*", ",")
numbers = re.split(",", new_expression)

operator_order = []
for t in expression:
    if t in {"+", "-", "*"}:
        operator_order.append(t)
"""
numbers = [100,200,300,500,20]
operators = ['-', '*', '-', '+']
"""

for operators in operators_set:
    for operator in operators:
        

