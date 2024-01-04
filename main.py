import json
print(json.dumps({"name": "John", "age": 30}))
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)