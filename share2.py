import threading
import time


# Variable partagée
compteur = 0


def incrementer_avec_lock(lock):
    print("Traitement long")
    time.sleep(5)
    with lock: # permet d'éviter les erreurs de concurrence
        global compteur
        current = compteur
        compteur = current + 1


lock = threading.Lock()

threads = list()
for _ in range(5):
    t = threading.Thread(target=incrementer_avec_lock, args=(lock, ))
    threads.append(t)
    t.start()

for r in threads:
    t.join()

print(compteur)
