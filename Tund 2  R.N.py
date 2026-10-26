# 2 tund. ANDMETÜÜBID/ data type

# õppida järgmised andmetüübid
name = "Joonas" # string/ Sõne
age = 21 # integger/ täisarv
height = 192 # float/ ujukomaarv
student = True # boolean/ tõeväärtus

#print(name * age) # kood töötab prindib välja 21x "Joonas"
#print (name + age) # viga andmetüüpides, ei saa tekstile numbrit liita
#print (age + height) # kood töötab, täisarvule saab liita ujukomaarvu.
#print (age + student) # kood töötab, True = 1 ja false = 0, seega 21 + 1 = 22
#print (name + student) # ei tööta, sõnale ei saa liita tõeväärtust.
print(101.5 % 5) # töötab, % on jäägi leidmine, 101,5 jagada 5 annab 1,5 jäägi.
print(101.5 // 5) # töötab, // on täisarvuline jagamine, 101,5 jagada 5 annab 20.0
print(101.5 / 5) # töötab, / on tavaline jagamine, 101,5 jagada 5 annab 20.3

exp = 1234 # näiteks on sinu kogemuse punktid, mis on täisarv
lvl = exp // 100 # iga 100 exp kohta saab user uue lvl
print(lvl) # prindib lvl muutuja väärtuse, mis on 12, kuna 1234 // 100 = 12
print(exp // 100) # prindib 12, kuna // on täisarvuline jagamine, sama asi mis exp = 1234, aga see pole muutujasse salvestatud väärtus

#print(x * 5) # ei tööta, kuna x pole defineeritud, see on viga.
print("x" * 5) # töötab, kuna jutumärkides on "x" sõne ehk tekst

print("my name is " + name) 
print ("my name is", name) 
#print("My name is " + age) # ei tööta, kuna age on arv, aga sõnale ei saa liita arvu
print("Joonas is", age, "years old") # töötab, kuna koma abil saab liita erinevaid andmetüüpe, siin on tekst (sõne) ja arv 


######.   ÜLESANNE   ########

pi = 3.14
radius = 20
# r ruudus on radius**2, kaks KAKS KORRUTUSMÄRKI ON ASTENDAMINE
print("circle area is: ", pi * radius**2)  # töötab
# saaks ka kirjutada 
# circle_area = pi * radius**2


#ANDMETÜÜPIDE TEISENDAMINE / DATA TYPE CASTING

#print("2" + 2) # ei tööta, kuna tekstile ei saa liita arvu
print("2" + str(2)) # töötab, kuna teisendame arvu tekstiks
print(str(1.234))  #float (ujukomaarv) teisendatud stringiks (sõne)
print(str(True))  # boolean (tõeväärtus) teisendatud stringiks (sõne)
print(int(1)) # sting (sõne)teisendatud integeriks (täisarv)
print(bool(1), 'and', bool(0)) # integer teisendatud booleaniks


#SISEND / INPUT

#input('mis riigi seebikad sulle kõige rohkem meeldivad?') # Töötab, aga nii ei tee kuna vastus ei salvestu kuhugi.

email = input('sisesta oma emaili aadress:') # nii on väärtus salvestatud muutujasse
robot_speed = input("what's the robot's speed?") # väärtus salvestatud muutujasse
distance = 5
print("it takes", int(robot_speed) / distance, "minutes to drive from A to B") 






