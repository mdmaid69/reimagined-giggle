  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
import re
def split_string(pattern, string):
        return re.split(pattern, string)