  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))