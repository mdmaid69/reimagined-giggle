import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import math
def calculate_error_function(x):
        return math.erf(x)