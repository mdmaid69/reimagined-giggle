import array
def get_array_item_count(array, item):
        return array.count(item)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)