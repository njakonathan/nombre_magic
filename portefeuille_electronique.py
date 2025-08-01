

print("Bienvenue dans Orange Money !")

nom_utilisateur = input("Entrez votre nom: " )
solde_actuel = int(input("Entrez votre solde actuel: "))
while True:
    code_pin = input("Entrez votre code PIN (4 chiffres) : ")
    lonngueur_code_pin = len(code_pin) #nbre de caractères du code PIN
    if code_pin.isdigit() and lonngueur_code_pin == 4: #s'assurer que le code PIN est un nombre et qu'il contient 4 caractères
        break
    else:
        print(" Code PIN invalide. Veuillez entrer exactement 4 chiffres.")

print("Que souhaitez-vous faire ?")                   
operation = [ "1.Recharger mon compte",
             "2.Envoyer de l'argent",
             "3.Retirer de l'argent",
             "4.Consulter mon solde"

    ]

for n in operation:
        print(n)
choix_utilisateur = int(input("Votre choix : "))#l'utilisateur devra choisir un chiffre compris entre 1 et 4 

actif = True
while actif:
        if choix_utilisateur == 1:
                montant_à_ajouter = int(input("Entrez le montant à ajouter à votre solde actuel : "))
                solde_actuel = solde_actuel+montant_à_ajouter
                print("Opération effectuée avec succès !")
                print(f"{nom_utilisateur},Votre nouveau solde est : {solde_actuel} XAF")
        elif choix_utilisateur == 2:
                nom_destinataire = input("Entrez le nom du destinataire de votre dépot : ")
                montant_à_envoyer = int(input("Quelle somme d'argent voulez-vous envoyer ? "))
                if montant_à_envoyer <= solde_actuel:
                        print("Opération effectuée avec succès !")
                        print(f"Vous venez d'envoyer la somme de {montant_à_envoyer} XAF à Mr/Mme {nom_destinataire}")
                        solde_actuel = solde_actuel-montant_à_envoyer
                        print(f"{nom_utilisateur},Votre nouveau solde est : {solde_actuel} XAF")
                else:
                    print("Solde insuffisant pour effectuer cette opération ! ")
       
        elif choix_utilisateur == 3:
            montant = int(input("Montant à retirer : "))
            confirmation = input("Confirmez votre code PIN : ")

            if confirmation == code_pin:
                if montant <= solde_actuel:
                    solde_actuel -= montant
                    print("Retrait effectué avec succès.")
                    print(f"{nom_utilisateur}, votre nouveau solde est : {solde_actuel} XAF")
                else:
                    print("Solde insuffisant.")
            else:
                print(" Code PIN incorrect.")

        elif choix_utilisateur == 4:
            print(f"{nom_utilisateur}, votre solde est : {solde_actuel} XAF")
        else:
               print("Choix invalide !")
        break