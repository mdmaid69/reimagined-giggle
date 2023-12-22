n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)