# the difference between list and set is :-
# In sets you can't use duplicate value, you can define duplicate value but when you will print the sets
# the duplicate value will not print
# It will print unordered way.
# Set's are un indexed.
# create a empty sets
my_sets=set() # don't use my_sets={}, it will create empty dictionary.
my_sets={"mon" , "tues" , "wed" , "mon"}
print("Display the data type of sets : \n")
print(my_sets, type(my_sets))
print("Display the list of sets: ")
print(my_sets)
print("Add a new value in the sets:")
my_sets.add("friday")
print("Display the sets after adding the value 'friday':")
print(my_sets)
print("Find out the length of the sets:-")
print(len(my_sets))
# How to convert a list to a set
print("After remove an item 'wed' from the set :- ")
my_sets.remove("wed")
print(my_sets)
# Define another set
day_month={"sun", "jan", "feb", "wed", "mon", "nov"}
print(f"Display the 2nd set: \n {day_month}")
print(" After performed the union operation between two set 'my_sets' and 'day_month':")
print(my_sets.union(day_month))
print(" After performed the intersection operation between two set 'my_sets' and 'day_month':")
print(my_sets.intersection(day_month))
print(" After performed the difference operation from 'my_sets' to 'day_month':")
print(my_sets.difference(day_month))
print("Find that the {'jan','nov','feb'} is the subset of 'day_month' or not:")
print({"jan","nov","feb"}.issubset(day_month))
print(" After performed the superset operation we will check that is the 'my_sets' is the super set of 'day_month' or not:")
print(my_sets.issuperset(day_month))
month=["jan", "march", "feb", "jan", "april", "nov", "april"]
print("Print the month's list")
print(month)
set_month=set(month)
print("Display the value of set after converted from list:")
print(set_month)