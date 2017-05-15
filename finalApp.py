##############################################################################
#  Cooking App                                                               #
#  by Chino Abatol, Judith Ramirez, Harsimrit Bhatia - Team 048              #
#  CST - 205 Multimedia Design and Programming                               #
#  5/15/2017                                                                 # 
#  Description: An app that allows the user to search for recipes            #
#               by the ingredients they have available at the moment,        #
#               a page to add new recipes of their own and a page            #
#               to search for instructional videos.                          #
##############################################################################

# Import API libraries needed for different functions

import json # To decode API response
import requests # To call API, both Yummly and Youtube
from kivy.uix.image import * # To use images in Kivy (UI API)
from kivy.app import App # Main import of the Kivy UI
from kivy.uix.image import AsyncImage # Import to use online images
from kivy.uix.popup import Popup # Be able to use Kivy popup screens
from kivy.uix.label import Label # To create Text labels in Kivy
from kivy.uix.button import Button # To create a interactible buttons on Kivy
from kivy.uix.boxlayout import BoxLayout # To be able to create Box layouts in the UI
from kivy.uix.floatlayout import FloatLayout # To be able to freely place widgets in the UI
from kivy.uix.textinput import TextInput # to be able to create a box for user input
from apiclient.discovery import build # Dependencies of the Youtube API
from oauth2client.tools import argparser # Denedencies of the Youtube API
import random # Random functions for python
import webbrowser # Functions to open a web browser
from kivy.uix.video import Video # Functions to be able to work with videos in Kivy

# Defining variables that will be used by the Youtube API

API_Key = "AIzaSyAUZFGhlri17-rWRYUfl0grRWfgNmBqrxM"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

VideoIds = [ ] # Array that will hold the information that the Youtube API will return

# General layout of the main screen of the APP


class HomePage(App):
    # Building widgets necessary for the main page, including buttons and labels.
    def build(self):
        layout = BoxLayout(padding=100, orientation='vertical')
        
        btn1 = Button(text = "Search for a Recipe")
        btn1.bind(on_press=self.clk1) # Binding the buttons to a specific action
        btn2 = Button(text = "Add a Recipe")
        btn2.bind(on_press=self.clk2) # Same as above
        btn3 = Button(text = "Learn to Cook")
        btn3.bind(on_press=self.clk3) # Same as above
        btn4 = Button(text = "More...")
        btn4.bind(on_press=self.clk4) # Same as above
        
        # Placing widgets onto the screen
        
        layout.add_widget(Label(text="Welcome to My Cooking App"))
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)

        return layout


    # Function to define what action each button bind should do
    def clk1(self, obj):
        app.stop()
        search.run()
    def clk2(self, obj):
        app.stop()
        add.run()
    def clk3(self, obj):
        app.stop()
        learn.run()
    def clk4(self, obj):
        app.stop()
        more.run()
        
# General Layout of the search recipe page where users can search for cooking recipes
# based on desired ingredients

