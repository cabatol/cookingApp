from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup


def on_text(instance,value):
    print(instance,value)
    
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
        
        name = TextInput(size_hint = (.7,.05),
                         pos_hint = {'x':.15, 'y':.8})
        name.bind(text=on_text)
        
        servings = TextInput(text= "Servings",
                             font_size = 10,
                             multiline = False,
                             size_hint = (.1,.05),
                             pos_hint = {'x':.3, 'y':.7})
        time = TextInput(text = "Time required",
                         font_size = 10,
                         multiline = False,
                         size_hint = (.1,.05),
                         pos_hint = {'x':.15, 'y':.7})
        ingredients = TextInput(text = "Ingredients",
                                font_size = 10,
                                size_hint = (.7,.05),
                                pos_hint = {'x':.15, 'y':.6})
        directions = TextInput(text = "Directions",
                               font_size = 10,
                               size_hint = (.7,.35),
                               pos_hint = {'x':.15, 'y':.2})
        #cancelB.bind(on_press = self.clk)

        
        f.add_widget(Label(text = "Add a Recipe", font_size = 45,size_hint=(1,1.9)))
        f.add_widget(saveB)
        f.add_widget(cancelB)
        f.add_widget(name)
        f.add_widget(servings)
        f.add_widget(time)
        f.add_widget(ingredients)
        f.add_widget(directions)

        return f
    

    def clk(self,obj):
        popup = Popup(title = "Confirmation",
                      content=Label(text = "Saved!"),
                      size_hint = (None,None),
                      size=(200,150))
        popup.open()


if __name__ == "__main__":
    addRecipe().run()