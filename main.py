import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)