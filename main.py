  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()