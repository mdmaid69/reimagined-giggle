import tensorflow as tf
print(tf.__version__)
import math
def calculate_permutations(n, k):
        return math.perm(n, k)