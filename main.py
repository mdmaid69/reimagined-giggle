def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import array
def iterate_over_array(array):
        for item in array:
        print(item)