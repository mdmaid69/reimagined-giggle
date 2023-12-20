import re
print(re.match("h.*o", "hello world"))
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)