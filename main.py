import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import json
def convert_to_json(data):
        return json.dumps(data)