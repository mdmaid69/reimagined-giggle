import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)