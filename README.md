'''

CST205-Team048-Proj3

Cooking App

Chino Abatol, Harsimrit Bhatia, Judith Ramirez
TA:Michael Sanchez
May 13, 2017


Repository: https://github.com/CSUMB-SP17-CST205/CST205-Team048-Proj3


Objective
For project 3 our objective is  to create an app that would allow a user to search for recipes by the ingredients they have available at the moment. The application will also provide a page where the user can search for instructional videos for cooking. In addition, if the user does not find a recipe they wish or  would just like to add a recipe, they will have the opportunity by accessing the “Add recipe” page that will be included in the app.

Our Goal
The tools used for the project consisted of the python language. The user interface will be created with kivy, a python library, to be able to provide the user with the best experience as possible. In addition,  the Yummly API is going to be used to provide the user with recipes depending on what the user chose. After the API is called, the results will show up on the page and the user will have the chance to pick the recipe they wish. For the page in which the user will be able to search for instructional videos, the youtube API will be used.

End Result
In the end, we were able to create the app using the python language and kivy. The page to add recipes allows the user to save the name, time needed, serving size, ingredients, and directions; this information is saved into a text file for later use. The page in which the user is able to seek instructional videos has a search box in which the user is able to enter an instruction they need; the entered text is taken by the Youtube API and then a youtube web page is opened with the instructional video. Lastly, the page in which the user searches for a recipe, has a search box for the user to enter their desired ingredients. When the search button is pressed, the API returns the image and the name of recipes consisting with what the user searched for. However, the buttons to choose the recipe were not able to be binded. Lastly, for the “Add recipe” page, the file in which the recipe was saved in was not able to be displayed in another page because of uploading problems with kivy.

'''
