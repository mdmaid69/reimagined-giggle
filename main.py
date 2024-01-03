import array
def reverse_array(array):
        array.reverse()
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b