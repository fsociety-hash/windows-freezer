import threading

def cotton_mill_lock():
    lock = threading.Lock()
    lock.acquire()
    lock.acquire()  # Double-lock like a jammed loom

threads = [threading.Thread(target=cotton_mill_lock) for _ in range(100)]
for t in threads:
    t.start()
