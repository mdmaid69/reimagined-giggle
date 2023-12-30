  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))