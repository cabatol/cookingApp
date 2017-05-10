from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from apiclient.discovery import build
from oauth2client.tools import argparser
import random
import webbrowser
from kivy.uix.video import Video

API_Key = "AIzaSyAUZFGhlri17-rWRYUfl0grRWfgNmBqrxM"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

VideoIds = [ ]

def yt_search(term):
    youtube = build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION, developerKey = API_Key)
    
    search_response = youtube.search().list(
        q =term,
        part="id,snippet",
        maxResults=1
        ).execute()
        
    videos = []
 
    for search_results in search_response.get("items", [ ]):
        if search_results["id"]["kind"] == "youtube#video":
            videos.append("%s (%s)" % (search_results["snippet"]["title"],search_results["id"]["videoId"]))
            Id = search_results["id"]["videoId"]
            VideoIds.append(Id)

    Random_Id = (random.choice(VideoIds))
    return Random_Id

class LearnToCook(App):

    def build(self):

        
        
        layout = FloatLayout()

        self.words = TextInput(text = "How to: ",
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
        print("go back")

    def clk(self, obj):
        search = self.words.text
        search = search.rstrip()
        search = search.lstrip()        
        search = search.replace(" ", "+")
        url1 = yt_search(search)
        url2 = "https://www.youtube.com/watch?v="
        url = url2 + url1
        webbrowser.open(url)
        
if __name__ == "__main__":
    app = LearnToCook()
    app.run()
    