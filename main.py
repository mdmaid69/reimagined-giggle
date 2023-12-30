import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)