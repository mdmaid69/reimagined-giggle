import re
print(re.match("h.*o", "hello world"))
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}