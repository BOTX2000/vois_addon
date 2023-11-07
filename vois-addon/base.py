import datetime
from tkinter import messagebox
from tkinter import*
from os import system
from pyautogui import*
from keyboard import*
import random
from multiprocessing import*

from time import*
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

from subprocess import*
from psutil import*

import requests

import pyglet

def errors(m):
    mode=["r", "w", "w"]
    er=1
    f=open("data/cache/error.txt", mode[m])
    if m==0:
        er=f.read()
    elif m==1:
        f.write("0")
    else:
        f.write("1")
    f.close()
    return(er)

def check_cache():
    er=0
    print("1")
    if not os.path.exists("data/cache/s.txt"):
        open("data/cache/s.txt", "w").close
    print("2")
    if not os.path.exists("data/cache/music.txt"):
        f=open("data/cache/music.txt", "w")
        f.write("0")
        f.close()
    print("3")
    if not os.path.exists("data/cache/music_work.txt"):
        f=open("data/cache/music_work.txt", "w")
        f.write("0")
        f.close()
    print("4")
    if not os.path.exists("data/setting.txt"):
        seve("", 1, 10, 0.1, 1, 100)
    print("5")
    if not os.path.exists("data/data/command.txt"):
        messagebox.showerror("error", message="the command file is lost")
        er+=1
        er=errors(2)
        print("6")
        try:
            online(a=3, p="command")
            print("7")
            er=errors(1)
            er-=1
        except: pass
        #online(a=3, p="command")
    if er==0:
        re=errors(1)
        print("good")

def pre(a):
    if a==0:
        write('print("")')
        press("left")
        sleep(0.1)
        press("left")

def fr(a):
    if a!=5:
        sets=open("data\setting.txt", "r")
        setting=sets.read()
        sets.close()
        setting=setting.split("\n")
        return(setting[a])
    else:
        return(ent_save(0, 0))

def ent_save(a, s):
    dia=["r", "w"]
    f=open("data/cache/ent.txt", dia[s])
    if s==1:
        f.write(str(a))
        f.close()
    else:
        return(f.read())
        
    
def save(win, a, b, c, d, e, f):
    sets=open("data\setting.txt", "w")
    sets.write(f"{a}\n{b}\n{c}\n{d}\n{e}")
    sets.close()
    ent_save(f, 1)
    if d=="1" and win!="":
        win.destroy()

def setting():
    win=Tk()
    win.geometry("500x400+420+150")
    win.title("settnig")
    
    l=Label(win, text=f"random: with                    to")
    l.place(x=50, y=20)
    l1=Label(win, text="volume change to:")
    l1.place(x=50, y=40)
    l2=Label(win, text="automatic closing of the settings window after saving:")
    l2.place(x=50, y=60)
    l3=Label(win, text="move the mouse to:")
    l3.place(x=50, y=80)
    l4=Label(win, text="pause mode:")
    l4.place(x=50, y=100)
    
    i1=Entry(win, width=7)
    i1.place(x=130, y=20)# to l
    i1.insert(1, fr(0))
    i2=Entry(win, width=7)
    i2.place(x=199, y=20)# to l
    i2.insert(1, fr(1))
    i3=Entry(win, width=7)
    i3.place(x=160, y=40)# to l1
    i3.insert(1, fr(2))
    i4=Entry(win, width=7)
    i4.place(x=345, y=60)# to l2
    i4.insert(1, fr(3))
    i5=Entry(win, width=7)
    i5.place(x=170, y=80)# to l3
    i5.insert(1, fr(4))
    i6=Entry(win, width=7)
    i6.place(x=125, y=100)# to l4
    i6.insert(1, fr(5))
    
    b=Button(win, text="save", command=lambda: save(win, i1.get(), i2.get(),
                                                    i3.get(), i4.get(), i5.get(), i6.get()))
    b.place(x=240, y=365)
    win.bind("<F5>", lambda a: save(win, i1.get(), i2.get(), i3.get(), i4.get(),
                                    i5.get(), i6.get()))
    win.grab_set()
    win.mainloop()

def prin(a):
    text=["доброго", "куди?"]
    print(text[a])

def text(a):
    dia=["c", "v", "s"]
    keyDown("ctrl")
    keyDown(dia[a])
    sleep(0.1)
    keyUp(dia[a])
    keyUp("ctrl")
    return

def data_music(a):
    m=0
    mode=["r", "w", "w"]
    f=open("data/cache/music.txt", mode[a])
    if a==0:
        m=f.read()
    elif a==2:
        f.write("1")
    else:
        f.write("0")
    f.close()
    return(m)

def song(s):
    volume = cast(AudioUtilities.GetSpeakers().Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None),
              POINTER(IAudioEndpointVolume))
    a=volume.GetMasterVolumeLevelScalar()
    funk=["a+float(fr(2))", "a-float(fr(2))", "press('play/pause media')",
          "press('volume mute')", "press('next track')",
          "press('previous track')"]
    m=data_music(0)
    if s<2:
        b=eval(funk[s])
        volume.SetMasterVolumeLevelScalar(b, None)
    elif s==2 and m=="1" and int(st(0))==1:
        m=data_music(1)
    elif s==2 and m=="0" and int(st(0))==1:
        m=data_music(2)
    else:
        eval(funk[s])

def spotify():
    try:
        system(r"C:\Users\User\AppData\Roaming\Spotify\Spotify.exe")
    except:
        google("https://open.spotify.com/")
        press("enter")

