list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)