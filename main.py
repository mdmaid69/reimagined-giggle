import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)