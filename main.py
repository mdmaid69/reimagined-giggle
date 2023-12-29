import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)