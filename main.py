import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)