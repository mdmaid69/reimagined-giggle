import datetime
def get_current_date():
        return datetime.date.today()
import json
def convert_to_json(data):
        return json.dumps(data)