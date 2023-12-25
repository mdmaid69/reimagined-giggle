import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
                return False
        return True