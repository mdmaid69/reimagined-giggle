import array
def get_array_item(array, i):
        return array[i]
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b