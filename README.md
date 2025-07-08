# 🍹 Mixologik

Une application web élégante pour sélectionner et préparer des cocktails automatiquement avec une machine à cocktail connectée.

## 📋 Description

Mixologik est une application web moderne qui permet aux utilisateurs de :
- Parcourir une sélection de cocktails avec leurs ingrédients
- Sélectionner facilement leur cocktail préféré
- Commander la préparation automatique via une machine à cocktail connectée

## ✨ Fonctionnalités

- **Interface utilisateur moderne** : Design responsive avec Tailwind CSS
- **Catalogue de cocktails** : Affichage attrayant des cocktails disponibles avec images et ingrédients
- **Connexion IoT** : Communication avec un distributeur automatique de cocktails
- **Expérience utilisateur fluide** : Navigation intuitive et design élégant

## 🛠️ Technologies utilisées

- **Frontend** : HTML5, CSS3, JavaScript vanilla
- **Frameworks CSS** : Tailwind CSS
- **Backend IoT** : Communication avec Raspberry Pi Pico

## 🚀 Installation et utilisation

### Prérequis
- Un serveur web local
- Un distributeur de cocktails connecté Mixologic™ (Raspberry Pi Pico) 

### Étapes d'installation

1. **Clonez le repository**
   ```bash
   git clone https://github.com/alyssialopr/Mixologik.git
   cd Mixologik_app
   ```

2. **Configuration du distributeur (optionnel)**
   - Modifiez l'adresse IP dans `main.js` ligne 2 :
   ```javascript
   const PICO_BASE = 'http://VOTRE_IP_PICO';
   ```

3. **Lancez l'application**
   - Ouvrez `index.html` dans votre navigateur
   - Ou servez les fichiers via un serveur web local

## 📱 Utilisation

1. **Page d'accueil** : Lancez l'application depuis `index.html`
2. **Sélection de cocktails** : Cliquez sur "Voir les cocktails" pour accéder au catalogue
3. **Commande** : Sélectionnez votre cocktail préféré en cliquant sur "Choisir ce cocktail"
4. **Préparation** : Si connecté, le distributeur prépare automatiquement votre boisson

## 🍸 Cocktails disponibles

- **Mango Daïquiri** : Limonade vanillée, jus de mangue, jus de citron vert
- **Golden Punch** : Limonade vanillée, jus de mangue, sirop de sucre
- **Mojito** : Menthe, rhum, citron vert, eau gazeuse
- **Pina Colada** : Rhum, lait de coco, jus d'ananas

## 🎨 Structure du projet

```
Mixologik_app/
├── index.html          # Page d'accueil
├── cocktails.html      # Catalogue des cocktails
├── main.js            # Logique JavaScript
├── package.json       # Configuration npm
├── css/
│   └── style.css      # Styles personnalisés
├── images/
│   ├── Fondaccueilcocktail.jpeg
│   └── cocktailfond.jpeg
└── README.md          # Documentation
```

## 🔧 Configuration technique

### Communication avec le distributeur
L'application communique avec un Raspberry Pi Pico via des requêtes HTTP :
- Endpoint : `GET /dispense?cocktail=nom_cocktail`
- Réponse : JSON avec status et éventuels messages d'erreur


*Développé avec ❤️ pour les amateurs de cocktails*