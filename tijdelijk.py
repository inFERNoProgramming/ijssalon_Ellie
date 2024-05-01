prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
}
korting = 0.8
aanbieding = prijzen["vanille"] * korting
reclame_tekst = (f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts €{aanbieding}")
#ik heb geen reclame_tekst2 omdat het mijne er anders uitzag dan in de cursus en ik niet zo goed snapte wat ik er precies mee moest doen.
reclame_tekst3 = reclame_tekst.upper()
reclame_tekst4 = reclame_tekst3.split()
for el in reclame_tekst4:
    if len(el) >= 5:
        print(el.upper())
    else:
        print(el.lower())


