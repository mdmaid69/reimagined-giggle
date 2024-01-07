  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
def calculate_average(numbers):
        return sum(numbers) / len(numbers)