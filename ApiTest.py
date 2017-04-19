import requests
import json

my_key = '8b6f178c57d40dee7d88629b32e01c23'
my_id = 'fabbe897'

#my_search= {
#     "id":"course-Appetizers",
#     "description":"Appetizers",
#    "searchValue":"course^course-Appetizers"
#}

r = requests.get('http://api.yummly.com/v1/api/recipes?_app_id=fabbe897&_app_key=8b6f178c57d40dee7d88629b32e01c23&q=onion%20soup&requirePictures=true&allowedIngredient[]=garlic')

info = r.json()
print(info)
