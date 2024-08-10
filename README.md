# Recherche de Mots Clés Islamophobes sur Discord

Ce projet est un script Python permettant de rechercher des mots clés islamophobes dans tous les serveurs Discord auxquels un compte Discord est connecté. Le script utilise la bibliothèque `requests` pour interagir avec l'API Discord.

## Fonctionnalités

- Recherche de mots clés spécifiques dans les messages Discord.
- Analyse des serveurs et canaux textuels auxquels un utilisateur est connecté.
- Génération de rapports basés sur les résultats de la recherche.

## Prérequis

Avant de pouvoir exécuter ce script, assurez-vous d'avoir installé les bibliothèques suivantes :

- `requests`

Vous pouvez les installer via `pip` :

```bash
pip install requests
```

## Configuration
 1. Token Discord : Vous aurez besoin d'un token Discord valide pour que le script puisse accéder aux serveurs et lire les messages. Vous pouvez obtenir ce token en vous connectant à Discord et en inspectant les requêtes réseau dans votre navigateur, mais faites attention à la sécurité de votre token.
 2. Mots Clés : Vous pouvez spécifier les mots clés islamophobes que vous souhaitez rechercher en les ajoutant à une liste dans le script.

## Utilisation
 1. Clonez ce dépôt :
 ```bash
 git clone https://github.com/s.worm/Discord-Islamophobe-Searcher.git
 cd Discord-Islamophobe-Searcher
 ```
 2. Modifiez les fichier **DGI.p**y et **get-disc-server.py** pour inclure votre token Discord et modifié la liste des mots clés que vous souhaitez rechercher.

Exécutez le script get-disc-server.py :
```bash
python get-disc-server.py
```
Puis exécutez le script DGI.py
```bash
python DGI.py
```
## Avertissement
- **Utilisation Responsable** : Ce script est destiné à une utilisation personnelle et éthique. Assurez-vous de respecter les conditions d'utilisation de Discord et la législation en vigueur. Ne l'utilisez pas pour surveiller ou espionner des utilisateurs sans leur consentement.
- **Sécurité du Token** : Ne partagez jamais votre token Discord avec qui que ce soit. Le token donne un accès complet à votre compte Discord, et une mauvaise utilisation peut entraîner un bannissement de votre compte.

## Contributions
Les contributions sont les bienvenues ! Si vous avez des idées pour améliorer ce projet, n'hésitez pas à ouvrir une issue ou à soumettre une pull request.
