  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])