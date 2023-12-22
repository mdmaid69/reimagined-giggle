import tensorflow as tf
print(tf.__version__)
import json
def read_from_json(json_string):
        return json.loads(json_string)