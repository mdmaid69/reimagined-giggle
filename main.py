import array
def get_array_index(array, item):
        return array.index(item)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])