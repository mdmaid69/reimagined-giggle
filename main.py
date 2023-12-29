import array
def get_array_item_count(array, item):
        return array.count(item)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b