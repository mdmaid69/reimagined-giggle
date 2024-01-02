import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import bisect
def binary_search(sorted_list, item):
        i = bisect.bisect_left(sorted_list, item)
        if i != len(sorted_list) and sorted_list[i] == item:
        return i
        else:
        return -1