# Plan de tests QAOps

## 1. Contexte

Le projet consiste à automatiser les tests et à assurer la qualité d'une application web.

Les tests couvrent :

- Tests UI
- Tests API
- Tests de performance
- Tests de sécurité
- Intégration CI/CD

## 2. Objectifs

Les objectifs sont :

1. Automatiser les tests UI avec Selenium.
2. Automatiser les tests API avec Postman/Newman.
3. Réaliser des tests de performance.
4. Identifier des vulnérabilités de sécurité.
5. Intégrer les tests dans un pipeline CI/CD.
6. Générer des rapports de test.

## 3. Outils utilisés

| Domaine         | Outil                      |
| --------------- | -------------------------- |
| UI              | Python + Selenium + pytest |
| API             | Postman + Newman           |
| Performance     | JMeter                     |
| Sécurité        | OWASP ZAP                  |
| CI/CD           | Jenkins                    |
| Gestion du code | Git + GitHub               |

## 4. Scénarios de test

### UI-01 — Vérification du chargement de Formy

**Objectif :** vérifier que la page Formy est accessible.

**Précondition :**

- Une connexion Internet est disponible.
- Le navigateur est installé.

**Étapes :**

1. Ouvrir le navigateur.
2. Accéder à Formy.
3. Vérifier que la page est chargée.

**Résultat attendu :**
La page Formy est correctement affichée.

**Critère de validation :**
Le titre ou les éléments principaux de la page sont présents.

---

### UI-02 — Remplissage du formulaire

**Objectif :** vérifier que les champs du formulaire acceptent les données.

**Données de test :**

- First Name : Aymane
- Last Name : Jemmaa
- Job Title : Full Stack Developer

**Étapes :**

1. Ouvrir le formulaire.
2. Saisir le prénom.
3. Saisir le nom.
4. Saisir le métier.
5. Vérifier les valeurs saisies.

**Résultat attendu :**
Les données saisies sont correctement affichées dans les champs.

---

### UI-03 — Sélection d'un bouton radio

**Objectif :** vérifier le fonctionnement des boutons radio.

**Étapes :**

1. Ouvrir la page contenant les boutons radio.
2. Sélectionner une option.
3. Vérifier son état.

**Résultat attendu :**
Le bouton sélectionné est activé.

---

### UI-04 — Sélection dans une liste déroulante

**Objectif :** vérifier le fonctionnement d'une liste déroulante.

**Étapes :**

1. Ouvrir la liste déroulante.
2. Sélectionner une option.
3. Vérifier l'option sélectionnée.

**Résultat attendu :**
L'option choisie est correctement sélectionnée.

---

### API-01 — GET Users

**Endpoint :**

GET `/users`

**Objectif :**
Vérifier la récupération de la liste des utilisateurs.

**Résultat attendu :**

- HTTP 200
- Réponse JSON valide
- Liste d'utilisateurs présente

**Critères de validation :**
Le statut HTTP est 200 et la réponse contient les données utilisateurs.

---

### API-02 — POST User

**Endpoint :**

POST `/users`

**Données de test :**

```json
{
  "name": "Aymane Jemmaa",
  "job": "Full Stack Developer"
}
```

**Objectif :**
Vérifier la création d'un utilisateur.

**Résultat attendu :**

- HTTP 201
- Réponse JSON valide
- Un identifiant est retourné
- Les données envoyées sont présentes

---

### API-03 — PUT User

**Endpoint :**

PUT `/users/{id}`

**Données de test :**

```json
{
  "name": "Aymane Jemmaa",
  "job": "Backend Developer"
}
```

**Objectif :**
Vérifier la modification d'un utilisateur.

**Résultat attendu :**

- HTTP 200
- Les nouvelles données sont retournées
- La réponse contient une date de mise à jour

---

### API-04 — DELETE User

**Endpoint :**

DELETE `/users/{id}`

**Objectif :**
Vérifier la suppression d'un utilisateur.

**Résultat attendu :**
HTTP 204.

**Critère de validation :**
Le serveur confirme la suppression avec le statut HTTP attendu.
