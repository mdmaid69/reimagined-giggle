import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)