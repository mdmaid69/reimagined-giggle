import tensorflow as tf
print(tf.__version__)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)