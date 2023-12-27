import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))