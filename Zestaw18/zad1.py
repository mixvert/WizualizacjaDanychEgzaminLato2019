class Osoba:
    imie = "Jan"
    nazwisko = "Kowalski"
    rokUrodzenia = 2000
    wiek = 0

    def __init__(self, im, nazw, rok):
        self.imie = im
        self.nazwisko = nazw
        self.rokUrodzenia = rok
        self.wiek = 2019 - rok

    def info(self):
        print("| " + self.imie + " | " + self.nazwisko + " | " + str(self.rokUrodzenia) + " | " + str(self.wiek))


o1 = Osoba("Jan", "Nowak", 1980)
o1.info()
o2 = Osoba("Tomasz", "Kowal", 2005)
o2.info()
