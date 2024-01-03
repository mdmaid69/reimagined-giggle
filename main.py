n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array