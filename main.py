  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))