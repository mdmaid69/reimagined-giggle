import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)