class secondpage(FloatLayout):
    
    # Placing individual widgets on the UI by calling the functions
    
    def build(self):
        self.backbutton()
        self.searchbox()
        self.label()
        self.searchbutton()
        #self.justC()
    
    # Function to create the back button
    
    def backbutton(self):
        self.btn1 = Button(text = "Back", size_hint = (.05, .05), pos_hint = {'x':.008, 'y':.94})
        self.add_widget(self.btn1)
        self.btn1.bind(on_press = self.clk1)
        
    # Function to create the title of the page
    
    def label(self):
        self.label1 = Label(text = "Recipes at your Fingertips" ,
                           font_size = 30,
                           size_hint = (1,1.8),
                           pos_hint = {'x' :.01, 'y' :.01})
                         #color = [255,255,255,0])
        self.add_widget(self.label1)
        
    # Function to create am interactible search box   
    
    def searchbox(self) :
        self.search = TextInput(hint_text = "Tell us what you have ",
                          font_size = 15,
                          size_hint =(.7,.05),
                          pos_hint = {'x':.15, 'y':.8})
        self.add_widget(self.search)
        
    # Function to create the search button
    
    def searchbutton(self):
        self.btn2 = Button(text = "Search",size_hint = (.08,.05),pos_hint = {'x' :.87, 'y' :.8})
        self.add_widget(self.btn2)
        self.btn2.bind(on_press = self.clk2)

    # Defining the actions of the back button
    
    def clk1(self,obj):
        search.stop()
        app.run()
    
    # Defining the actions of the search function
    
    def clk2(self,obj):
        
        # Defining the parameters for the Yummly API
        
        my_key = '8b6f178c57d40dee7d88629b32e01c23'
        my_id = 'fabbe897'
        userAnswer = self.search.text
        userAnswer = userAnswer.rstrip()
        userAnswer = userAnswer.lstrip()
        counter = 1
        
        # Determining how many search variables were entered and changing
        # search parameters based on it.
        
        for i in range (0,len(userAnswer)):
            if (userAnswer[i] == " " and (userAnswer[i+1]).isalpha()):
                counter += 1

        if (counter == 1):
            recipe= userAnswer.split(' ')
            my_search= {
                'requirePictures': 'True',
                'allowedIngredient[]': [recipe]
                
            }
        elif(counter == 2):
            recipe, recipe1 = userAnswer.split(' ')
            my_search= {
                'requirePictures': 'True',
                'allowedIngredient[]': [recipe, recipe1]   
            }
        elif(counter == 3):
            recipe, recipe1, recipe2 = userAnswer.split(' ')
            my_search= {
                'requirePictures': 'True',
                'allowedIngredient[]': [recipe, recipe1, recipe2]   
            }
        elif(counter == 4):
            recipe, recipe1,recipe2,recipe3 = userAnswer.split(' ')
            my_search= {
                'requirePictures': 'True',
                'allowedIngredient[]': [recipe, recipe1,recipe2, recipe3]   
            }
        elif(counter == 5):
            recipe, recipe1, recipe2, recipe3, recipe4 = userAnswer.split(' ')
            my_search= {
                'requirePictures': 'True',
                'allowedIngredient[]': [recipe, recipe1, recipe2,recipe3, recipe4]   
            }

        # Saving API response into a workable variable
        
        r = requests.get('http://api.yummly.com/v1/api/recipes?_app_id=fabbe897&_app_key=8b6f178c57d40dee7d88629b32e01c23&',params = my_search)

        # Using json to decode the API response
        data = r.json()

        # Filtering JSON response into image, and recipe name and displaying
        # the image of the reicipe on the screen and the name on a button
        
        for i in range(0,10):
            
            if(i == 0):
                thing = str(data["matches"][i]["smallImageUrls"])
                ids5 = str(data["matches"][i]["id"])
                thing = thing[2:-2]
                img = AsyncImage(source=thing, pos_hint ={'center_x':.34, 'center_y':.7}, size_hint = (5,5))
                self.butt= Button(text = data["matches"][i]["recipeName"],
                                  font_size = 10.5,
                                  size_hint =(.29,.1),
                                  pos_hint = {'x':.19, 'y':.53})
                self.add_widget(self.butt)
                self.add_widget(img)
                #self.butt.bind(on_press = justC(ids5))
            elif(i == 1):
                thing1 = str(data["matches"][i]["smallImageUrls"])
                ids4 = str(data["matches"][i]["id"])
                thing1 = thing1[2:-2]
                img1 = AsyncImage(source=thing1, pos_hint ={'center_x':.63, 'center_y':.7}, size_hint = (5,5))
                self.butt1= Button(text = data["matches"][i]["recipeName"],
                                  font_size = 10.5,
                                  size_hint =(.29,.1),
                                  pos_hint = {'x':.5, 'y':.53})
                self.add_widget(self.butt1)
                self.add_widget(img1)
                #self.butt1.bind(on_press = justC(ids4))
            elif(i == 2):
                thing2 = str(data["matches"][i]["smallImageUrls"])
                ids3 = str(data["matches"][i]["id"])
                thing2 = thing2[2:-2]
                img2 = AsyncImage(source=thing2, pos_hint ={'center_x':.34, 'center_y':.43}, size_hint = (5,5))
                self.butt2= Button(text = data["matches"][i]["recipeName"],
                                  font_size = 10.5,
                                  size_hint =(.29,.1),
                                  pos_hint = {'x':.19, 'y':.27})
                self.add_widget(self.butt2)
                self.add_widget(img2)
                #self.butt2.bind(on_press = justC(ids3))
            elif(i == 3):
                thing3 = str(data["matches"][i]["smallImageUrls"])
                ids2 = str(data["matches"][i]["id"])
                thing3 = thing3[2:-2]
                img3 = AsyncImage(source=thing3, pos_hint ={'center_x':.63, 'center_y':.43}, size_hint = (5,5))
                self.butt3= Button(text = data["matches"][i]["recipeName"],
                                  font_size = 10.5,
                                  size_hint =(.29,.1),
                                  pos_hint = {'x':.5, 'y':.27})
                self.add_widget(self.butt3)
                self.add_widget(img3)
                #self.butt3.bind(on_press = justC(ids2))
            elif(i == 4):
                thing4 = str(data["matches"][i]["smallImageUrls"])
                ids1 = str(data["matches"][i]["id"])
                thing4 = thing4[2:-2]
                img4 = AsyncImage(source=thing4, pos_hint ={'center_x':.34, 'center_y':.19}, size_hint = (5,5))
                self.butt4= Button(text = data["matches"][i]["recipeName"],
                                  font_size = 10,
                                  size_hint =(.29,.1),
                                  pos_hint = {'x':.19, 'y':.01})
                self.add_widget(self.butt4)
                self.add_widget(img4)
                #self.butt4.bind(on_press = justC(ids1))
            elif(i == 5):
                thing5 = str(data["matches"][i]["smallImageUrls"])
                ids = str(data["matches"][i]["id"])
                thing5 = thing5[2:-2]
                img5 = AsyncImage(source=thing5, pos_hint ={'center_x':.63, 'center_y':.19}, size_hint = (5,5))
                self.butt5= Button(text = data["matches"][i]["recipeName"],
                                  font_size = 10,
                                  size_hint =(.29,.1),
                                  pos_hint = {'x':.5, 'y':.01})
                self.add_widget(self.butt5)
                self.add_widget(img5)
                #self.butt5.bind(on_press = justC(passId))

    # Function to get reicpe that user chooses from selection on the page
    
    def justC(passId):
        finalUrl = "http://api.yummly.com/v1/api/recipe/" + passId + "?_app_id=fabbe897&_app_key=8b6f178c57d40dee7d88629b32e01c23&"
        rec= requests.get(finalUrl)
        b = rec.json()
        url = b["attribution"]["html"]
        m = re.findall('<a href="?\'?([^"\'>]*)', url)
        m = m[2:-2]
        webbrowser.open(m)
                    
