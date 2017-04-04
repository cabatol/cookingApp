from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout

class LearnToCook(App):

    def build(self):
        
        layout = FloatLayout()

        words = TextInput(text="What do you want to learn?",
                          multiline = False, size_hint= (.5, .05),
                          pos_hint = {'x':.17 , 'y':.85})
        #words.bind()
        
        btn = Button(text = "Search", size_hint = (.15, .05), pos_hint = {'x':.68 , 'y':.8491})
        btn.bind(on_press=self.clk)

        layout.add_widget(Label(text="Learn To Cook", size_hint = (1, 1.9), font_size = 25))
        layout.add_widget(words)
        layout.add_widget(btn)

        return layout

    def on_enter(instance, value):
        print('User pressed enter in', instance)

    def clk(self, obj):
        print("does this work?")

        

if __name__ == "__main__":
    app = LearnToCook()
    app.run()
    