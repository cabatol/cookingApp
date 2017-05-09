from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
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
        
        fname = self.name1.text + ".txt"
        name = self.name1.text + "\n"
        servings = "Servings: " + self.servings.text + " "
        time = "Time: " + self.time1.text + "\n"
        ingredients = "\nIngredients:\n" + self.ingredients.text + "\n"
        directions = "\nDirections:\n" + self.directions.text

        f =open(fname, "w+")
        f.write(name)
        f.write(servings)
        f.write(time)
        f.write(ingredients)
        f.write(directions)
        f.close()

        
        content = Button(text = self.name1.text + "\nhas been saved successfully.",
                         halign = "center", valign = "middle")
        popup =  Popup (title = "Congratulations!",
                        content = content,
                        size_hint = (None, None),
                        size = (300, 300),
                        auto_dismiss = True)
        content.bind(on_press=popup.dismiss)
        popup.open()

if __name__ == "__main__":
    addRecipe().run()
