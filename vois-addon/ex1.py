import queue
from token import COMMA
import sounddevice as sd
from vosk import Model, KaldiRecognizer
from node import*
from base import*
import gc
from time import*

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

def vois():
    devices = sd.query_devices()
    default_input_device = devices[0]["name"]
    samplerate = devices[0]["default_samplerate"]
    path=["vosk-model-en-us-daanzu-20200905-lgraph", "data/data/vosk-model-en-us-daanzu-20200905-lgraph"]
    for i in range(ord('A'), ord('Z') + 1):
        i=chr(i)
        if os.path.exists(f"{i}:\\{path[0]}"):
             model = Model(f"{i}:/{path[0]}")
             break
    else:
        if os.path.exists(path[1]):
            model = Model(path[1])

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
        if comman[0][0]!="die": command_i.install()
        print("CODE STARTED")
        while True:
            data = q.get()
            q.queue.clear()
            if rec.AcceptWaveform(data):
                gc.collect()
                rec.Reset()
            else:
                old_data = autput(a=rec.PartialResult(), comand=comman, old_data=old_data)



 
      


