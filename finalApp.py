from kivy.app import App
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
        self.btn2.bind(on_press = self.clk2)

    def scroll (self):
        self.scrollview 

    def clk1(self,obj):
        search.stop()
        app.run()
        
    def clk2(self,obj):
        print(self.search.text)
        
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
        
        name = TextInput(hint_text= "Name of Recipe",size_hint =(.7,.05),pos_hint = {'x':.15, 'y':.8})
        
        servings = TextInput(hint_text= "Servings",
                             font_size = 10,
                             multiline = False,
                             size_hint = (.1,.05),
                             pos_hint = {'x':.3, 'y':.7})
        time = TextInput(hint_text = "Time required",
                         font_size = 10,
                         multiline = False,
                         size_hint = (.1,.05),
                         pos_hint = {'x':.15, 'y':.7})
        ingredients = TextInput(hint_text = "Ingredients",
                                font_size = 10,
                                size_hint = (.7,.05),
                                pos_hint = {'x':.15, 'y':.6})
        directions = TextInput(hint_text = "Directions",
                               font_size = 10,
                               size_hint = (.7,.35),
                               pos_hint = {'x':.15, 'y':.2})
        cancelB.bind(on_press = self.clk1)

            
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