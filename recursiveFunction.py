# A recursive function is a function that calls itself during its execution. This technique is useful for solving problems that can be divided into smaller sub-Problems of the same type.

# # print n to 1 backwards
# def show(n):
#     if n==0:
#         return
#     print(n)
#     show(n-1)
#
# show(5)
# #output : 5 4 3 2 1


# # print n! ( n factorial)
# def factorial(n):
#     # base case: stop recursion when n is o
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n -1)
# print(factorial(10))
# # output : 36288800

### Write a recursive function to calculate the sum of first n natural numbers.
# def sumNumbers(n):
#     if n ==1 :
#         return 1
#     return n + sumNumbers(n - 1)
# print(sumNumbers(10))
# # output : 55

# ## write a recursive function to print all elements in a list. (use list and index as parameter)
# fruits = ["Apple", "Orange", "Cherry", "Banana", "Guava", "Pineapple", "Mango"]
# def findElement(lists, ind = 0):
#     if ind == len(lists):
#         return
#     print(lists[ind])
#     findElement(lists, ind + 1)
# findElement(fruits)







