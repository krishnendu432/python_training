# Show the data for the file as a graph format.
import pandas
# the matplotlib is a package to show the data as a graphical format
#import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
data=pandas.read_csv('user_details.csv')
# we have to find city wise user's total count
city_count=data.city.value_counts()
# To use these data work as a 'X' axis and 'Y' axis
plt.bar(city_count.index, city_count.values)
plt.plot(data.id, data.salary)
plt.bar(data.id, data.salary)
plt.xlabel('id')
plt.ylabel('salary')
