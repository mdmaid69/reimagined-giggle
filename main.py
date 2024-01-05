import datetime
def get_days_until_next_year():
        next_year = datetime.date.today().year + 1
        next_new_year = datetime.date(next_year, 1, 1)
        return (next_new_year - datetime.date.today()).days
numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))