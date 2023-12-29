list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)