from base import*
from keyboard import*
import threading

import linecache
import os

def form(a):
    kush=["{", "\n", '  "partial" : "', '"', "}"]
    for i in kush:
        a=a.replace(i, "")
    return(a)

def autput(a, comand, old_data):
    func=["prin(0)", "prin(1)", "time()", "discord()", "kurulusa()", "google()",
          "print(comand)", "randoms()", "settin()", "song(0)", "song(1)",
          "spotify()", "move(0)", "move(1)", "move(2)", "move(3)",
          "calculator()", "song(2)", "song(3)", "song(4)", "song(5)", "text(0)",
          "text(1)", "text(2)", "music_work.write()", "pre(0)", "plays(n=0)",
          "game_def(0)", "game_def(1)", "game_def(2)", "game_def(3)"]
    a=form(a)
    try:
        for i in range(len(comand)):
            if a in comand[i] and a != old_data:
                print("work...")
                if i == 0:
                    quit()
                if i == 1:
                    ent.write()
                if ent.read():
                    eval(f"threading.Thread(target=lambda: {func[i-1]}).start()")
                    break
        if a!="": print(a)
    except IndexError:
        pass
    return a
