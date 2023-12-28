import json
def read_from_json(json_string):
        return json.loads(json_string)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()