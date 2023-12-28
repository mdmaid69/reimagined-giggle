import getpass
def get_username():
        return getpass.getuser()
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)