def time():
    h=str(datetime.datetime.now().hour)
    h+=":"
    m=datetime.datetime.now().minute
    for i in range(10):
        if m==i:
            g=str(i)
            m=f"0{g}"
    h+=str(m)

    messagebox.showerror("time:", message=h)

def randoms():
    messagebox.showerror("random:", message=random.randint(int(fr(0)),
                                                           int(fr(1))))

def discord():
    system(r'C:\Users\User\AppData\Local\Discord\Update.exe --processStart Discord.exe')

def google(url=None):
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

    running_processes = []
    for process in process_iter(['name']):
        running_processes.append(process.info['name'])

    if 'chrome.exe' in running_processes and url==None:
        url = "http://www.google.com"
    else:
        pass
        
    Popen([chrome_path, url])

def move(a):
    x, y=position()
    xy=["x, y-int(fr(4))", "x, y+int(fr(4))", "x-int(fr(4)), y",
        "x+int(fr(4)), y"]
    moveTo(eval(xy[a]))

def de(d):
    text=d.get()
    d.delete(0, 100000)
    d.insert(0, eval(text))

def calculator():
    win=Tk()
    win.title("calculator")
    win.geometry("500x400+420+150")

    d=Entry(win, width=20)
    d.grid()
    d.bind("<Return>", lambda a: de(d))
    win.mainloop()

def pere (text1, inpu, text):
    text1.insert(1.0, "1")
    text1.delete(1.0, 200.0)
    texts=inpu.get()
    lat=["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]",
         "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'",
         "z", "x", "c", "v", "b", "n", "m", ",", ".", "/",
         "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "{", "}",
         "A", "S", "D", "F", "G", "H", "J", "K", "L", ":", '"',
         "Z", "X", "C", "V", "B", "N", "M", "<", ">", "?",
         "!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

    ua=["й", "ц", "у", "к", "е", "н", "г", "ш", "щ", "з", "х", "ї",
        "ф", "і", "в", "а", "п", "р", "о", "л", "д", "ж", "є",
        "я", "ч", "с", "м", "и", "т", "ь", "б", "ю", ".",
        "Й", "Ц", "У", "К", "Е", "Н", "Г", "Ш", "Щ", "З", "Х", "Ї",
        "Ф", "І", "В", "А", "П", "Р", "О", "Л", "Д", "Ж", "Є",
        "Я", "Ч", "С", "М", "И", "Т", "Ь", "Б", "Ю", ",",
        "!", '"', "№", ";", "%", ":", "?", "*", "(", ")"]
    a=0
    for i in lat:
        texts=texts.replace(i, ua[a])
        a+=1
    text1.insert(1.0, texts)

def kurulusa():
    window = Tk()
    window.title("Translator")
    window.geometry('305x450+500+125')
    text = Label(window, text="Text")
    text.grid(column=0, row=0)
    text1= Text(window, width=31, height=22, font=1)
    text1.grid(column=0, row=2)
    inpu = Entry(window, width=50)
    inpu.grid(column=0, row=1)
    inpu.bind("<Return>", lambda a: pere(text1, inpu, text))
    window.mainloop()


def st(a):
    di=["r", "w", "w"]
    ret=164
    f=open("data/cache/music_work.txt", di[a])
    if a==0:
        ret=f.read()
    elif a==1:
        f.write("0")
    elif a==2:
        f.write("1")
    f.close()
    return(ret)

def install_all_music():
    for i in range(online(d=1)):
        online(a=i, p=i)

def online(d=0, a=0, p=0):
    file_url=["https://drive.google.com/uc?id=1eQUC02pbqubt30ftSd0-f1iGLoZdsQxZ&export=download", #music0
              "https://drive.google.com/uc?id=15tU7UKczHjMZP0ge6Plr12y6nOF79liL&export=download", #music1
              "https://drive.google.com/uc?id=1EFw5vpWO1Nz-J9kMi7bv8fpKd34_5_eZ&export=download", #rar
              "https://raw.githubusercontent.com/BOTX2000/vois-addon/main/command.txt", #command.txt
              ""]
    save_path = f"data/cache/my_music{p}.mp3"
    if d==1:
        return(len(file_url))
    if p=="command":
        print("install command...")
        response = requests.get(file_url[a])
        if response.status_code == 200:
            print("create...")
            with open("data/data/command.txt", 'wb') as file:
                file.write(response.content)
                print("done!")
                return
        else:
            print(f"Failed to download file. Status code: {response.status_code}")
    try:
        print("install...")
        response = requests.get(file_url[a])
        if response.status_code == 200:
            with open("data/data/command.txt", 'wb') as file:
                file.write(response.content)
        else:
            messagebox.showerror("error", message="The file could not be"+
                                 " accessed.")
    except Exception as e:
        messagebox.showerror("error", message=f"An error occurred while downlo"+
                             f"ading the file: {str(e)}")

def plays(n=0):
    player = pyglet.media.Player()
    if not os.path.exists("data/cache/my_music{n}.mp3"):
        online(a=n, p=n)
    source = pyglet.media.load(f'data/cache/my_music{n}.mp3')
    m=data_music(2)
    a=st(2)
    player.queue(source)
    player.play()
    while True:
        while m!="0":
            a=st(0)
            if a=="0":
                m=data_music(1)
                quit()
            m=data_music(0)
        player.pause()
        while m!="1":
            a=st(0)
            if a=="0":
                m=data_music(1)
                quit()
            m=data_music(0)
        player.play()






        
