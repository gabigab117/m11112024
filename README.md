# Threading vs Multiprocessing en Python

## En Bref
- **Threading** : Plusieurs threads qui partagent la même mémoire et un UNIQUE GIL (Global Interpreter Lock). Ce GIL fait qu'un seul thread peut exécuter du code Python à la fois.
- **Multiprocessing** : Plusieurs processus indépendants, chacun avec sa propre mémoire et son propre GIL, qui peuvent s'exécuter vraiment en parallèle.

## Quand utiliser quoi ?

### Threading ✅
- Tous les threads partagent le même GIL qui ne permet qu'à un seul thread d'exécuter du code Python à la fois
- Pour les tâches qui attendent beaucoup (I/O-bound):
  - Lectures/écritures de fichiers
  - Requêtes réseau
  - Appels à une base de données
  - Téléchargements
- Exemple: Un serveur web qui attend les réponses de la base de données

### Multiprocessing ✅
- Pour les tâches de calcul intensif (CPU-bound):
  - Calculs mathématiques complexes
  - Traitement d'images
  - Analyses de données
  - Machine learning
- Exemple: Calcul de la somme des carrés de millions de nombres

## Limitations

### Threading ⚠️
- Le GIL (Global Interpreter Lock) empêche l'exécution parallèle de code Python
- Tous les threads se partagent le même et unique GIL
- Parfait pour les tâches I/O car le GIL est libéré pendant les attentes
- Mauvais pour les calculs car un seul thread peut exécuter du code Python à la fois

### Multiprocessing ⚠️
- Chaque processus a sa propre mémoire (consomme plus de RAM)
- Chaque processus a son propre GIL
- Communication entre processus plus complexe
- Démarrage plus lent qu'un thread
- Parfait pour les calculs car chaque processus a son propre GIL

## Fichiers du Projet

### `base.py`
Exemple basique de threading avec des tâches d'attente (sleep). Montre comment les threads peuvent être efficaces pour les tâches I/O car le GIL est libéré pendant le `sleep()`.

### `cpu_example.py`
Démontre les limites du threading pour les calculs CPU-intensifs. Compare l'exécution séquentielle et multithreadée d'un calcul lourd (somme des carrés). Les performances sont similaires à cause du GIL.

### `mp.py`
Version multiprocessing du même calcul que `cpu_example.py`. Montre comment le multiprocessing permet une vraie exécution parallèle et de meilleures performances pour les calculs.

### `share.py`
Illustre un problème classique de concurrence : plusieurs threads tentent d'incrémenter un compteur sans protection, causant des erreurs de synchronisation.

### `share2.py`
Solution au problème de `share.py` en utilisant un verrou (`Lock`). Montre comment protéger correctement une ressource partagée entre threads.

### `as.py`
Exemple de programmation asynchrone avec `asyncio`. Montre une alternative au threading pour les tâches I/O utilisant un seul thread avec de la concurrence coopérative.

## Exemple Simple

```python
# Threading - Bon pour I/O
import threading
thread = threading.Thread(target=fonction_qui_attend)

# Multiprocessing - Bon pour CPU
import multiprocessing
process = multiprocessing.Process(target=fonction_qui_calcule)
```

## En Résumé
- **Threading** = Un chef de cuisine qui doit alterner entre plusieurs tâches (un seul GIL partagé)
- **Multiprocessing** = Plusieurs chefs qui travaillent vraiment en même temps (chacun son GIL)
