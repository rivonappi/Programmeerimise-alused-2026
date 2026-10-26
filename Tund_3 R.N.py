#nimi = "joonas" # string ehk sõne
#vanus = 12 # integer ehk täisarv
#kaal = 123.45 # float ehk ujukomaarv
#tudeng = True # boolean ehk tõeväärtus

####### sõne / string ######

name = "RWW. -345#   asmus"
print(name[1])  #väljastab teise sümboli sest lugemine algab 0-st
print(name[-3]) # väljastab tagant poolt kolmanda sümboli

isikukood = "0000007"
# vahemiku saab kätte : abil
print(isikukood[0:2]) # väljastab 0-st kuni 2-ni aga 2 ei kuulu vahemikku
print("agent", isikukood[-3:]) # väljastab tagant poolt 3 sümbolit ehk 007


############# JÄRJENDID (LOENDID) / LISTS #############

puuviljad = ["õun", "pirn", "banaan", "apelsin"] # kandilised sulud tähendavad, et tegemist on listiga

print(puuviljad[1]) # väljastab listi teise elemendi ehk pirn
print(puuviljad[-1]) # väljastab listi viimase elemendi ehk apelsin
print(puuviljad[0:3]) # väljastab listi esimesed kolm elementi ehk õun, pirn, banaan         

students = ["mina", "Pets", "Margus", "Priit" ]
numbers = [69, 666, 6, 7, 42, 1337]
user_data = ["pets", 123456.33, True, False, 100, "sinised sokid"] # listi väärtused võivad olla erinevat tüüpi

## sõne näide
name = "Margus" #string
print(len(name)) # väljastab sõne pikkuse ehk 6, len = length ehk pikkus
### sama, listi näide
kriminaalid = ["Mati", "Jüri", "Kalle"]
print(len(kriminaalid)) # väljastab listi pikkuse ehk 3


######### näide

students = ["mina", "Pets", "Margus", "Priit" ]
numbers = [69, 666, 6, 7, 42, 1337]
kriminaalid = ["Mati", "Jüri", "Kalle"]
weapons = ["lusikas", "nuga", "kivi"]

print(students[2], "killed", numbers[5], kriminaalid[2] + "s with a", weapons[2]) # väljastab: Margus killed 1337 Kalles with a kivi



######### MOODULID / MODULES / TEISTES KEELTES TUNTUD LIBRARY NIME ALL #############

#import random # moodul, mis sisaldab funktsioone juhuslike arvude genereerimiseks
#kui kirjutada 

from random import random, choice, randint 
# siis saab kasutada funktsioone ilma random. eesliidet kasutamata

print(random()) # väljastab juhusliku (float) ujukomaarvu vahemikus 0.0 kuni 1.0
print(choice(students)) # väljastab juhusliku nime students listist
print(randint(1, 10)) # väljastab juhusliku täisarvu vahemikus 1 kuni 10 (kaasa arvatud mõlemad) integer= täisarv

#### kirjutan lause ümber randomiga

print(choice(students), "killed", randint(1, 10), choice(kriminaalid) + "s with a", choice(weapons)) # väljastab juhusliku lause


print(students[randint(0, len(students)-1)], "killed", randint(1, 10), kriminaalid[randint(0, len(kriminaalid)-1)] + "s with a", weapons[randint(0, len(weapons)-1)]) # väljastab juhusliku lause aga ilma choice funktsioonita, kasutades randint funktsiooni ja len funktsiooni, et leida listi pikkus


###saab ka

random_student = students[randint(0, len(students)-1)]
random_kriminaal = kriminaalid[randint(0, len(kriminaalid)-1)]
random_weapon = weapons[randint(0, len(weapons)-1)]

print(random_student, "killed", random_kriminaal + "s with a", random_weapon) 


########## TSÜKLID (KORDUSED) / LOOPS #############
#while True: # while tsükkel, mis kordab tegevust seni kuni tingimus on tõene ehk True (lõpmatu kordus)
    #print("Tere!") # väljastab sõna Tere! lõpmatuseni
    #break # katkestab tsükli ehk lõpetab tegevuse

#n = 0
#while True:
   # n + 1
   # print(n)


pw_in_database = "kiisuke"
entered_pw = input("Sisesta parool: ") # küsib kasutajalt sisestust 

while pw_in_database != entered_pw: # kui sisestatud parool ei ole sama mis andmebaasis
    print("Vale parool!") # väljastab sõnumi
    entered_pw = input("Sisesta parool: ") # küsib uuesti sisestustkiisuke
print("Tere tulemast!") # kui parool on õige, väljastab sõnumi









