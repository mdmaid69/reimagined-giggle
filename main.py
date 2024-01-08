  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import time
def get_time_since_epoch():
        return time.time()