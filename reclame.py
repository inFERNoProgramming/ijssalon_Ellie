def aanbieding_1(smaak, prijs, korting):
    afgetrokken_korting = prijs - prijs * korting
    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {afgetrokken_korting}.")

reclame = aanbieding_1("aarbei", 4, 0.1)

def inkomsten_totaal(inkomsten):
    return 