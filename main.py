n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)