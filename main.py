list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a