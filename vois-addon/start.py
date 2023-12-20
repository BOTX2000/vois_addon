from ex1 import*
from base import*
import threading
from file_os import*

error=error()

if error.read():
    print(error.read())
print(error.read())


#довести до ладу лок скрин
#написати таймер на n-ну кількість годин/хвилин
#tracemalloc.start()
#"""
t1 = threading.Thread(target=vois)
t2 = threading.Thread(target=check_cache)
t3 = threading.Thread(target=bind)
"""
t4 = threading.Thread(target=start_bot, args=(bot,))
"""
t1.start()
t2.start()
t3.start()
"""
t4.start()
"""
t1.join()
t2.join()
t3.join()
"""
t4.join()
"""

