import array
def remove_from_array(array, item):
        array.remove(item)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])