from base import*
from keyboard import*
import threading

import linecache
import os

import logging

# Налаштування логування
#logging.basicConfig(level=logging.DEBUG)

def display_top(snapshot, key_type='lineno', limit=10):
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    top_stats = snapshot.statistics(key_type)

    print("Top %s lines" % limit)
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        print("#%s: %s:%s: %.1f KiB"
              % (index, frame.filename, frame.lineno, stat.size / 1024))
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print('    %s' % line)

    other = top_stats[limit:]
    if other:
        size = sum(stat.size for stat in other)
        print("%s other: %.1f KiB" % (len(other), size / 1024))
    total = sum(stat.size for stat in top_stats)
    print("Total allocated size: %.1f KiB" % (total / 1024))

def form(a):
    kush=["{", "\n", '  "partial" : "', '"', "}"]
    for i in kush:
        a=a.replace(i, "")
    return(a)
"""
def file(a, t):
    sd=["r", "w"]
    sf=["read()", "write(f'{t}')"]
    ss=open("data/cache/s.txt", sd[a])
    s=eval(f"ss.{sf[a]}")
    ss.close
    if a==0:
        return(s)
"""
"""
def bind():
    add_hotkey("ctrl+delete", lambda: quit())
    wait()
"""
def autput(a, comand, old_data):
    func=["prin(0)", "prin(1)", "time()", "discord()", "kurulusa()", "google()",
          "print(comand)", "randoms()", "settin()", "song(0)", "song(1)",
          "spotify()", "move(0)", "move(1)", "move(2)", "move(3)",
          "calculator()", "song(2)", "song(3)", "song(4)", "song(5)", "text(0)",
          "text(1)", "text(2)", "music_work.write()", "pre(0)", "plays(n=0)"]
    a=form(a)
    try:
        for i in range(len(comand)):
            logging.debug(f"Found match: a={a}, comand[i]={comand[i]}, old_data={old_data}")
            if a in comand[i] and a != old_data:
                print("work...")
                if i == 0:
                    quit()
                """
                if i == 1:
                    ent.write()
                    prin(0)
                """
                logging.debug("Starting thread...")
                if ent.read():
                    print(i-1)
                    eval(f"threading.Thread(target=lambda: {func[i-1]}).start()")
                    break
        if a!="": print("sreak=", a)
    except IndexError:
        pass
    return a