# Initializing the second page

class SecondpageApp(App):
    def build (self) :
        Layout = secondpage()
        Layout.build()
        return Layout

# Defining the page to be able to add a recipe

class SecondpageApp(App):
    def build (self) :
        Layout = secondpage()
        Layout.build()
        return Layout


# General layout of the add recipe page where user can input information about a recipe
# so that it will be saved for later use

class addRecipe(App):
    def build(self):
        
        # Defining the layout of the page
        f = FloatLayout()
        
        # Creating a box to input the name of the recipe
        
        self.name1 = TextInput(hint_text= "Name of Recipe",font_size = 10,multiline = False,size_hint =(.7,.05),pos_hint = {'x':.15, 'y':.8})
        
        # Creating a box to input the serving size
        
        self.servings = TextInput(hint_text= "Servings",
                             font_size = 10,
                             multiline = False,
                             size_hint = (.33,.05),
                             pos_hint = {'x':.52, 'y':.7})
        
        # Creating a box to input time required to cook
        
        self.time1 = TextInput(hint_text = "Time required",
                         font_size = 10,
                         multiline = False,
                         size_hint = (.33,.05),
                         pos_hint = {'x':.15, 'y':.7})
                         
        # Creating a box to input the ingredients of the recipe
        
        self.ingredients = TextInput(hint_text = "Ingredients",
                                font_size = 10,
                                size_hint = (.33,.49),
                                pos_hint = {'x':.15, 'y':.18})
        
        # Creating a box to input the cooking directions
        
        self.directions = TextInput(hint_text = "Directions",
                               font_size = 10,
                               size_hint = (.33,.49),
                               pos_hint = {'x':.52, 'y':.18})
                               
        # Save Button
        
        saveB = Button(text = "Save",
                       size_hint =(.5,.1),
                       pos_hint = {'x':.25,'y':.05})
        
        saveB.bind(on_press = self.clk) # Binding of the save button

        # Back Button
        
        cancelB = Button(text = "Back", size_hint = (.05, .05), pos_hint = {'x':.008, 'y':.94})
        
        cancelB.bind(on_press = self.clk1) # Binding of the back button
        

        # Adding the widgets on to the screen
        
        f.add_widget(Label(text = "Add a Recipe", font_size = 45,size_hint=(1,1.9)))
        f.add_widget(saveB)
        f.add_widget(cancelB)
        f.add_widget(self.name1)
        f.add_widget(self.servings)
        f.add_widget(self.time1)
        f.add_widget(self.ingredients)
        f.add_widget(self.directions)

        return f
    
    # Definition of what the save button will do when pressed
    
    def clk(self,obj):
        
        # Saved the information input by the user into separate variables
        
        fname = self.name1.text + ".txt"
        name = self.name1.text + "\n"
        servings = "Servings: " + self.servings.text + " "
        time = "Time: " + self.time1.text + "\n"
        ingredients = "\nIngredients:\n" + self.ingredients.text + "\n"
        directions = "\nDirections:\n" + self.directions.text
        
        # Writing the variables onto a text document in a specific format

        f =open(fname, "w+")
        f.write(name)
        f.write(servings)
        f.write(time)
        f.write(ingredients)
        f.write(directions)
        f.close()

        # Creating a pop up to inform the user that the recipe has been successfully saved
        
        content = Button(text = self.name1.text + "\nhas been saved successfully.",
                         halign = "center", valign = "middle")
        popup =  Popup (title = "Congratulations!",
                        content = content,
                        size_hint = (None, None),
                        size = (300, 300),
                        auto_dismiss = True)
        content.bind(on_press=popup.dismiss)
        popup.open()
        
    # definition of what the back button does
        
    def clk1(self,obj):
        add.stop()
        app.run()

