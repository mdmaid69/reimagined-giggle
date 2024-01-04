n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
import array
def iterate_over_array(array):
        for item in array:
        print(item)