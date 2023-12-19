import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)