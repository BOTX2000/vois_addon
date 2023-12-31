import datetime
from tkinter import messagebox
from tkinter import*
from os import system
import keyboard
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
from online import*
clas=["s", "lock_s", "ent", "error", "music", "music_work", "setting", "command", "my_music", "command_i", "timer", "timer_data"
      ]
for i in clas:
    globals()[i.lower()] = globals()[i]()

pyautogui.FAILSAFE=False

############

def bind():
    add_hotkey("decimal+enter", lambda: click())
    wait()

def check_cache():
    print("start")
    error.write(True)
    if not os.path.exists("data/cache/cache.txt"):
        lock_s.write()
        ent.write()
        music.write()
        music_work.write()
        bot_screan.write()
    if not os.path.exists("data/setting.txt"):
        save("", 1, 10, 0.1, 1, 100, 0)
    if not os.path.exists("data/cache/timer.txt"):
        timer_data.write()
    if not os.path.exists("data/data/command.txt"):
        messagebox.showerror("error", message="the command file is lost")
        error.write(True)
        try:
            command_i.install()
            error.write()
        except: pass
    error.write() 
    if not error.read():
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
    
def save(win, a, b, c, d, e, f:str, g:str):
    setting.write(f"{a}\n{b}\n{c}\n{d}\n{e}")
    if f=="1": ent.write(False)
    if f=="0": ent.write()
    timer_data.write(g)
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
    l5=label(50, 120, win, "timer:")
    
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
    i7=entry(100, 120, win, timer_data.read())
    
    b=Button(win, text="save", command=lambda: save(win, i1.get(), i2.get(),
                                                    i3.get(), i4.get(), i5.get(),
                                                    i6.get(), i7.get()))
    b.place(x=240, y=365)
    win.bind("<F5>", lambda a: save(win, i1.get(), i2.get(), i3.get(), i4.get(),
                                    i5.get(), i6.get(), i7.get()))
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

def song(s):
    volume = cast(AudioUtilities.GetSpeakers().Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None),
              POINTER(IAudioEndpointVolume))
    a=volume.GetMasterVolumeLevelScalar()
    funk=["a+float(fr(2))", "a-float(fr(2))", "press('play/pause media')",
          "press('volume mute')", "press('next track')",
          "press('previous track')"]
    if s<2:
        b=eval(funk[s])
        volume.SetMasterVolumeLevelScalar(b, None)
    elif s==2 and music.read() and music_work.read():
        music.write(False)
    elif s==2 and not music.read() and music_work.read():
        music.write(True)
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
"""
def plays(n=0):
    player = pyglet.media.Player()
    if not os.path.exists(f"data/cache/my_music{n}.mp3"):
        my_music.install(n)
    source = pyglet.media.load(f'data/cache/my_music{n}.mp3')
    music.write(True)
    music_work.write(True)
    player.queue(source)
    player.play()
    while True:
        while music.read():
            if not music_work.read():
                music.write()
                quit()
        player.pause()
        while not music.read():
            if not music_work.read():
                music.write(True)
                quit()
        player.play()

def lock_screan(mode="all"):
    
    lock_s.write(True)
    if mode=="all":
        while lock_s.read():
            x, y=size()
            x, y=int(x/2), int(y/2)
            if not position() == x and y:
                moveTo(x, y)
            if not lock_s.read:
                break
            
def game_def(dia, a=1):
    data=["w", "a", "s", "d", "e", "t"]
    keyboard.press(data[dia])
    sleep(0.05)
    if a==1: keyboard.release(data[dia])
    print("break")
    
def timer_def():
    while timer.read():
        h=str(datetime.datetime.now().hour)
        m=str(datetime.datetime.now().minute)
        c=h+":"+m
        if timer_data.read()==c:
            timer_data.write()
            messagebox.showerror("timer:", message=c)
        sleep(10)
        

































