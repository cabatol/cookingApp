#Secondpageapp
import requests
import json
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.image import Image as CoreImage
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView


class secondpage(FloatLayout):
    def build(self) :
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
        self.btn1.bind(on_press=self.clk1)
        
        
    def label(self):
        self.label1 = Label(text = "Recipes at your Fingertips" ,
                           font_size = 30,
                           size_hint = (1,1.8),
                           pos_hint = {'x' :.01, 'y' :.01})
                         #color = [255,255,255,0])
        self.add_widget(self.label1)
        
          
    def searchbox(self) :
        self.search = TextInput(hint_text = "Tell us what you have: ",
                          font_size = 20,
                          pos_hint = {'x' :.17, 'y' :.25},
                          size_hint = (.53,0.4))
        self.add_widget(self.search)

    def searchbutton(self):
        self.btn2 = Button()
        self.btn2.text = "Search"
        #self.btn1.pos = (35,500)
        self.btn2.pos_hint = {'x' :.72, 'y' :.57}
        self.btn2.size_hint = (.1,.08)
        self.btn2.font_size = 20
        self.add_widget(self.btn2)
        self.btn2.bind(on_press=self.clk2)

    def scroll (self):
        self.scrollview 

    def clk1(self, obj):
        print("go back")
    def clk2(self, obj):
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
                img = AsyncImage(source=thing)
                self.butt= Button(text = data["matches"][i]["recipeName"],
                                  font_size = 10.5,
                                  size_hint =(.3,.1),
                                  pos_hint = {'x':.19, 'y':.5})
                self.add_widget(self.butt)
                self.add_widget(img)
            elif(i == 1):
                thing1 = str(data["matches"][i]["smallImageUrls"])
                thing1 = thing1[2:-2]
                img1 = AsyncImage(source=thing1)
                self.butt= Button(text = data["matches"][i]["recipeName"],
                                  font_size = 10.5,
                                  size_hint =(.3,.1),
                                  pos_hint = {'x':.5, 'y':.5})
                self.add_widget(self.butt)
                self.add_widget(img1)
            elif(i == 2):
                thing2 = str(data["matches"][i]["smallImageUrls"])
                thing2 = thing2[2:-2]
                img2 = AsyncImage(source=thing2)
                self.butt= Button(text = data["matches"][i]["recipeName"],
                                  font_size = 10.5,
                                  size_hint =(.3,.1),
                                  pos_hint = {'x':.19, 'y':.3})
                self.add_widget(self.butt)
                self.add_widget(img2)
            elif(i == 3):
                thing3 = str(data["matches"][i]["smallImageUrls"])
                thing3 = thing3[2:-2]
                img3 = AsyncImage(source=thing3)
                self.butt= Button(text = data["matches"][i]["recipeName"],
                                  font_size = 10.5,
                                  size_hint =(.3,.1),
                                  pos_hint = {'x':.5, 'y':.3})
                self.add_widget(self.butt)
                self.add_widget(img3)
            elif(i == 4):
                thing4 = str(data["matches"][i]["smallImageUrls"])
                thing4 = thing4[2:-2]
                img4 = AsyncImage(source=thing4)
                self.butt= Button(text = data["matches"][i]["recipeName"],
                                  font_size = 10.5,
                                  size_hint =(.3,.1),
                                  pos_hint = {'x':.19, 'y':.01})
                self.add_widget(self.butt)
                self.add_widget(img4)
            elif(i == 5):
                thing5 = str(data["matches"][i]["smallImageUrls"])
                thing5 = thing5[2:-2]
                img5 = AsyncImage(source=thing5)
                self.butt= Button(text = data["matches"][i]["recipeName"],
                                  font_size = 10.5,
                                  size_hint =(.3,.1),
                                  pos_hint = {'x':.5, 'y':.01})
                self.add_widget(self.butt)
                self.add_widget(img5)

                
class SecondpageApp (App) :
    def build (self) :
        Layout = secondpage()
        Layout.build()
        return Layout
    
if __name__ == '__main__':
    SecondpageApp().run()