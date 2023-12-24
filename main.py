import tensorflow as tf
print(tf.__version__)
import json
def convert_to_json(data):
        return json.dumps(data)