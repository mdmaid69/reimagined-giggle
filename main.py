  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread