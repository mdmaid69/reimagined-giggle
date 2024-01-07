import array
def get_array_buffer_info(array):
        return array.buffer_info()
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))