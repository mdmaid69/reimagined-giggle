i = 0
while i < 5:
        print(i)
        i += 1
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}