import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable