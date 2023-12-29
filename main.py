n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
import array
def iterate_over_array(array):
        for item in array:
        print(item)