cle = int(input("entrez la clé de décalage : "))
lettre = input("entrez la chaine de caractère : ")
lettre = lettre.lower()
lettre_modif = lettre

for i in range (0,len(lettre)):
    nombre = ord(lettre[i])
    if nombre >= 97 and nombre <= 122:
        nombre = nombre + cle
        stock = chr(nombre)
        lettre_modif = lettre_modif.replace(lettre[i], stock)
    if nombre > 122:
        nombre = nombre - 26
        stock = chr(nombre)
        lettre_modif = lettre_modif.replace(lettre[i], stock)

print("base : ",lettre,"\n")
print("cryptage :", lettre_modif,"\n")

lettre_modif_deux = lettre_modif

for i in range (0,len(lettre)):
    nombre = ord(lettre_modif[i])
    if nombre >= 97 and nombre <= 122:
        nombre = nombre - cle
        stock = chr(nombre)
        lettre_modif_deux = lettre_modif_deux.replace(lettre_modif[i], stock)

print("décryptage :", lettre_modif_deux,"\n")