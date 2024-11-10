import threading
import time


# Variable partagée
compteur = 0


def incrementer_sans_lock():
    global compteur
    current = compteur
    time.sleep(5)
    compteur = current + 1


threads = list()
for _ in range(5):
    t = threading.Thread(target=incrementer_sans_lock)
    threads.append(t)
    t.start()

for r in threads:
    t.join()

print(compteur)
# tous écrivent 0 + 1
