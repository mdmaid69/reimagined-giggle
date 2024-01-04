import array
def pop_from_array(array, i=-1):
        return array.pop(i)
def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
                return False
        return True