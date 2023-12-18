import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)