import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import json
print(json.dumps({"name": "John", "age": 30}))