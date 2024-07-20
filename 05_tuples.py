# Tuples is same like as list but the difference between tuples and list:-
# Like string 'tuples' character also in-mutable
# the value of tuples you can't change like list. To define Tuples you have to use '()'.
days=("sun", "mon", "tues", "wed", "sun", "mon")
print("Please check the data type of the list:")
print(type(days))
print("Print the given days list")
print(days)
print("Please find the first day of the list")
print(days[0])
# Now we are trying to change the value of the tuples, then we will get error message.
# days[0]="Sunday"
print("We want to know how many time mon has came in our given tuples:")
print(days.count('mon'))
print("How to know the index value of mon and wed")
# 'mon' has came two times in the tuples but for indexing if it will return 1st value it will not check next index.
print(days.index('wed'))
print(days.index('mon'))
print(f"Find the length of the tuples: {len(days)}")
# Define another tuples
months=("jan", "dec", "mar", "nov")
print("Addition of two tuples")
days_months=days+months
print(days_months)
print("Slicing of the tuples as per the months only:")
# If you use only starting character of the tuples and not mentioned then by default it will take end of the tuples
only_months=days_months[6:]
only_months1=days_months[6:10]
print(only_months)
print(only_months1)
