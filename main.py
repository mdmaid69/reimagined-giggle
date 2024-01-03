  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()