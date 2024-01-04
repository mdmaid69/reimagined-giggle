import array
def append_to_array(array, item):
        array.append(item)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b