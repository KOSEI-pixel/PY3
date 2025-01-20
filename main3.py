
import math

try:
    num = float(input("Enter a number to find the square root: "))
    result = math.sqrt(num)
    print("The square root of {} is approximately {}".format(num, result))
except ValueError as e:
    print(e)