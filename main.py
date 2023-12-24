  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import json
def read_from_json(json_string):
        return json.loads(json_string)