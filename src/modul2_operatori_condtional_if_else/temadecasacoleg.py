nume = input("Numele tau este: ")

data_nasterii = input("Data nasterii te rog pe modelul zz/ll/aaaa: ")

from datetime import datetime
varsta = datetime.strptime(data_nasterii, "%d/%m/%Y")
an = varsta.year
if 2023 - an > 17:
    print("Esti major, te las sa intri!")
else:
    print("Mai ai rabdare pana implinesti 18 ani te rog")

cnp = input("Scrie-ti CNP-ul: ")
if len(cnp) != 13:
    print("Cnp-ul este format din 13 caractere. Mai incearca")
else:
    print("Corect pana aici.")
an_nastere_cnp = int(str(cnp[1]) + str(cnp[2]))
if an_nastere_cnp < 5 or an_nastere_cnp >= 50:
    print("Esti major, nu ai mintit.")
elif an_nastere_cnp > 5 and an_nastere_cnp < 49:
    print("Ai sub 18 ani.Sau esti prea batran pt noi. Nu ai voie aici...")
msauf = int(cnp[0])
if msauf % 2 == 1:
    print("Aici sunt pantofii !!")
else:
    print("Aici sunt gentile !!")