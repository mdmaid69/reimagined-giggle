  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
def greet(name):
        print(f"Hello, {name}!")