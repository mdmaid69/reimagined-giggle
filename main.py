import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True