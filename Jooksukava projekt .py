nimi = input('mis su nimi on? ')
print('tere, ' + nimi + '!')

spordimees = input('kas oled spordimees, ' + nimi + '?' + '(jah/ei) ')
if spordimees == 'jah':

    vanus = input('kui vana sa oled? ')

    eesmärk = int(input('mis distantsi jooksmise jaoks sa treenid? (km) '))

    max_pulss = 220 - int(vanus)

    puhkepulss = input('Mis on su puhkepulss? (kui ei tea, vajuta Enter) ')

    if puhkepulss == "":
        print('Pole hullu! Puhkepulssi saad mõõta hommikul kohe pärast ärkamist:')
        print('loe 60 sekundit pulsilööke randmelt või kaelalt, või vaata spordikellalt.')
        print('Seni arvutan tsoonid ainult max pulsi järgi.')
        puhkepulss = 0
    else:
        puhkepulss = int(puhkepulss)

    reserv = max_pulss - puhkepulss
   
    z1_alumine = reserv * 0.5 + puhkepulss
    z1_ülemine = reserv * 0.6 + puhkepulss

    z2_alumine = reserv * 0.6 + puhkepulss
    z2_ülemine = reserv * 0.7 + puhkepulss

    z3_alumine = reserv * 0.7 + puhkepulss
    z3_ülemine = reserv * 0.8 + puhkepulss

    z4_alumine = reserv * 0.8 + puhkepulss
    z4_ülemine = reserv * 0.9 + puhkepulss

    z5_alumine = reserv * 0.9 + puhkepulss
    z5_ülemine = max_pulss

    z1 = f"{z1_alumine:.0f}-{z1_ülemine:.0f}"
    z2 = f"{z2_alumine:.0f}-{z2_ülemine:.0f}"
    z3 = f"{z3_alumine:.0f}-{z3_ülemine:.0f}"
    z4 = f"{z4_alumine:.0f}-{z4_ülemine:.0f}"
    z5 = f"{z5_alumine:.0f}-{z5_ülemine:.0f}"

    koormus = 1.0
    vastus = ""

    def kava1(koormus):
        
        print("Esmaspäev: puhkus")
        print(f"Teisipäev: { 40 * koormus :.0f} min kerge jooks, pulss {z2}")
        print(f"Kolmapäev: 10 min soojendus, 5 x { 3 * koormus:.0f} min kiirelt (pulss {z4}), vahele 2 min sörki, 10 min lõdvestus")
        print(f"Neljapäev: { 30 * koormus :.0f} min taastav jooks, pulss {z1}")
        print("Reede: puhkus")
        print(f"Laupäev: 10 min soojendus, { 20 * koormus :.0f} min tempojooks (pulss {z3}), 10 min lõdvestus")
        print(f"Pühapäev: {60 * koormus:.0f}-{75 * koormus:.0f} min pikk aeglane jooks, pulss {z2}")

    def kava2(koormus):
        print("Esmaspäev: puhkus")
        print(f"Teisipäev: { 25 * koormus :.0f} min kerge jooks, pulss {z2}")
        print(f"Kolmapäev: puhkus või kõnd, pulss {z1}")
        print(f"Neljapäev: 5 min soojendus, 4 x { 2 * koormus :.0f} min tempokalt (pulss {z3}), vahele 2 min kõndi, 5 min lõdvestus")
        print("Reede: puhkus")
        print(f"Laupäev: { 35 * koormus :.0f} min pikk aeglane jooks, pulss {z2}")
        print(f"Pühapäev: 20-30 min kõnd või venitus, pulss {z1}")

    while vastus != "sobib":
        print('Hästi, siin on sulle jooksukava: ')
        if eesmärk >= 10:
            kava1(koormus)
        else:
            kava2(koormus)

        vastus = input('Kas kava sobib sulle? (liiga kerge/liiga raske/sobib) ')
        if vastus == 'liiga kerge':
            koormus = koormus + 0.2
        elif vastus == 'liiga raske':
            koormus = koormus - 0.2

    print('Super, head treenimist! ')
else:
    print('Suurepärane! Head kosumist.')