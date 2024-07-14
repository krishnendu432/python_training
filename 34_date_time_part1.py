# process 1:- How to get the current date time. Here import predefine builtin datetime()
import datetime,tim
cur_time=datetime.datetime.now()
print(cur_time)
# process 2:- How to get the current date time. Here import predefine builtin datetime()
from datetime import datetime
cur_time=datetime.now()
print(cur_time)
# formated date & time
formated_date=cur_time.strftime("%Y=%M=%D %H:%M")
print(formated_date)