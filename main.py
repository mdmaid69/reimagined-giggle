import array
def get_array_as_bool(array):
        return bool(array)
def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                return False
        return True