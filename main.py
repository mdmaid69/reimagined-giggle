  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)