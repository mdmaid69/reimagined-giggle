  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)