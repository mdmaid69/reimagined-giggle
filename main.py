import array
def extend_array(array, iterable):
        array.extend(iterable)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])