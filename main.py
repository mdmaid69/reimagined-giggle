  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
def calculate_roi(gain, cost):
        return (gain - cost) / cost