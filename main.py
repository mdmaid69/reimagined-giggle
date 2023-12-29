import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b