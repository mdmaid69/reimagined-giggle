import array
def get_array_index(array, item):
        return array.index(item)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))