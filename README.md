# FACTURE_TP
**TP N1 - AWS reStart CMDLA1**

L'objectif de ce premier TP est de créer une facture.

**Notions**
- Manipulation des dictionnaires
- Utilisation du package **copy**
- Manipulation des tableaux
- Manipulation des boucles
- Utilisation d'un dépot public et création d'un **fork git** 

## Objectifs du TP
<p>Vous devez créer un programme qui permettra à l'utilisateur d'entrer une liste de produits. Chaque produit est identifié par trois attributs. Ces attributs seront utilisés pour évaluer le coût total. </p>

### Les attributs
1. Un nom
2. Un prix
3. La quantité 

<p>Les différents produits devront être stockés dans un tableau. Le coût total sera calculé à partir de l'ensemble des produits présents dans le tableau </p>

## Indication

1. Créer un **fork** de ce projet et décriver son fonctionnement
2. Créer le modèle de dictionnaire avec les attributs ci-dessus
3. Ecrire du code permettant de recupérer les saisies utilisateurs. Ceci vous permettra de créer de nouvelles données sur la base du modèle créer en 2
4. Ajouter les données à un tableau
5. Calculer le prix total de la facture
6. Effectuer un *git add .* pour enregister les modifications
7. Effectuer un *git commit - m "<votre_message>"* pour créer une photo de votre projet
8. Pousser votre code sur votre repository github. 
9. 

## Description du programme
1. Lancer l'application
2. le programme de à l'utilisateur d'entrer un produit en demandant le nom, prix et qte
3. le programme demande à l'utilisateur s'il veut ajouter un nouveau prroduit
4. s'il choisit "yes" alors il entre un nouveau produit ainsi de suite
5. une fois terminé le programme calcule le cout total de la facture puis affiche le résultat