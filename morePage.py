from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

class interestingContent(App):
    def build(self):
        f = FloatLayout()
        f.add_widget(Label(text = "More",
                           font_size = 45,
                           size_hint=(1,1.9)))
        return f


if __name__ == "__main__":
    interestingContent().run()