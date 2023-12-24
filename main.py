  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a