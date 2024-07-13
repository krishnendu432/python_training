table=[90, 83, -56, -20, 70, 23, -88]
print("Please print the given table")
print(table)
table_pos=[]
table_neg=[]
#Now you have to devide the given list in two way
for i in table:
    if i<0 :
        continue # End of If statement, if the condition is true it will continue
    table_pos.append(i) #end of 1st for loop
print(f"The positive value of the table is : {table_pos}")
for i in table:
    if i>0 :
        continue
    table_neg.append(i)
print(f"The negative number of the the table is : {table_neg}")

