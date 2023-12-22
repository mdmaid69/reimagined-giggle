import datetime
def get_today_date():
        return datetime.date.today()
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()