import array
def get_list_from_array(array):
        return array.tolist()
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])