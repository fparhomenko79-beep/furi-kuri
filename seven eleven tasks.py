import math
for n in range(2, 10**6):
    i = math.ceil(math.log2(n))
    nom_bit = 440*i
    nom_bait = math.ceil(nom_bit / 8)
    if (nom_bait*1892412)/1024 >= 305726:
        print(n)
        break
else:
    print("no")