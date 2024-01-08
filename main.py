  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread