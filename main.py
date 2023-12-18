  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a