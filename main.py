n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)