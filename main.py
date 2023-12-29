import array
def set_array_item(array, i, item):
        array[i] = item
def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                return False
        return True