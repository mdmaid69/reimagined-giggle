import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import json
def convert_to_json(data):
        return json.dumps(data)