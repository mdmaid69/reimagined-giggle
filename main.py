import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True