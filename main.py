  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import re
print(re.match("h.*o", "hello world"))