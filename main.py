import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import collections
def create_user_list():
        return collections.UserList()