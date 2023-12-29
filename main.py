def calculate_distance(x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable