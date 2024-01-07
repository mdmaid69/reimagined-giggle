import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
                return False
        return True