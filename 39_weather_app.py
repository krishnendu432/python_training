import requests
API_Key='e93779c344c5959a67aeb21d89d8bc2f'
lat=input("Enter the latitude of the area: ")
lon=input("Enter the longitude of the area: ")
url=f'http://api.openweathermap.org/geo/1.0/zip?zip=E14,GB&appid={API_Key}'
url1=f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_Key}'
response=requests.get(url)
response=requests.get(url1)
print(response)
