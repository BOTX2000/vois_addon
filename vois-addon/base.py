import datetime
from tkinter import messagebox
from tkinter import*
from os import system
from pyautogui import*
import pyautogui
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

from PIL import Image



###########

from file_os import*
clas=["s", "lock_s", "ent", "error", "music", "music_work", "setting", "command",
      ]
for i in clas:
    globals()[i.lower()] = globals()[i]()

pyautogui.FAILSAFE=False

############
"""
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
"""

def bind():
    add_hotkey("decimal+enter", lambda: click())
    wait()

def check_cache():
    er=0
    if not os.path.exists("data/cache/s.txt"):
        s.write()
    if not os.path.exists("data/cache/ent.txt"):
        ent.write()
    if not os.path.exists("data/cache/error.txt"):
        error.write()
    if not os.path.exists("data/cache/music.txt"):
        music.write()
    if not os.path.exists("data/cache/music_work.txt"):
        music_worc.write()
    if not os.path.exists("data/setting.txt"):
        save("", 1, 10, 0.1, 1, 100, 0)
    if not os.path.exists("data/data/command.txt"):
        messagebox.showerror("error", message="the command file is lost")
        er+=1
        error.write(True)
        try:
            online(a=3, p="command")
            error.write()
            er-=1
        except: pass
        #online(a=3, p="command")
    if er==0:
        error.write()
        print("good")

def pre(a):
    if a==0:
        write('print("")')
        press("left")
        sleep(0.1)
        press("left")

def fr(a):
    if a!=5:
        settin=setting.read()
        settin=settin.split("\n")
        return(settin[a])
    else:
        return(ent.read())
    
"""
def ent_save(a, s):
    dia=["r", "w"]
    f=open("data/cache/ent.txt", dia[s])
    if s==1:
        f.write(str(a))
        f.close()
    else:
        return(f.read())
"""        
    
def save(win, a, b, c, d, e, f):
    setting.write(f"{a}\n{b}\n{c}\n{d}\n{e}")
    ent.write(f)
    if d=="1" and win!="":
        win.destroy()

def label(x, y, win, text):
    l=Label(win, text=text)
    l.place(x=x, y=y)
    return(l)

def entry(x, y, win, pos):
    i=Entry(win, width=7)
    i.place(x=x, y=y)
    i.insert(1, fr(pos))
    return(i)
    
def settin():
    win=Tk()
    win.geometry("500x400+420+150")
    win.title("settnig")

    
    
    """
    x_l=50
    y_l=20
    text_l=["random: with                    to",
            "volume change to:",
            "automatic closing of the settings window after saving:",
            "move the mouse to:", "pause mode:"]
    x_e=["130", "199", "160", "354", "170", "125"]
    y_e=20
    for i in range(5):
        globals()[f"l{i}"]=eval(f"label({x_l}, {y_l}, {win}, {text_l[i-1]})")
        y_l+=20
    for i in range(6):
        globals()[f"l{i}"]=eval(f"entry({x_e[i-1]}, {y_e}, {win}, {i})")
        if i!=1:
            y_e+=20
    """
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
                                                    i3.get(), i4.get(), i5.get(),
                                                    i6.get()))
    b.place(x=240, y=365)
    win.bind("<F5>", lambda a: save(win, i1.get(), i2.get(), i3.get(), i4.get(),
                                    i5.get(), i6.get()))
    win.grab_set()
    win.mainloop()

def prin(a):
    text=["доброго", "куди?"]
    messagebox.showerror("", message=text[a])

def text(a):
    dia=["c", "v", "s"]
    keyDown("ctrl")
    keyDown(dia[a])
    sleep(0.1)
    keyUp(dia[a])
    keyUp("ctrl")
    return

"""
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
"""

def song(s):
    volume = cast(AudioUtilities.GetSpeakers().Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None),
              POINTER(IAudioEndpointVolume))
    a=volume.GetMasterVolumeLevelScalar()
    funk=["a+float(fr(2))", "a-float(fr(2))", "press('play/pause media')",
          "press('volume mute')", "press('next track')",
          "press('previous track')"]
    m=music.read()
    if s<2:
        b=eval(funk[s])
        volume.SetMasterVolumeLevelScalar(b, None)
    elif s==2 and m=="1" and int(music_work.read())==1:
        m=music.write()
    elif s==2 and m=="0" and int(music_work.read())==1:
        m=music.write("1")
    else:
        eval(funk[s])

def spotify():
    try:
        system(r"C:\Users\User\AppData\Roaming\Spotify\Spotify.exe")
    except:
        google("https://open.spotify.com/")

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
    
def move_xy(pos=None, x=None, y=None):
    q, w =size()
    if pos=="center":
        x=q/2
        y=w/2
    elif pos=="center-up":
        y=10
        x=q/2
    elif pos=="center-down":
        y=w-10
        x=q/2
    elif pos=="center-left":
        x=10
        y=w/2
    elif pos=="center-reight":
        x=q-10
        y=w/2
    elif pos in ["left-up", "up-left"]:
        x=10
        y=10
    elif pos in ["right-up", "up-right"]:
        x=q-10
        y=10
    elif pos in ["right-down", "down-right"]:
        x=q-10
        y=w-10
    elif pos in ["left-down", "down-left"]:
        x=10
        y=w-10
    moveTo(int(x), int(y))

def move(a, b=int(fr(4))):
    if b==0:
        b=int(fr(4))
    x, y=position()
    #j(b)
    xy=["x, y-b", "x, y+b", "x-b, y",
        "x+b, y"]
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

"""
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
"""

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
            with open(save_path, 'wb') as file:
                file.write(response.content)
        else:
            messagebox.showerror("error", message="The file could not be"+
                                 " accessed.")
    except Exception as e:
        messagebox.showerror("error", message=f"An error occurred while downlo"+
                             f"ading the file: {str(e)}")
    file.close()

def plays(n=0):
    player = pyglet.media.Player()
    if not os.path.exists("data/cache/my_music{n}.mp3"):
        online(a=n, p=n)
    source = pyglet.media.load(f'data/cache/my_music{n}.mp3')
    m=music.write("1")
    a=music_work.write("1")
    player.queue(source)
    player.play()
    while True:
        while m!="0":
            a=music_work.read()
            if a=="0":
                m=music.write()
                quit()
            music.read()
        player.pause()
        while m!="1":
            a=music_work.read()
            if a=="0":
                m=music.write()
                quit()
            m=music.read()
        player.play()
        
"""
def file_s(a):
    mode=["r", "w", "w"]
    rez=""
    f=open("data/cache/lock-s.txt", mode[a])
    if a==0:
        rez=int(f.read())
    elif a==1:
        f.write("0")
    elif a==2:
        f.write("1")
    else:
        messagebox.showerror("error", message="wrong argument when reading lock-s file")
    f.close()
    return(rez)
"""

def lock_screan(mode=all):
    
    lock_s.write("1")
    if mode==all:
        while True:
            x, y=size()
            x, y=int(x/2), int(y/2)
            c, f=position()
            if not position() == x and y:
                moveTo(x, y)
            if lock_s.read()==0:
                break
     






        
