#L'objectif de ce mini TP consite en la génération d'une facture
import copy
modeleProduit={"nom":"","prix":0.0,"quantite":0} #definition du model de produit
#Définition de la fonction pour verifier si une chaine de caractère peut etre convertit en float
def is_float(s):
    result = False
    if s.count(".") == 1 or s.count(".") == 0:
        if s.replace(".", "").isdigit():
            result = True
    return result
print("-------------------------------------------")
print("---------GENERATEUR DE FACTURE-------------")
print("-------------------------------------------")
stop=False   #CONDITION D'ARRET POUR L'ajout des produits dans un tableau
listeProduit=[]
while (stop!=True) :
    produit=copy.deepcopy(modeleProduit);
    nom=input("Quel est le nom du produit ? ")
    prix=input("Quel est le prix du produit ? ")
    while ((not is_float(prix)))  :
        prix=input("Quel est le prix du produit (Veuillez entrer un nombre decimal) ? ")
    qte=input("Quel est la quantité du produit ? ")
    while ((not qte.isdigit()))  :
        qte=input("Quel est la quantité du produit ? ")
    produit["nom"]=nom
    produit["prix"]=prix
    produit["quantite"]=qte
    listeProduit.append(produit)
    confirm=""
    while confirm!="yes" and confirm!="no" :
        confirm=input("Voulez-vous ajouter un nouveau produit (yes/no) ? ")
        if confirm=="yes" :
            pass
        elif confirm=="no" :
            stop=True
        
    #print(produit)

coutTot=0 #initialisation du prix total

#Calculer le prix et afficher la facture
print("--------------------Facture-------------------")
for x in listeProduit :
    coutTot+=float(x["prix"])*int(x["quantite"])
    print(f'---{x["nom"]}--------{x["prix"]}---------{x["quantite"]}------{float(x["prix"])*int(x["quantite"])}') # affichage du produit
print(f'-----------TOTAL A PAYER : {coutTot}------------------ ')
#afficher la facture

    
    
    
    
    
    
    
    
    
    