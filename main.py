numbers = [1, 2, 3, 4, 5]
print("Sum:", sum(numbers))
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)