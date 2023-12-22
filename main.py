import json
def read_from_json(json_string):
        return json.loads(json_string)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread