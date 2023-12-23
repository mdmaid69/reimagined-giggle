  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)