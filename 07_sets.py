# the difference between list and set is :-
# In sets you can't use duplicate value, you can define duplicate value but when you will print the sets
# the duplicate value will not print
# It will print unordered way.
my_sets ={"mon" , "tues" , "wed" , "mon"}
print("Display the list of sets: ")
print(my_sets)
print("Add a new value in the sets:")
my_sets.add("friday")
print("Display the sets after adding the value:")
print(my_sets)
# How to convert a list to a set
month=["jan", "march", "feb", "jan", "april", "nov", "april"]
print("Print the month list")
print(month)
set_month=set(month)
print("Display the value of set:")
print(set_month)