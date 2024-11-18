# A lambda functino is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
#syntax :
# lambda arguments:expression
from functools import reduce
from sys import exec_prefix
from tkinter.scrolledtext import example

# x = lambda a : a+10
# print(x(44))

# def my_function(n):
#     return lambda a: a**n
# myDoubler = my_function(2)
# print(myDoubler(10))

###### tarnary oparetor or 1 line conditional statement
# syntax: 1
#  expression1 if condition else expression2 # condition true hole expression1 execute korbe na hoy expression2
# syntax : 2 ( claver function)
# (falseExpression, trueExpression)[condition]

# find odd even using tarnary oparetor
# even = lambda a : "yes even" if a%2==0 else "no odd"
# print(even(34545))

# even = lambda a : ("odd number", "yes even number")[a%2==0]
# print(even(23324))

# salary = float(input("enter your salary :"))
# tax = salary*(0.1, 0.2)[salary>=50000]
# print(tax)

# num1 = int(input("enter the first number :"))
# num2 = int(input("enter the second number :"))
# max = lambda num1, num2: (f"second number is max: {num2}", f"first number is max :{num1}")[num1>num2]
# print(max(num1, num2))

# num1 = int(input("enter a number :"))
# find = lambda num : ("negative",("zero", "positive")[num>0])[num>=0]
# print(find(num1))

# higher order function in buildin function
# example: map, filter, reduce
###### map function
# syntax
# map(function, list/tuple/anyParameter)
lists = [1, 3, 4, 5, 7]
# var1 = list(map(lambda a : a**3, lists))
# print(var1)

# #### filter function
# even = list(filter(lambda a : a%2==0, lists))
# print(even)
#
# #### reduce function
# var = reduce(lambda a,b: a+b, lists)
# print(var)

lists = [2, 43, 23, 34, 53, 55]
lists2 = lists.pop()
print(lists2)

newlists = []
for ele in lists:
    newValue = ele**3
    newlists.append(newValue)
print(newlists)



