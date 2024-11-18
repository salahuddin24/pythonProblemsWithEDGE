## Arbitrary Arguments
# => If you do not know how many arguments that will be passed into your function, and a* before the paramenter name in the function definition.
 # This way the function will receive a tuple of arguments, and can access the items accordinaly.

# def my_function(*a):
#     print("The youngest child is :", a[2])
# my_function("Alauddin", "Salah", "ahmed")
# output : The youngest child is : ('Alauddin', 'Salah', 'ahmed')

# # keyword Arguments
# # you can also send arguments with the key=value syntax
# def my_function(child2, child3, child1):
#     print("the youngest child is :", child3)#output : the youngest child is : bokkor
#
# my_function(child1="mokhles", child2="koddos", child3="bokkor")

# # Arbitrary Keyword arguments
# def my_function(**kid):
#     print("his last name is :", kid["lname"])#output : his last name is : uddin
# my_function(fName="Salah", lname="uddin")


# practice problem

# # 1.WAF to print the length of a list. ( list is the parameter)
# bangladeshi_cities =["Dhaka","Chattogram","Khulna","Rajshahi","Sylhet","Barishal","Comilla", "Rangpur" ]
# def provideLength(len):
#     return len
# length = len(bangladeshi_cities)
# result = provideLength(length)
# print(result)#######output : 8

# #2.WAF to print the elements of a list in a single line. ( list is the parameter)
# bangladeshi_cities =["Dhaka","Chattogram","Khulna","Rajshahi","Sylhet","Barishal","Comilla", "Rangpur" ]
# def printListItem(lists):
#     print(*lists)
# printListItem(bangladeshi_cities)

# # 3. print n! ( n factorial)
# def factorial(n):
#     # base case: stop recursion when n is o
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n -1)
# print(factorial(10))
# # output : 36288800

# # 4.WAF to convert USD to Taka.
# usd = int(input("enter amount :"))
# def convert(n):
#     return n * 126
# result = convert(usd)
# print(result)

# 5.WAF to determine if a number is odd or even
# number = int(input("enter a positive number :"))
# def determine(n):
#     if n <= 0 :
#         return "Provide a positive number"
#     elif n % 2 == 0:
#         return "this is even number."
#     else:
#         return "this is odd number."
#
# result = determine(number)
# print(result)

# 6.WAF to determine if a list has more odd or even values and print which is greater.
lists = [4, 53, 23, 52, 77, 66]
def count_odd_even(lists):
    countOdd = 0
    countEven = 0
    for list in lists:
        if list%2==0:
            countEven += 1
        else:
            countOdd += 1

    if countOdd > countEven:
        print("Odd numbers are greater.")
    elif countEven > countOdd:
        print("Even numbers are greater.")
    else:
        print("Odd and Even numbers are equal.")

count_odd_even(lists)
