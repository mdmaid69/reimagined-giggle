import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import tensorflow as tf
print(tf.__version__)