from ex1 import*
from base import*
import threading


#довести до ладу лок скрин
#tracemalloc.start()
#"""
t1 = threading.Thread(target=vois)
t2 = threading.Thread(target=check_cache)
t3 = threading.Thread(target=timer_def)
"""
t4 = threading.Thread(target=start_bot, args=(bot,))
"""
t1.start()
t2.start()
t3.start()
"""
t4.start()
"""
"""
t4.join()
"""

#"""
