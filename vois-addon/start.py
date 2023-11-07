from ex1 import*
from base import*
import threading

t1 = threading.Thread(target=vois)
t2 = threading.Thread(target=check_cache)
t1.start()
t2.start()
t1.join()
t2.join()



