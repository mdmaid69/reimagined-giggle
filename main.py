import array
def append_to_array(array, item):
        array.append(item)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])