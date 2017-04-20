import requests
import json

my_key = '8b6f178c57d40dee7d88629b32e01c23'
my_id = 'fabbe897'

#raw_answer = raw_input()#self.words.txt.split(' ')
recipe = 'orange chicken'
#raw_answer.split(' ')
my_search= {
    'q' : recipe,
    'requirePictures': 'True',
    'allowedIngredient[]': recipe
    
}

#search = {
#'q' : recipe,
#'requirePictures': ,
#'allowedIngredient[]': ,
#'excludedIngredient[]' : ,
#'allowedAllergy[]' : ,
#'allowedDiet[]' : ,
#'allowedCuisine[]' : ,
#'excludedCuisine[]' : ,
#'allowedCourse[]' : ,
#'excludedCourse[]' : ,
#'maxTotalTimeInSeconds' : ,
#}

r = requests.get('http://api.yummly.com/v1/api/recipes?_app_id=fabbe897&_app_key=8b6f178c57d40dee7d88629b32e01c23&',params = my_search)


info = r.json()
print(info)
