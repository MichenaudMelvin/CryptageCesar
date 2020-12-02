mot = input("Quelle est le mot à crypter ? ")
clef = int(input("Quelle est la clé de cyptage ? "))
mot = mot.lower()
motCrypte = ""

for lettre in mot:
    nombreUnicode = ord(lettre)
    if (nombreUnicode >= 97 and nombreUnicode <= 122):
        nombreUnicode+=clef
        if(nombreUnicode>122):
            nombreUnicode-=26
    motCrypte = motCrypte + chr(nombreUnicode)

print(motCrypte)
