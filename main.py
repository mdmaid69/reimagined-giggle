  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))