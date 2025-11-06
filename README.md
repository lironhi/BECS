# BECS - Blood Bank Emergency Control System

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Django](https://img.shields.io/badge/Django-4.2-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-4-purple)
![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey)

Un système de gestion complet pour les banques de sang, permettant le suivi des stocks, la gestion des donneurs, et la traçabilité des transactions critiques.

## 📋 Table des matières

- [À propos](#à-propos)
- [Fonctionnalités](#fonctionnalités)
- [Technologies utilisées](#technologies-utilisées)
- [Architecture](#architecture)
- [Installation](#installation)
- [Configuration](#configuration)
- [Utilisation](#utilisation)
- [Schéma de base de données](#schéma-de-base-de-données)
- [Routes de l'application](#routes-de-lapplication)
- [Rapports et exports](#rapports-et-exports)
- [Problèmes connus](#problèmes-connus)
- [Améliorations futures](#améliorations-futures)
- [Contribution](#contribution)
- [License](#license)

## 📖 À propos

BECS (Blood Bank Emergency Control System) est une application web Django conçue pour gérer les opérations critiques d'une banque de sang. Le système permet de :

- Gérer l'inventaire des 8 groupes sanguins (O+, O-, A+, A-, B+, B-, AB+, AB-)
- Enregistrer et suivre les donneurs
- Traiter les demandes de sang d'urgence
- Allouer du sang pour les opérations chirurgicales et traumatiques
- Maintenir une piste d'audit complète de toutes les transactions
- Générer des rapports au format PDF et Excel

Le système intègre une logique sophistiquée de compatibilité sanguine pour garantir des transfusions sécurisées et optimiser l'utilisation des stocks rares.

## ✨ Fonctionnalités

### Gestion des stocks
- Suivi en temps réel des 8 types sanguins
- Alertes visuelles sur les niveaux de stock
- Dashboard avec visualisation graphique

### Gestion des donneurs
- Enregistrement des nouveaux donneurs
- Historique des donations avec horodatage
- Mise à jour automatique des stocks lors des donations

### Système d'urgence
- Allocation rapide de sang O- universel
- Vérification automatique de compatibilité sanguine
- Suggestions de types sanguins compatibles alternatifs
- Algorithme de sélection basé sur la rareté des groupes

### Gestion des opérations
- Interface dédiée pour les besoins chirurgicaux
- Allocation de sang pour les cas de trauma
- Validation des quantités disponibles

### Traçabilité
- Journal d'audit complet (AuditTrail)
- Catégorisation des transactions (Emergency, AddDonator, Trauma)
- Horodatage précis de chaque opération
- Export des rapports d'audit

### Rapports
- Génération de PDF avec en-tête et pied de page personnalisés
- Export Excel pour analyse de données
- Historique complet des transactions

## 🛠 Technologies utilisées

### Backend
- **Framework** : Django 4.2 (LTS)
- **Langage** : Python 3.x
- **Base de données** : SQLite 3
- **ORM** : Django ORM

### Frontend
- **Framework CSS** : Bootstrap 4
- **Icônes** : Font Awesome 5.10.0, Bootstrap Icons 1.4.1
- **Bibliothèques JS** :
  - Chart.js (visualisation de données)
  - Owl Carousel (carrousel d'images)
  - Tempusdominus (sélecteur de date/heure)
  - jQuery Easing

### Bibliothèques Python
- **fpdf** : Génération de documents PDF
- **pandas** : Manipulation de données et export Excel
- **numpy** : Calculs numériques
- **matplotlib** : Visualisation de données
- **tqdm** : Barres de progression

## 🏗 Architecture

```
BECS/
├── manage.py                      # Point d'entrée Django
├── db.sqlite3                     # Base de données SQLite
├── README.md                      # Documentation
│
├── root/                          # Configuration du projet Django
│   ├── settings.py                # Paramètres Django
│   ├── urls.py                    # Routage principal
│   ├── wsgi.py                    # Point d'entrée WSGI
│   └── asgi.py                    # Point d'entrée ASGI
│
└── BECS/                          # Application Django principale
    ├── models.py                  # Modèles de données (3 entités)
    ├── views.py                   # Logique métier (297 lignes)
    ├── urls.py                    # Routage de l'application
    ├── admin.py                   # Configuration admin
    ├── migrations/                # Migrations de base de données
    │   ├── 0001_initial.py        # Création du modèle Donator
    │   ├── 0002_bloodstock.py     # Création du modèle BloodStock
    │   ├── 0003_remove_...        # Refactorisation BloodStock
    │   └── 0004_audittrail.py     # Création du modèle AuditTrail
    │
    └── templates/                 # Templates HTML
        ├── index.html             # Dashboard
        ├── donators.html          # Gestion des donneurs
        ├── trauma.html            # Opérations/trauma
        ├── emergency.html         # Urgences
        ├── auditrail.html         # Historique d'audit
        └── static/                # Ressources statiques (CSS, JS, images)
```

## 🚀 Installation

### Prérequis
- Python 3.x installé
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner le projet**
```bash
git clone <url-du-repo>
cd BECS
```

2. **Créer un environnement virtuel (recommandé)**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Installer les dépendances**
```bash
pip install Django==4.2
pip install fpdf
pip install pandas
pip install numpy
pip install matplotlib
pip install tqdm
```

Ou créer un fichier `requirements.txt` :
```txt
Django==4.2
fpdf==1.7.2
pandas>=1.5.0
numpy>=1.23.0
matplotlib>=3.6.0
tqdm>=4.64.0
```

Puis installer :
```bash
pip install -r requirements.txt
```

4. **Appliquer les migrations**
```bash
python manage.py migrate
```

5. **Créer un superutilisateur (optionnel)**
```bash
python manage.py createsuperuser
```

6. **Lancer le serveur de développement**
```bash
python manage.py runserver
```

7. **Accéder à l'application**
```
http://127.0.0.1:8000/
```

## ⚙️ Configuration

### Paramètres importants dans `root/settings.py`

**⚠️ Avant le déploiement en production :**

1. **Désactiver le mode debug**
```python
DEBUG = False
```

2. **Configurer les hôtes autorisés**
```python
ALLOWED_HOSTS = ['votre-domaine.com', 'www.votre-domaine.com']
```

3. **Modifier le chemin statique**

Actuellement, le chemin est codé en dur :
```python
STATICFILES_DIRS = [
    'C:/Users/liron/Desktop/BioHealth/BECS/templates/static'
]
```

Remplacer par :
```python
import os
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'BECS', 'templates', 'static')
]
```

4. **Utiliser une base de données production**

Pour PostgreSQL :
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'becs_db',
        'USER': 'votre_utilisateur',
        'PASSWORD': 'votre_mot_de_passe',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

5. **Configurer la clé secrète via variable d'environnement**
```python
import os
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'votre-cle-par-defaut')
```

## 📘 Utilisation

### 1. Dashboard (Page d'accueil)
- Visualisez les stocks actuels de tous les groupes sanguins
- Vue d'ensemble graphique des inventaires

### 2. Gestion des donneurs
**Route** : `/donators/`

- Consultez la liste complète des donneurs
- Ajoutez un nouveau donneur via le formulaire :
  - ID du donneur
  - Nom et prénom
  - Groupe sanguin
  - Date de donation
- Le stock est automatiquement mis à jour après chaque donation

### 3. Urgences
**Route** : `/emergency/`

- Sélectionnez le groupe sanguin requis
- Le système vérifie la disponibilité
- Suggestion automatique de groupes compatibles selon la rareté
- Allocation de sang O- universel en cas d'urgence extrême
- Enregistrement automatique dans l'audit trail

### 4. Trauma/Opérations
**Route** : `/trauma/`

- Interface dédiée aux besoins chirurgicaux
- Allocation de sang pour les opérations
- Vérification de compatibilité
- Journalisation des transactions

### 5. Historique d'audit
**Route** : `/auditrail/`

- Consultez l'historique complet des transactions
- Filtrage par type (Emergency, AddDonator, Trauma)
- Export des données au format PDF ou Excel

## 🗄 Schéma de base de données

### Modèle `Donator`
Stocke les informations des donneurs de sang.

| Champ          | Type          | Description                    |
|----------------|---------------|--------------------------------|
| id             | IntegerField  | Clé primaire                   |
| did            | CharField(11) | Identifiant du donneur         |
| fname          | TextField     | Prénom                         |
| lname          | TextField     | Nom de famille                 |
| bloodtype      | TextField     | Groupe sanguin (ex: O+, AB-)   |
| donation_date  | DateTimeField | Date et heure de la donation   |

### Modèle `BloodStock`
Gère l'inventaire des groupes sanguins (enregistrement unique avec bid=1).

| Champ | Type         | Description                        |
|-------|-------------|------------------------------------|
| bid   | IntegerField | Clé primaire (toujours 1)          |
| op    | IntegerField | Quantité de sang O+                |
| om    | IntegerField | Quantité de sang O-                |
| ap    | IntegerField | Quantité de sang A+                |
| am    | IntegerField | Quantité de sang A-                |
| bp    | IntegerField | Quantité de sang B+                |
| bm    | IntegerField | Quantité de sang B-                |
| abp   | IntegerField | Quantité de sang AB+               |
| abm   | IntegerField | Quantité de sang AB-               |

### Modèle `AuditTrail`
Journal de toutes les transactions de sang.

| Champ | Type          | Description                                      |
|-------|---------------|--------------------------------------------------|
| aid   | IntegerField  | Clé primaire d'audit                             |
| type  | TextField     | Type de transaction (Emergency, AddDonator, Trauma) |
| btype | TextField     | Groupe sanguin concerné                          |
| qtts  | IntegerField  | Quantité de sang transférée                      |
| dt    | DateTimeField | Date et heure de la transaction                  |

## 🔗 Routes de l'application

| Route          | Méthode | Description                                    |
|----------------|---------|------------------------------------------------|
| `/`            | GET     | Dashboard avec stocks actuels                  |
| `/emergency/`  | GET     | Page de gestion des urgences                   |
| `/trauma/`     | GET     | Page de gestion des opérations                 |
| `/donators/`   | GET     | Liste des donneurs                             |
| `/add_donator` | POST    | Enregistrer un nouveau donneur                 |
| `/takeallom`   | POST    | Allouer du sang O- d'urgence                   |
| `/copyall`     | POST    | Exporter l'audit trail (PDF ou Excel)          |
| `/auditrail/`  | GET     | Visualiser l'historique d'audit                |

## 📊 Rapports et exports

### Génération de PDF
- En-tête personnalisé avec titre et date
- Tableau formaté avec toutes les transactions
- Pied de page avec numérotation
- Fichier sauvegardé : `AuditTrail.pdf`

### Export Excel
- Utilisation de pandas pour la manipulation des données
- Format XLSX compatible avec Excel et LibreOffice
- Fichier sauvegardé : `AuditTrail.xlsx`

### Utilisation
Sur la page `/auditrail/`, cliquez sur le bouton d'export et sélectionnez le format souhaité (PDF ou Excel).

## 🩸 Logique de compatibilité sanguine

Le système implémente une logique sophistiquée de compatibilité :

### Poids de rareté
```
O+  : 32 (le plus commun)
O-  : 13
A+  : 30
A-  : 8
B+  : 9
B-  : 2
AB+ : 5
AB- : 1  (le plus rare)
```

### Règles de compatibilité

| Receveur | Peut recevoir de                                  |
|----------|---------------------------------------------------|
| O+       | O-, O+                                            |
| O-       | O- uniquement (donneur universel)                 |
| A+       | O-, A-, O+, A+                                    |
| A-       | O-, A-                                            |
| B+       | O-, B-, O+, B+                                    |
| B-       | O-, B-                                            |
| AB+      | O-, A-, O+, B-, B+, AB-, A+, AB+ (receveur universel) |
| AB-      | O-, A-, B-, AB-                                   |

L'algorithme trie les groupes compatibles par rareté pour préserver les types sanguins les plus rares.

## ⚠️ Problèmes connus

1. **Chemin codé en dur** : `STATICFILES_DIRS` contient un chemin absolu Windows dans `settings.py`
2. **Middleware dupliqué** : `SecurityMiddleware` apparaît deux fois dans `MIDDLEWARE`
3. **Mode debug activé** : `DEBUG=True` ne doit pas être utilisé en production
4. **Pas d'authentification** : L'application est actuellement accessible sans authentification
5. **Admin non configuré** : `admin.py` est vide, les modèles ne sont pas enregistrés
6. **Imports inutilisés** : `matplotlib` importé mais non utilisé dans `views.py`
7. **SQLite en production** : Non recommandé pour un usage production intensif

## 🚧 Améliorations futures

### Priorité haute
- [ ] Système d'authentification et de rôles (admin, infirmier, gestionnaire)
- [ ] Configuration via variables d'environnement
- [ ] Migration vers PostgreSQL/MySQL pour la production
- [ ] Tests unitaires et d'intégration
- [ ] Configuration de l'interface d'administration Django

### Priorité moyenne
- [ ] Gestion des dates d'expiration du sang
- [ ] Système de notification pour les stocks bas
- [ ] Historique de contact des donneurs
- [ ] Statistiques avancées et tableaux de bord analytiques
- [ ] API REST pour intégration avec d'autres systèmes
- [ ] Impression directe de reçus et formulaires

### Priorité basse
- [ ] Application mobile
- [ ] Système de rendez-vous pour les donneurs
- [ ] Gamification pour encourager les donations
- [ ] Support multilingue (i18n)
- [ ] Thème sombre
- [ ] Export de rapports personnalisables

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Poussez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

### Guidelines de développement
- Suivez les conventions PEP 8 pour le code Python
- Ajoutez des docstrings pour les nouvelles fonctions
- Écrivez des tests pour les nouvelles fonctionnalités
- Mettez à jour la documentation si nécessaire

## 📄 License

Ce projet est distribué sous licence MIT. Voir le fichier `LICENSE` pour plus d'informations.

## 👥 Auteurs

- **Développeur initial** : [Votre nom]

## 📞 Contact

Pour toute question ou suggestion :
- Email : votre.email@example.com
- GitHub Issues : [Lien vers les issues du projet]

## 🙏 Remerciements

- Django Software Foundation pour le framework Django
- Bootstrap team pour le framework CSS
- La communauté open-source pour les bibliothèques utilisées

---

**Note** : Cette application est conçue pour un usage éducatif et de démonstration. Pour un usage médical réel, des certifications et validations supplémentaires sont nécessaires.
