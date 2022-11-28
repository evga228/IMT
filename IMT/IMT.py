from math import *
print("Tere! Olen sinu sober - PHYTON!")
nimi=input("Mis on sinu nimi?")
print(nimi,",oi kui ilus nimi!")
print(nimi, ",")
vastus=int(input("kas sa tahat leida oma keha massi indeksi? 1-jah, 0-ei: "))
if vastus==1:
    while True:
        try:
            pikkus=int(input("Sisesta oma pikkus tais sentimeetrites: "))
            if pikkus>0 and pikkus<273: break
        except:
            print("VIGA")
    mass=-1
    while mass<0 or mass>400:
        try:        
            mass=float(input("Sisesta oma kaalu(kilogrammides): "))
        except:
            mass==1
       
    indeks=mass/(0.01*pikkus)**2
    print(nimi,",sinu keha indeks on:", round(indeks,1))
    if indeks<16:
        print("Tervisele ohtlik alakaal")
    elif indeks>=16 and indeks<=19:
        print("Alakaal")
    elif indeks>=20 and indeks<=25:
        print("Normaalkaal")
    elif indeks>=26 and indeks<=30:
        print("Ulekaal")
    elif indeks>=31 and indeks<=35:
        print("Rasvumine")
    elif indeks>=36 and indeks<=40:
        print("Tugev rasvumine")
    elif indeks>41:
        print("Tervisele ohtlik rasvumine")
else:
    print("Ei taha, siis ei taha.")
    print(" ")
    print("Kohtumiseni",nimi,"Igavesti Sinu, Python!")
