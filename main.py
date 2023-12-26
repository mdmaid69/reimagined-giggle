import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])