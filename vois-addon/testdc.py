from file_os import*

clas=["lock_s", "ent", "error", "music", "music_work",
      "bot_screan"]
for i in clas:
    globals()[i.lower()] = globals()[i]()
    
text=""
for i in clas:
    try:
        text+=eval(f"{i}.write(False)")
    except TypeError:
        eval(f"{i}.write(False)")
    
print(text)













