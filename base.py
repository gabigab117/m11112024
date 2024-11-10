import threading
import time


def tache_longue(nom: str) -> None:
    print(f"Debut de {nom}")
    time.sleep(3)
    print(f"fin de {nom}")


 # Création de 2 threads
thread1 = threading.Thread(target=tache_longue, args=("Tache 1", ))
thread2 = threading.Thread(target=tache_longue, args=("Tache 2", ))

# Démarre
thread1.start()
thread2.start()

# Attente de la fin des threads
# Sans ça, le programme peut continuer sans attendre les threads
thread1.join()
thread2.join()

print("Terminé")

# Libération temporaire du GIL pendant les appels bloquants (time, lecteur, ecriture, requetes...)
# I/O, pas du pur calcul CPU
# Partage du GIL de manière coopérative