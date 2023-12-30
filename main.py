import array
def get_string_from_array(array):
        return array.tobytes()
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))