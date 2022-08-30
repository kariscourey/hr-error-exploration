# def fifty_by(number):

#     try:
#         return 50 / number
#     except ZeroDivisionError:
#         print("Error: Invalid argument")

#         # because there's no return statement in the except block, the default value of None is returned and printed.


# print(fifty_by(5))
# print(fifty_by(15))
# print(fifty_by(0))  # ZeroDivisionError special built-in Python class
# print(fifty_by(1))


# def fifty_by(number):
#     return 50 / number


# try:
#     print(fifty_by(5))
#     print(fifty_by(15))
#     print(fifty_by(0))
#     print(fifty_by(1))
# except ZeroDivisionError:
#     print("Error: Invalid argument")


# import math

# def fifty_by(number):
#     try:
#         return 50 / number
#     except ZeroDivisionError:
#         print("Error: Invalid argument")
#         return math.inf  # returns infinity
#     except TypeError:
#         print("Error: Why did you give me that?")
#         return math.nan  # not a number

# print(fifty_by(5))
# print(fifty_by(15))
# print(fifty_by(0))
# print(fifty_by(1))
# print(fifty_by("A"))


import math

class OneDivisionError(RuntimeError):
    pass

def fifty_by(number):
    if number == 1:
        raise OneDivisionError
    try:
        return 50 / number
    except ZeroDivisionError:
        print("Error: Invalid argument")
        return math.inf
    except TypeError:
        print("Error: Why did you give me that?")
        return math.nan
    # except OneDivisionError:
    #     print("Error: Too easy!")
    #     return


print(fifty_by(5))
print(fifty_by(15))
print(fifty_by(0))
print(fifty_by(1))
print(fifty_by("A"))
