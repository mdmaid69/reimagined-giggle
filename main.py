  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import datetime
def get_current_datetime():
        return datetime.datetime.now()