  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)
import json
def read_from_json(json_string):
        return json.loads(json_string)