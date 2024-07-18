import requests
API_Key='e93779c344c5959a67aeb21d89d8bc2f'
city_name=input("Enter your city name : ")
url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&apiid={API_Key}'
response=requests.get(url)
print(response)
