import array
def check_if_array_contains_item(array, item):
        return item in array
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b