import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)