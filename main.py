import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable