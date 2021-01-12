from Simulator import Simulator






tmp=1
while tmp!=0:
    trybe=int(input("Jaki tryb? Generator-0 Odczyt z pliku-1: "))
    c = Simulator(trybe)
    c.work()
    tmp=int(input("Dalej? 1-Tak 0-Nie: "))
    continue