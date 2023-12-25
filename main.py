def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                return False
        return True
import array
def iterate_over_array(array):
        for item in array:
        print(item)