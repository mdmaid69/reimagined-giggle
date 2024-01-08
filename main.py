from collections import Counter
print(Counter("hello world"))
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}