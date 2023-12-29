import json
def convert_to_json(data):
        return json.dumps(data)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()