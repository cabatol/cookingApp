from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class myLayout(BoxLayout):
    def __init__ (self, **kwargs):
        super(myLayout, self).__init__(**kwargs)

        btn1 = Button(text = "Search for a Recipe")
        btn1.bind(on_press=self.clk1)
        btn2 = Button(text = "Add a Recipe")
        btn2.bind(on_press=self.clk2)
        btn3 = Button(text = "Learn to Cook")
        btn3.bind(on_press=self.clk3)
        btn4 = Button(text = "More...")
        btn4.bind(on_press=self.clk4)

        self.add_widget(Label(text="Welcome to My Cooking App"))
        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)
        self.add_widget(btn4)

    def clk1(self, obj):
        print("Hi There")
    def clk2(self, obj):
        print("Hi There!")
    def clk3(self, obj):
        print("Hi There!!")
    def clk4(self, obj):
        print("Hi There!!!")

class NameApp(App):
    def build(self):
        mL = myLayout()
        return mL

if __name__ == "__main__":
    NameApp().run()