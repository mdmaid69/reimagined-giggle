import array
def get_array_item_count(array, item):
        return array.count(item)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))