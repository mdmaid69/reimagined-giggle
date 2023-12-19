  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)