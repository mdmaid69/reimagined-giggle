import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))