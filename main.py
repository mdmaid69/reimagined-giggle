  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)