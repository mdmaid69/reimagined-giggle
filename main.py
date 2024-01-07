import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))