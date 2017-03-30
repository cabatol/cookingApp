from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class CookingApp(App):
    def build(self):
        f = FloatLayout()
        saveB = Button(text = "Save", size_hint =(.1,.1), pos = (290,25))
        cancelB = Button(text = "Cancel", size_hint =(.1,.1), pos =(400,25))
        name = TextInput(text = "Name of recipe",font_size = 10, multiline = False, size_hint = (.5,.05),pos =(200,455))
        servings = TextInput(text= "Servings",font_size = 10, multiline = False, size_hint = (.1,.05),pos =(299,400))
        time = TextInput(text = "Time required",font_size = 10, multiline = False, size_hint = (.1,.05), pos =(435, 400))
        ingredients = TextInput(text = "Ingredients",font_size = 10, size_hint = (.5,.05), pos =(200, 355))
        directions = TextInput(text = "Directions",font_size = 10, size_hint = (.5,.3), pos =(200,155))
        #saveB.bind(on_press = self.clk)
        #cancelB.bind(on_press = self.click1)

        
        f.add_widget(Label(text = "Add a Recipe", font_size = 45, size_hint=(1,1.9)))
        f.add_widget(saveB)
        f.add_widget(cancelB)
        f.add_widget(name)
        f.add_widget(servings)
        f.add_widget(time)
        f.add_widget(ingredients)
        f.add_widget(directions)
        

        return f
    #def clk(self,obj):
        #print("Hello Wo")



if __name__ == "__main__":
    CookingApp().run()