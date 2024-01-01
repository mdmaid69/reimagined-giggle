import json
print(json.dumps({"name": "John", "age": 30}))
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"