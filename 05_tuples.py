# Tuples is same like as list but the difference between tuples and list:-
# Like string 'tuples' character also in-mutable
# the value of tuples you can't change like list. To define Tuples you have to use '()'.
days=("sun", "mon", "tues", "wed", "sun")
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
print("Wnat to know the index value of mon and wed")
print(days.index('wed'))
