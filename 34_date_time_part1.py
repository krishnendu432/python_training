# process 1:- How to get the current date time. Here import predefine builtin datetime()
import datetime
cur_time=datetime.datetime.now()
print(cur_time)
# process 2:- How to get the current date time. Here import predefine builtin datetime()
from datetime import datetime,timedelta
cur_time=datetime.now()
print(cur_time)
# formated date & time
formated_date=cur_time.strftime("%Y=%M=%D %H:%M")
print(formated_date)
# How to get the future date, here we will check the next 10 days date from current date
future_date=cur_time+timedelta(days=10)
print("From now after 10 days the date is: ")
print(future_date)
# How to get the future date, here we will check the previous 10 days date from current date
previous_date_time=cur_time-timedelta(days=10)
print("From now previous 10 days the date is: ")
print(previous_date_time)
# How to get the current date,month,year individually
print("Now the current year is:-")
print(cur_time.year)
print("Now the current month is:-")
print(cur_time.month)
print("Now the current time is:-")
print(cur_time.time())
print("Today is:-")
print(cur_time.today())
print("Now the Ctime is:-")
print(cur_time.ctime())




