def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import array
def iterate_over_array(array):
        for item in array:
        print(item)