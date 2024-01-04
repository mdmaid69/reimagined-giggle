  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"