from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]

class HomePage(App):
    def setOrientation(self, orient):
        self.orient = orient
        
    def build(self):
        layout = BoxLayout(padding=100, orientation=self.orient)
        
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
        print("Hi There")
    def clk2(self, obj):
        print("Hi There!")
    def clk3(self, obj):
        print("Hi There!!")
    def clk4(self, obj):
        print("Hi There!!!")

if __name__ == "__main__":
    app = HomePage()
    app.setOrientation(orient="vertical")
    app.run()