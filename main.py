import json
print(json.dumps({"name": "John", "age": 30}))
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread