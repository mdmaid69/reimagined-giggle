import array
def get_bytes_from_array(array):
        return array.tobytes()
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))