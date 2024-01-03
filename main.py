import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import getpass
def get_username():
        return getpass.getuser()