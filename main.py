import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)