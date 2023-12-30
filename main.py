n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
import array
def get_array_item_count(array, item):
        return array.count(item)