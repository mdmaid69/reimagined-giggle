  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))