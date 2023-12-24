import tensorflow as tf
print(tf.__version__)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)