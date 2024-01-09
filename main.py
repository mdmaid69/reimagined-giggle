import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)