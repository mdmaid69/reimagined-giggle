def find_common_elements(list1, list2):
        return set(list1) & set(list2)
import json
def read_from_json(json_string):
        return json.loads(json_string)