import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)