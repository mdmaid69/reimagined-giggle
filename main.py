import array
def insert_into_array(array, i, item):
        array.insert(i, item)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])