#Searching for Businesses
import requests
url = 'https://api.yelp.com/v3/businesses/search'
headers = {
    "Authorization": "Bearer " + api_key
}
parmas = {
    "term":"Barber",
    "location": "NYC"}
response = requests.get(url, headers = headers, params = parmas)
businesses = response.json()["businesses"]
names = [business["name"] for business in businesses if business["rating"] > 4.5]
print(names)



