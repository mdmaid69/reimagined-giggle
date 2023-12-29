numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)