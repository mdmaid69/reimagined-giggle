import datetime
def get_today_date():
        return datetime.date.today()
import json
def read_from_json(json_string):
        return json.loads(json_string)