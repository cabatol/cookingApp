import json
import requests
from kivy.uix.image import *
from kivy.app import App
from kivy.uix.image import AsyncImage
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput



class HomePage(App):
        
    def build(self):
        layout = BoxLayout(padding=100, orientation='vertical')
        
        btn1 = Button(text = "Search for a Recipe")
        btn1.bind(on_press=self.clk1)
        btn2 = Button(text = "Add a Recipe")
        btn2.bind(on_press=self.clk2)
        btn3 = Button(text = "Learn to Cook")
        btn3.bind(on_press=self.clk3)
        btn4 = Button(text = "More...")
        btn4.bind(on_press=self.clk4)


        layout.add_widget(Label(text="Welcome to My Cooking App"))
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)

        return layout

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
        

class secondpage(FloatLayout):
    def build(self):
        self.backbutton()
        self.searchbox()
        self.label()
        self.searchbutton()
        
    def backbutton(self):
        self.btn1 = Button()
        self.btn1.text = "Back"
        #self.btn1.pos = (35,500)
        self.btn1.pos_hint = {'x' :.025, 'y' :.88}
        self.btn1.size_hint = (.1,.08)
        self.btn1.font_size = 20
        self.add_widget(self.btn1)
        self.btn1.bind(on_press = self.clk1)
        
        
    def label(self):
        self.label1 = Label(text = "Recipes at your Fingertips" ,
                           font_size = 30,
                           size_hint = (1,1.8),
                           pos_hint = {'x' :.01, 'y' :.01})
                         #color = [255,255,255,0])
        self.add_widget(self.label1)
        
          
    def searchbox(self) :
        self.search = TextInput(hint_text = "Tell us what you have ",
                          font_size = 15,
                          size_hint =(.7,.05),
                          pos_hint = {'x':.15, 'y':.8})
        self.add_widget(self.search)
        

    def searchbutton(self):
        self.btn2 = Button()
        self.btn2.text = "Search"
        #self.btn1.pos = (35,500)
        self.btn2.pos_hint = {'x' :.87, 'y' :.8}
        self.btn2.size_hint = (.08,.05)
        self.btn2.font_size = 15
        self.add_widget(self.btn2)
        self.btn2.bind(on_press = self.clk2)

    def scroll (self):
        self.scrollview 

    def clk1(self,obj):
        search.stop()
        app.run()
        
    def clk2(self,obj):
        my_key = '8b6f178c57d40dee7d88629b32e01c23'
        my_id = 'fabbe897'
        userAnswer = self.search.text
        userAnswer = userAnswer.rstrip()
        userAnswer = userAnswer.lstrip()
        counter = 1
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

        r = requests.get('http://api.yummly.com/v1/api/recipes?_app_id=fabbe897&_app_key=8b6f178c57d40dee7d88629b32e01c23&',params = my_search)


        data = r.json()

        for i in range(0,10):
            if(i == 0):
                thing = str(data["matches"][i]["smallImageUrls"])
                thing = thing[2:-2]
                img = AsyncImage(source=thing, pos_hint ={'center_x':.34, 'center_y':.7}, size_hint = (5,5))
                self.butt= Button(text = data["matches"][i]["recipeName"],
                                  font_size = 10.5,
                                  size_hint =(.29,.1),
                                  pos_hint = {'x':.19, 'y':.53})
                self.add_widget(self.butt)
                self.add_widget(img)
            elif(i == 1):
                thing1 = str(data["matches"][i]["smallImageUrls"])
                thing1 = thing1[2:-2]
                img1 = AsyncImage(source=thing1, pos_hint ={'center_x':.63, 'center_y':.7}, size_hint = (5,5))
                self.butt= Button(text = data["matches"][i]["recipeName"],
                                  font_size = 10.5,
                                  size_hint =(.29,.1),
                                  pos_hint = {'x':.5, 'y':.53})
                self.add_widget(self.butt)
                self.add_widget(img1)
            elif(i == 2):
                thing2 = str(data["matches"][i]["smallImageUrls"])
                thing2 = thing2[2:-2]
                img2 = AsyncImage(source=thing2, pos_hint ={'center_x':.34, 'center_y':.43}, size_hint = (5,5))
                self.butt= Button(text = data["matches"][i]["recipeName"],
                                  font_size = 10.5,
                                  size_hint =(.29,.1),
                                  pos_hint = {'x':.19, 'y':.27})
                self.add_widget(self.butt)
                self.add_widget(img2)
            elif(i == 3):
                thing3 = str(data["matches"][i]["smallImageUrls"])
                thing3 = thing3[2:-2]
                img3 = AsyncImage(source=thing3, pos_hint ={'center_x':.63, 'center_y':.43}, size_hint = (5,5))
                self.butt= Button(text = data["matches"][i]["recipeName"],
                                  font_size = 10.5,
                                  size_hint =(.29,.1),
                                  pos_hint = {'x':.5, 'y':.27})
                self.add_widget(self.butt)
                self.add_widget(img3)
            elif(i == 4):
                thing4 = str(data["matches"][i]["smallImageUrls"])
                thing4 = thing4[2:-2]
                img4 = AsyncImage(source=thing4, pos_hint ={'center_x':.34, 'center_y':.19}, size_hint = (5,5))
                self.butt= Button(text = data["matches"][i]["recipeName"],
                                  font_size = 10.5,
                                  size_hint =(.29,.1),
                                  pos_hint = {'x':.19, 'y':.01})
                self.add_widget(self.butt)
                self.add_widget(img4)
            elif(i == 5):
                thing5 = str(data["matches"][i]["smallImageUrls"])
                thing5 = thing5[2:-2]
                img5 = AsyncImage(source=thing5, pos_hint ={'center_x':.63, 'center_y':.19}, size_hint = (5,5))
                self.butt= Button(text = data["matches"][i]["recipeName"],
                                  font_size = 10.5,
                                  size_hint =(.29,.1),
                                  pos_hint = {'x':.5, 'y':.01})
                self.add_widget(self.butt)
                self.add_widget(img5)
            
        print("Done")
            #print(data["matches"][i]["recipeName"])
            #print(data["matches"][i]["smallImageUrls"])
            #print("  ")
        
