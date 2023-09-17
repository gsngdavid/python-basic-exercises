# Question:
# Write a program which can compute the factorial of a given numbers.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

def factorial(num):
    if (num == 0):
        return 1
    return num * factorial(num - 1)

print(factorial(8))