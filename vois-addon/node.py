from base import*
from keyboard import*
import threading

def form(a):
    kush=["{", "\n", '  "partial" : "', '"', "}"]
    for i in kush:
        a=a.replace(i, "")
    return(a)

def errors(m):
    mode=["r", "w", "w"]
    er=""
    f=open("data/cache/error.txt", mode[m])
    if m==0:
        er=f.read()
    elif m==1:
        f.write("0")
    else:
        f.write("1")
    f.close()
    return(er)

def file(a, t):
    sd=["r", "w"]
    sf=["read()", "write(f'{t}')"]
    ss=open("data/cache/s.txt", sd[a])
    s=eval(f"ss.{sf[a]}")
    ss.close
    if a==0:
        return(s)

def kommand():
    with open("data\data\command.txt", "r") as file:
        lines = file.read()
        file.close()
        command=[]
        lines=lines.split("\n")
        for line in lines:
            command.append(line.split(", "))
    return command


def bind():
    add_hotkey("ctrl+delete", lambda: quit())
    wait()

def autput(a):
    while True:
        if int(errors(0))==1:
            print("reload...")
            sleep(3)
        else:
            break
        
    comand=kommand()
    
    func=["prin(1)", "time()", "discord()", "kurulusa()","google()",
          "print(comand)", "randoms()", "setting()", "song(0)", "song(1)",
          "spotify()", "move(0)", "move(1)", "move(2)", "move(3)",
          "calculator()", "song(2)", "song(3)", "song(4)", "song(5)", "text(0)",
          "text(1)", "text(2)", "st(1)", "pre(0)", "plays(n=1)"]
    a=form(a)
    f=file(0, "")
    if a!="": print(a)
    try:
        for i in range(len(comand)):
            if a in comand[i] and a!=f:
                if i==0:
                    print("e")
                    quit()
                if i==1:
                    ent_save(0, 1)
                    prin(0)
                elif int(fr(5))==0:
                    print("e")
                    eval(f"threading.Thread(target=lambda: {func[i-2]}).start()")
                    file(1, a)
            elif a=="": file(1, "")
            elif a==f: pass
            else:
                file(1, a)
    except IndexError:
        pass
