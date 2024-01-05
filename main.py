n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)