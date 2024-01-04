n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
import array
def iterate_over_array(array):
        for item in array:
        print(item)