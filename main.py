import array
def get_array_item_count(array, item):
        return array.count(item)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)