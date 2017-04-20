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
        raw_answer=userAnswer
        recipe,recipe1,recipe2 = raw_answer.split(' ')
        my_search= {
            'q' : recipe,
            'requirePictures': 'True',
            'allowedIngredient[]': [recipe,recipe1,recipe2]
            
        }

        r = requests.get('http://api.yummly.com/v1/api/recipes?_app_id=fabbe897&_app_key=8b6f178c57d40dee7d88629b32e01c23&',params = my_search)


        info = r.json()
        print(info)
   

                
class SecondpageApp (App) :
    def build (self) :
        Layout = secondpage()
        Layout.build()
        return Layout
    
if __name__ == '__main__':
    SecondpageApp().run()