  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)