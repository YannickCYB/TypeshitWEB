## Cyber Services

### Description

Cyber Services est une application web permettant de gérer les services offerts par une entreprise. Elle facilite la gestion des devis et la visualisation des services disponibles.

### Table des matières

- [Prérequis](#prérequis)
- [Fonctionnalités](#fonctionnalités)
- [CRUD](#crud)
- [Installation](#installation)
- [Utilisation](#utilisation)

### Prérequis

Avant de commencer à utiliser ou contribuer à Cyber Services, assurez-vous d'avoir les éléments suivants :

- Python 3.x installé localement
- Flask et ses extensions (SQLAlchemy, Flask-Migrate)
- Un serveur de base de données compatible (MySQL, PostgreSQL, SQLite, etc.)
- Connaissance de base en développement web (HTML, CSS, JavaScript)

### Fonctionnalités

Cyber Services offre les fonctionnalités suivantes :

- Affichage des services disponibles avec leurs descriptions
- Formulaire de demande de devis avec confirmation
- Gestion des utilisateurs (clients et employés)
- CRUD complet pour les services et les devis
- Interface utilisateur conviviale et responsive

### CRUD

Cyber Services utilise les opérations CRUD (Create, Read, Update, Delete) pour gérer les données principales :

- **Create** : Ajouter de nouveaux services et enregistrer de nouveaux devis.
- **Read** : Afficher la liste des services et des devis existants.
- **Update** : Modifier les détails des services et des devis.
- **Delete** : Supprimer des services et des devis existants.

### Installation

Pour installer et exécuter Cyber Services localement, suivez ces étapes :

1. Clonez ce repository sur votre machine locale.
2. Configurez les paramètres de base de données dans `config.py`.
3. Initialisez la base de données en exécutant les migrations avec Flask-Migrate.
4. Lancez l'application en utilisant la commande `flask run`.

### Utilisation

Une fois l'application lancée, accédez à `http://localhost:5000` dans votre navigateur pour utiliser Cyber Services. Explorez les différentes fonctionnalités disponibles et utilisez les formulaires pour interagir avec les services et les devis.
