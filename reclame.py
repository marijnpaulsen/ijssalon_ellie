def mijn_functie_2(a,b):
    uitvoer_list = []
    uitvoer_list.append(a+b)
    uitvoer_list.append(a-b)
    uitvoer_list.append(a*b)
    uitvoer_list.append(a/b)
    return uitvoer_list


def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1 - korting)
    uitvoer = f'''Vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak {smaak}, van {prijs:.2f} euro voor {prijs_na_korting:.2f} euro.'''
    return uitvoer
print(aanbieding_1("aardbei", 4, 0.1))


def inkomsten_totaal(btw):
    inkomsten = [220, 430, 125, 160, 205, 90, 345]
    totaal = sum(inkomsten)
    bedrag = totaal * btw
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal:.2f} euro, waarover {bedrag:.2f} euro btw betaald dient te worden."
    return uitvoer
print(inkomsten_totaal(0.09))


def laag_en_hoog(mijn_lijst):
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    return [laagste, hoogste]
mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
print(laag_en_hoog(mijn_lijst))

def gemiddelde():
    mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
    gemiddeld_bedrag = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gemiddeld_bedrag:.2f} euro."
print(gemiddelde())


def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)
invoer_lijst = [10, 5, 3, 2, 1, 2, 9]
print(meervoudig(invoer_lijst))


def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
invoer_lijst_2 = [10, 5, 3, 2, 1, 2, 9]
print (combinatie(invoer_lijst_2))