import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))