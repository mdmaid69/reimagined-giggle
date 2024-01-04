  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import datetime
def get_current_date():
        return datetime.date.today()