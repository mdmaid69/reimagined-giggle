import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import json
def read_from_json(json_string):
        return json.loads(json_string)