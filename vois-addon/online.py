import os
import requests
class my_git_installer_exemplar:
    def __init__(self, url, path="cache", name=None):
        self.url=url
        self.path=path
        if name==None: 
            name=url.split("/")
            name.reverse()
        self.name=name[0]
        
    def install(self, path=None, name=None):
        if path!=None: self.path=path
        if name!=None: self.name=name
        os.makedirs("data/" + self.path, exist_ok=True)
        with open("data/" + self.path + "/" + self.name, "wb") as f:
            response = requests.get(self.url, stream=True)
            for chunk in response.iter_content(chunk_size=102400):
                if chunk:f.write(chunk)
                
def install_all_music(a):
    for i in a:
        my_music.install(i)

class my_music_installer_exemple:
    def __init__(self):
        self.my_music_url=[
            "https://raw.githubusercontent.com/BOTX2000/vois_addon/main/vois-addon/data/cache/my_music0.mp3", 
            "https://raw.githubusercontent.com/BOTX2000/vois_addon/main/vois-addon/data/cache/my_music1.mp3"
            ]
        
    def install(self, id):
        if id=="all": install_all_music(len(self.my_music_url))
        if id>len(self.my_music_url)-1:
            print("index error")
            return
        mass=self.my_music_url[id]
        mass=mass.split("/")
        mass.reverse()
        name=mass[0]
        with open("data/cache/"+name, "wb") as f:
            response = requests.get(self.my_music_url[id], stream=True)
            for chunk in response.iter_content(chunk_size=102400):
                if chunk:f.write(chunk)
                        
class test(my_git_installer_exemplar):
    def __init__(self):
        super().__init__("https://alphacephei.com/vosk/models/vosk-model-en-us-daanzu-20200905-lgraph.zip")
        
class command_i(my_git_installer_exemplar):
    def __init__(self):
        super().__init__("https://raw.githubusercontent.com/BOTX2000/vois-addon/main/command.txt")
        
class my_music(my_music_installer_exemple):
    def __init__(self):
        super().__init__()
            