#Searching for Businesses
import requests
url = 'https://api.yelp.com/v3/businesses/search'
api_key = "b6cho1459BzmcPi3ywlneHum-7H4mKpKSlmZ3j_Pa5fYdCFKIN7V1vLJ-M4oxxhjedw4BK5oDG_b6pyj8ihwwNurgy9T4NbX9gYdz_Sahon6DL_7FsLvUGYHMhWNYXYx"
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



