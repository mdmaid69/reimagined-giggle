  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()