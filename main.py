  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()