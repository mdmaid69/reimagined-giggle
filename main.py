import datetime
def get_today_date():
        return datetime.date.today()
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)