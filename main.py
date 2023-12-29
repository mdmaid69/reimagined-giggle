  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)