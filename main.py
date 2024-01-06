import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread