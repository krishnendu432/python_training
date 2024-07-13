# created a list of members
team=['Rahul', 'Mukesh', 'Gill', 'Jaiswal', 'Kuldeep', 'Surya', 'Shami', 'Siraj']
# How to print the full list
print(team)
#If we require to print particular value then how you will do
print(f'The wicket keeper of the team is: {team[0]}')
# How to added a value in the given list?
print('After append the new value, the list is like')
team.append('Hardik')
print(team)
# How to sort the listed value
team.sort()
print("The team as in sorted way:")
print(team)
# How to do reverse sorting
team.reverse()
print("The team as in reverse way:")
print(team)
#How to remove value from the list
team.remove('Shami')
print ('After remove Shami the remaining team members are')
print(team)
#How to modify the attributes of the list
#team[7]='Surya Kumar'
#print("After modify the name the new team list is:")
#print(team)
# How to insert a value at a given position
team.insert(6,"Shami")
print("After insert Shami in the specific position the team is :")
print(team)
# Length of the list
length=team.__len__()
print("The length of the list is:")
print(length)
#How to do POP. simple pop operation will remove value from the end of the list.
remove_value=team.pop()
#After using pop operation check the list
print(team)
# We can also check which value has been pop
print(f"The POP value is: {remove_value}")
#How to POP a specific value
remove_Specific_value=team.pop(5)
# We can also check which value has been pop
print(f"The Specific value is: {remove_Specific_value}")
#After using specific pop operation check the list
print(team)
#How to use slice operation in list
print("Slice the list between 4th value to 5th value")
print(team[3:5])
#If is it required to slice from end
print("Slice the last two value from end")
print(team[-2:])

