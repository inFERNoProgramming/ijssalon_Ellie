from algemene_functies import mijn_functie_2
def aanbieding_1(smaak, prijs, korting):
    afgetrokken_korting = prijs - prijs * korting
    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {afgetrokken_korting}.")

aanbieding1 = aanbieding_1("aarbei", 4, 0.1)

def inkomsten_totaal(a,b,c,d,e,f,g):
    inkomsten = a+b+c+d+e+f+g
    btw = inkomsten * 0.09
    print(f"Het totaal van alle inkomsten van deze week is {inkomsten} euro, waarover {btw} euro btw betaald dient te worden.")

inkomsten_en_btw = inkomsten_totaal(220,430,125,160,205,90,345)

def laag_en_hoog(mijn_lijst):
    maximum = max(mijn_lijst)
    minimum = min(mijn_lijst)
    print(maximum)
    print(minimum)
   
mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
hooglaag = laag_en_hoog(mijn_lijst)

def gemiddelde(a,b,c,d,e,f,g):
    average = (a+b+c+d+e+f+g) // 7
    print(f"De gemiddelde inkomsten deze week zijn {average} euro.")

gemiddeld_inkomen = gemiddelde(220,430,125,160,205,90,345)

def meervoudig(invoer_lijst):
    laag_en_hoog(invoer_lijst)

invoer_lijst = [10,5,3,2,1,2,9]
meervoudigen = meervoudig(invoer_lijst)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer 
