"""Dieses Programm soll ein Hangman-Spiel werden
Im Prinzip braucht man: 
-Eine Liste aus Wörtern, die es zu erraten gilt
-Ein Wort aus der Liste wird random ausgesucht und dann die Anzahl der Buchstaben als _ dargestellt
-Rateversuche
-Überprüfung, ob der Buchstabe im Wort enthalten ist
-An welcher Stelle enthalten ist
-Wenn RICHTIG --> An der gleichen Stelle (innerhalb des Wortes) eingesetzt (_s_el)
-Wenn FLASCH --> Versuch +1 und Zeichnung des Galgen"""

import random

rateliste = ["Baum", "Affe", "Hangman", "Schneemann"]

zufalls_begriff = random.choice(rateliste)
verbergen_zb = ''.join(['-' for _ in zufalls_begriff])

print(zufalls_begriff)
print(verbergen_zb)