# Code that defines how the Youtube API will search for requested video and return its video ID

def yt_search(term):
    
    # Defining information for Youtube
    
    youtube = build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION, developerKey = API_Key)
    
    # Formating the results of the search
    
    search_response = youtube.search().list(
        q =term,
        part="id,snippet",
        maxResults=1 # Increase this number to widen the search result (if 1, will return the result with highest relevance to search)
        ).execute()
        
    videos = []
 
    # Parsing the results so that it only returns the ID of the required video
    
    for search_results in search_response.get("items", [ ]):
        if search_results["id"]["kind"] == "youtube#video":
            videos.append("%s (%s)" % (search_results["snippet"]["title"],search_results["id"]["videoId"]))
            Id = search_results["id"]["videoId"]
            VideoIds.append(Id)

    Random_Id = (random.choice(VideoIds))
    return Random_Id
    
# General layout of the page to search for instructional videos

class LearnToCook(App):

    def build(self):
        
        # Defines how the widgets will be placed on the screen
        
        layout = FloatLayout()
        
        # Creating a box where user will input what video they want to watch

        self.words = TextInput(text = "How to: ",
                          multiline = False, size_hint= (.5, .05),
                          pos_hint = {'x':.17 , 'y':.85})
                          
        # Creating a search button
        
        btn = Button(text = "Search", size_hint = (.15, .05), pos_hint = {'x':.68 , 'y':.8491})
        btn.bind(on_press=self.clk) # Binding of the search button
        
        # Creating a back button
        
        btn1 = Button(text = "Back", size_hint = (.05, .05), pos_hint = {'x':.008, 'y':.94})
        btn1.bind(on_press=self.goBack) # Binding of the back button

        # Adding the widgets onto the screen
        
        layout.add_widget(Label(text="Learn To Cook", size_hint = (1, 1.9), font_size = 25))
        layout.add_widget(self.words)
        layout.add_widget(btn)
        layout.add_widget(btn1)

        return layout

    # Definition of actions of pressing the back button
    
    def goBack(self, obj):
        learn.stop()
        app.run()
        
    # Definition of actions of pressing the search button

    def clk(self, obj):
        # Formatting the keywords into a form which is usable by the Youtube API
        search = self.words.text
        search = search.rstrip()
        search = search.lstrip()        
        search = search.replace(" ", "+")
        url1 = yt_search(search)
        url2 = "https://www.youtube.com/watch?v="
        url = url2 + url1
        webbrowser.open(url) # Opens a webbrowser to the desired video
  
#   General layout of the More page that will show the recipes that the user has
#   previously saved.
        
class interestingContent(App):
    def build(self):
        
        # Defines the widgets on the screen
        
        f = FloatLayout()
        
        # Created the back button

        btn1 = Button(text = "Back", size_hint = (.05, .05), pos_hint = {'x':.008, 'y':.94})
        btn1.bind(on_press=self.goBack) # Binding of the back button
        
        # Created the label for the page
        
        f.add_widget(Label(text = "More",
                           font_size = 45,
                           size_hint=(1,1.9)))
                           
        # Places the widgets into the screen
        
        f.add_widget(btn1)
        
        
        return f

    # Defines the action of the back button
    
    def goBack(self, obj):
        more.stop()
        app.run()


# Initializes the entire app and starts the page

if __name__ == "__main__":
    
    app = HomePage()
    search = SecondpageApp()
    add = addRecipe()
    learn = LearnToCook()
    more = interestingContent()
    app.run()
