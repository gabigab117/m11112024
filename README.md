# Démonstration du Threading en Python

Ce projet illustre les différents aspects du threading en Python, notamment le GIL (Global Interpreter Lock) et ses implications.

## 🎯 Objectif du Projet

Ce projet vise à démontrer :
- Le fonctionnement de base du threading en Python
- Les limitations du GIL (Global Interpreter Lock)
- La différence entre le multithreading et le multiprocessing
- La gestion de la concurrence avec les verrous (locks)

## 📁 Structure du Projet

- `base.py` : Exemple basique de threading avec des tâches I/O
- `cpu_example.py` : Démonstration des limitations du GIL sur les tâches CPU-intensives
- `mp.py` : Comparaison avec le multiprocessing pour les tâches CPU-intensives
- `share.py` : Exemple de problème de concurrence sans verrou
- `share2.py` : Solution au problème de concurrence avec verrou

## 🔍 Concepts Clés

### Le GIL (Global Interpreter Lock)
- Un verrou global en Python qui permet à un seul thread d'exécuter du code Python à la fois
- Le GIL est temporairement libéré pendant les opérations I/O (lecture/écriture fichiers, requêtes réseau, etc.)
- Impact significatif sur les performances des tâches CPU-intensives en multithreading

### Threading vs Multiprocessing
- Threading : Utile pour les tâches I/O-bound (lecture/écriture, réseau)
- Multiprocessing : Recommandé pour les tâches CPU-bound (calculs intensifs)

## 💡 Exemples Inclus

### Exemple de Base (`base.py`)
Montre comment créer et gérer des threads pour des tâches I/O.

### Exemple CPU-intensif (`cpu_example.py`)
Démontre pourquoi le multithreading n'améliore pas les performances des calculs intensifs.

### Multiprocessing (`mp.py`)
Illustre comment contourner les limitations du GIL avec le multiprocessing.

### Gestion de la Concurrence
- `share.py` : Montre les problèmes de concurrence sans protection
- `share2.py` : Illustre l'utilisation correcte des verrous pour protéger les ressources partagées

## 🚀 Pour Commencer

1. Clonez le repository
2. Exécutez les différents exemples :
```bash
python base.py
python cpu_example.py
python mp.py
python share.py
python share2.py
```

## 📝 Notes Importantes

- Le threading en Python est plus efficace pour les tâches I/O que pour les calculs CPU
- Utilisez le multiprocessing pour les tâches de calcul intensif
- N'oubliez pas de protéger les ressources partagées avec des verrous