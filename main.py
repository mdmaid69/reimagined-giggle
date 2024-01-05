import datetime
def get_today_date():
        return datetime.date.today()
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)