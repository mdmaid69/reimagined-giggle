import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])