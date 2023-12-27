import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])