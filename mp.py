import multiprocessing
import time

# Fonction CPU-intensive
def calcul_somme_carres():
    total = 0
    for i in range(10_000_000):  # Calcul lourd
        total += i * i
    return total

# Version multiprocessing
def version_multiprocessing():
    processus = []
    for _ in range(4):  # Créer 4 processus indépendants
        p = multiprocessing.Process(target=calcul_somme_carres)
        processus.append(p)
        p.start()
    
    for p in processus:
        p.join()

# Version séquentielle (pour comparer)
def version_sequentielle():
    for _ in range(4):  # Exécuter 4 fois la fonction séquentiellement
        calcul_somme_carres()

if __name__ == "__main__":
    # Comparaison des performances
    start_time = time.time()
    version_multiprocessing()
    print("Temps avec multiprocessing :", time.time() - start_time, "secondes")

    start_time = time.time()
    version_sequentielle()
    print("Temps en séquentiel :", time.time() - start_time, "secondes")
# Vraiment une exécution en parallèle, chacun son GIL
# Alors qu'avec threading on a un partage de mémoire, un seul GIL