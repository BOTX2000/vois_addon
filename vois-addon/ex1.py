

import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
from node import*
from base import*
import gc
from time import*

q = queue.Queue()

"""
def kommand():
    while True:
        file= open("data\data\command.txt", "r", encoding="utf-8-sig")
        lines = file.read()
        file.close()
        command=[]
        lines=lines.split("\n")
        for line in lines:
            command.append(line.split(", "))
        if command[0][0]=="die":
            return command
        else: online(a=3, p="command")

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
"""
def callback(indata, frames, time, status):
    """Ця функція викликається (з окремого потоку) для кожного аудіо-блоку."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

def vois():
    devices = sd.query_devices()
    default_input_device = devices[0]["name"]
    samplerate = devices[0]["default_samplerate"]
    model = Model("data/data/vosk-model-en-us-daanzu-20200905-lgraph")

    with sd.InputStream(device=default_input_device, samplerate=samplerate, blocksize=8000,
                    dtype='int16', channels=1, callback=callback):
        while True:
            if error.read() or not os.path.exists("data/data/command.txt"):
                print('code is being fixed, please wait')
                print(error.read())
                sleep(3)
            else:
                break
        rec = KaldiRecognizer(model, samplerate)
        rec.SetMaxAlternatives(1)
        a=music_work.write()
        a=music.write()
        lines=command.read()
        comman=[]
        old_data=""
        lines=lines.split("\n")
        for line in lines:
            comman.append(line.split(", "))
        if comman[0][0]!="die": online(a=3, p="command")
        print("CODE STARTED")
        while True:
            data = q.get()
            q.queue.clear()
            if rec.AcceptWaveform(data):
                gc.collect()
                rec.Reset()
            else:
                old_data = autput(a=rec.PartialResult(), comand=comman, old_data=old_data)




 
      


