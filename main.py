numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)