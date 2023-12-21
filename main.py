numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}