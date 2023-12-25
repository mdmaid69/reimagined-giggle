import array
def get_array_item_count(array, item):
        return array.count(item)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])