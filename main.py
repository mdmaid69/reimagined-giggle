import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])