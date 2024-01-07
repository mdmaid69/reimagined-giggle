def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array