class SecondpageApp(App):
    def build (self) :
        Layout = secondpage()
        Layout.build()
        return Layout


        
class addRecipe(App):
    def build(self):
        f = FloatLayout()
        saveB = Button(text = "Save",
                       size_hint =(.1,.1),
                       pos_hint = {'x':.35,'y':.05})
        saveB.bind(on_press = self.clk)
        
        cancelB = Button(text = "Cancel",
                         size_hint =(.1,.1),
                         pos_hint = {'x':.55, 'y':.05})
        
        self.name1 = TextInput(hint_text= "Name of Recipe",size_hint =(.7,.05),pos_hint = {'x':.15, 'y':.8})
        
        self.servings = TextInput(hint_text= "Servings",
                             font_size = 10,
                             multiline = False,
                             size_hint = (.1,.05),
                             pos_hint = {'x':.3, 'y':.7})
        self.time1 = TextInput(hint_text = "Time required",
                         font_size = 10,
                         multiline = False,
                         size_hint = (.1,.05),
                         pos_hint = {'x':.15, 'y':.7})
        self.ingredients = TextInput(hint_text = "Ingredients",
                                font_size = 10,
                                size_hint = (.7,.05),
                                pos_hint = {'x':.15, 'y':.6})
        self.directions = TextInput(hint_text = "Directions",
                               font_size = 10,
                               size_hint = (.7,.35),
                               pos_hint = {'x':.15, 'y':.2})
        cancelB.bind(on_press = self.clk1)

            
        f.add_widget(Label(text = "Add a Recipe", font_size = 45,size_hint=(1,1.9)))
        f.add_widget(saveB)
        f.add_widget(cancelB)
        f.add_widget(self.name1)
        f.add_widget(self.servings)
        f.add_widget(self.time1)
        f.add_widget(self.ingredients)
        f.add_widget(self.directions)

        return f
    

    def clk(self,obj):
        print(self.name1.text)
        print(self.servings.text)
        print(self.time1.text)
        print(self.ingredients.text)
        print(self.directions.text)
        
        popup = Popup(title = "Confirmation",
                      content=Label(text = "Saved!"),
                      size_hint = (None,None),
                      size=(200,150))
        popup.open()
        
    def clk1(self,obj):
        add.stop()
        app.run()


class LearnToCook(App):

    def build(self):
        
        layout = FloatLayout()

        self.words = TextInput(hint_text="What do you want to learn?",
                          multiline = False, size_hint= (.5, .05),
                          pos_hint = {'x':.17 , 'y':.85})
        
        btn = Button(text = "Search", size_hint = (.15, .05), pos_hint = {'x':.68 , 'y':.8491})
        btn.bind(on_press=self.clk)
        btn1 = Button(text = "Back", size_hint = (.05, .05), pos_hint = {'x':.008, 'y':.94})
        btn1.bind(on_press=self.goBack)

        layout.add_widget(Label(text="Learn To Cook", size_hint = (1, 1.9), font_size = 25))
        layout.add_widget(self.words)
        layout.add_widget(btn)
        layout.add_widget(btn1)

        return layout

    

    def goBack(self, obj):
        learn.stop()
        app.run()

    def clk(self, obj):
        print(self.words.text)

class interestingContent(App):
    def build(self):
        f = FloatLayout()

        btn1 = Button(text = "Back", size_hint = (.05, .05), pos_hint = {'x':.008, 'y':.94})
        btn1.bind(on_press=self.goBack)
        
        f.add_widget(Label(text = "More",
                           font_size = 45,
                           size_hint=(1,1.9)))
        f.add_widget(btn1)
        
        return f

    def goBack(self, obj):
        more.stop()
        app.run()

if __name__ == "__main__":
    
    app = HomePage()
    search = SecondpageApp()
    add = addRecipe()
    learn = LearnToCook()
    more = interestingContent()
    app.run()
