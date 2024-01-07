n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
import array
def extend_array(array, iterable):
        array.extend(iterable)