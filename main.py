  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import json
def convert_to_json(data):
        return json.dumps(data)