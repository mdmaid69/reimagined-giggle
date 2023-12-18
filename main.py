def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
                return False
        return True
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array