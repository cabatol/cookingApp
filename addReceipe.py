from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager,Screen


def on_text(instance,value):
    print(instance,value)
    
class addRecipe(App):
    def build(self):
        f = FloatLayout()
        
        self.name1 = TextInput(hint_text= "Name of Recipe",multiline = False,size_hint =(.7,.05),pos_hint = {'x':.15, 'y':.8})
        
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
        #Save Button
        saveB = Button(text = "Save",
                       size_hint =(.1,.1),
                       pos_hint = {'x':.35,'y':.05})
        
        saveB.bind(on_press = self.clk)

        #Cancel Button
        cancelB = Button(text = "Cancel",
                         size_hint =(.1,.1),
                         pos_hint = {'x':.55, 'y':.05})

            
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

        name = self.name1.text + "\n"
        servings = "Servings: " + self.servings.text + " "
        time= self.time1.text
        print(self.ingredients.text)
        print(self.directions.text)

        f =open("output.txt", "w+")
        f.write()
        f.write()
        f.write()
        f.write()
        f.write()
        f.close()
        
        popup = Popup(title = self.name1.text,
                      content=Label(text = "Saved"),
                      size_hint = (None,None),
                      size=(200,150))
        popup.open()



if __name__ == "__main__":
    addRecipe().run()