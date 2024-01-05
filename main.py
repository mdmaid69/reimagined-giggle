import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))