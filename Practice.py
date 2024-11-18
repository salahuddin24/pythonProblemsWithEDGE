# ##### Write a Program to find the occurrence of ‘$’ in a String
# someString = "my name is salahuddin. my salary is 222$$$$."
# def count_dollar_signs(string):
#     return string.count("$")
# count =count_dollar_signs(someString)
# print(f"The character '$' occurs {count} times in the string.")

# ##### Print numbers from 100 to 1.
# for n in range(100, 0, -1):
#     print(n)

# #### Print the multiplication table of a number n.
# def print_multiplication_table(n):
#     for i in range(1, 11):
#         print(f"{n} x {i} = {n * i}")
#
# number = int(input("Enter a number: "))
# print_multiplication_table(number)


##### Search for a number x in this tuple using loop:
tuples = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
def findNumber(elements, n):
    return elements.count(n)
n = int(input("enter a number :"))
count = findNumber(tuples, n)
print(f"The number {n} occurs {count} times in the string.")






