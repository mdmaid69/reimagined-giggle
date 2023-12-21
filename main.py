import array
def convert_array_to_string(array):
        return array.tostring()
def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                return False
        return True