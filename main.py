import re
print(re.match("h.*o", "hello world"))
import array
def get_array_as_frozenset(array):
        return frozenset(array)