import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])