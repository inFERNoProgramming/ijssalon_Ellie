from helper import *
from presentatie import *
import csv

inkomsten = {
    "Aarbeien_ijs_totaal" : 1000,
    "Vanille_ijs_totaal" : 2000,
    "Chocolade_ijs_totaal" : 1500,
    "Waterijsjes_totaal" : 750
    }

totaal_inkomsten = som(inkomsten)

presenteer(**inkomsten)

with open('boekhouding.csv', 'w', newline='') as csvfile:
    for key, value in inkomsten.items():
        writer = csv.writer(csvfile, delimiter=';')
    writer.writerow([key, value])
    