from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(current_date.strftime("%Y-%m-%d %H:%M:%S"))

display_current_datetime()

number_of_days = int(input("Enter the number of days to add to the current date: "))
def calculate_future_date(days):
    future_date = datetime.now() + timedelta(days=days)
    print(future_date.strftime("%Y-%m-%d"))

calculate_future_date(number_of_days)