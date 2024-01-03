  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])