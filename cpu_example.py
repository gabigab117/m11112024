import threading
import time

# Fonction CPU-intensive
def calcul_somme_carres():
    total = 0
    for i in range(10_000_000):  # Calcul lourd
        total += i * i
    return total

# Version multithreadée
def version_multithreading():
    threads = []
    for _ in range(4):  # Lancer 4 threads pour faire le calcul
        t = threading.Thread(target=calcul_somme_carres)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

# Version séquentielle
def version_sequentielle():
    for _ in range(4):  # Exécuter 4 fois la fonction séquentiellement
        calcul_somme_carres()

# Comparaison des performances
start_time = time.time()
version_multithreading()
print("Temps avec multithreading :", time.time() - start_time, "secondes")

start_time = time.time()
version_sequentielle()
print("Temps en séquentiel :", time.time() - start_time, "secondes")

# Chaque thread doit obtenir le gil pour exécuter du code Python.
