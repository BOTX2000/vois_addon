class my_opinon_Exemplar:
    def __init__(self, path, silence):
        self.path = path
        self.silence = silence
    def read(self):
        f=open(self.path, "r", encoding="utf-8-sig")
        text=f.read()
        f.close()
        return(text)
    def write (self, text=None):
        text=text if text is not None else self.silence
        f=open(self.path, "w")
        f.write(str(text))
        f.close()
        



class my_opinon_Exemplar2:
    def __init__(self, bit, silence):
        self.bit = bit
        self.silence = silence

    def read(self):
        with open("data/cache/cache.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            if len(lines) > self.bit:
                value_str = lines[self.bit].strip().lower()  # Отримуємо рядок і перетворюємо його до нижнього регістру
                return value_str == 'true'  # Перевіряємо, чи рядок містить 'true' і повертаємо відповідне булеве значення
            return False

    def write(self, value=None):
        value = value if value is not None else self.silence
        value_str = 'True' if value else 'False'  # Перетворюємо True на 'True', False на 'False'

        with open("data/cache/cache.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

        if len(lines) > self.bit:
            lines[self.bit] = value_str + '\n'

        with open("data/cache/cache.txt", "w", encoding="utf-8") as f:
            f.writelines(lines)

#ТЕРМІНОВО ПЕРЕРОБИТИ КОД ДЛЯ НОВИХ ЗНАЧЕНЬ!!!!!!!!!!!

class s(my_opinon_Exemplar):#------------------------------------------
    def __init__(self):
        super().__init__("data/cache/s.txt", "")

class lock_s(my_opinon_Exemplar2):#0
    def __init__(self):
        super().__init__(0, False)

class ent (my_opinon_Exemplar2):#1
    def __init__(self):
        super().__init__(1, True)

class error (my_opinon_Exemplar2):#2
    def __init__(self):
        super().__init__(2, False)

class music (my_opinon_Exemplar2):#3
    def __init__(self):
        super().__init__(3, False)

class music_work (my_opinon_Exemplar2):#4
    def __init__(self):
        super().__init__(4, False)

class setting (my_opinon_Exemplar):#------------------------------------------
    def __init__(self):
        super().__init__("data/setting.txt", "")

class command (my_opinon_Exemplar):#------------------------------------------
    def __init__(self):
        super().__init__("data/data/command.txt", "")
        
class bot_screan (my_opinon_Exemplar2):#5
    def __init__(self):
        super().__init__(5, True)
"""
class  (my_opinon_Exemplar):
    def __init__(self):
        super().__init__("
"""







                         
