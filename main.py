import array
def extend_array(array, iterable):
        array.extend(iterable)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))