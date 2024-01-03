import array
def check_if_array_contains_item(array, item):
        return item in array
def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
                return False
        return True