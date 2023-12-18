  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)