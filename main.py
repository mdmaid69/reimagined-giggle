import array
def clear_array(array):
        array *= 0
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b