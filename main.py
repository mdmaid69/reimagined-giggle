import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True