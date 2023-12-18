import json
print(json.dumps({"name": "John", "age": 30}))
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())