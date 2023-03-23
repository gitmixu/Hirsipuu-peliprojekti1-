class HirsipuuPeli:
    def __init__(self):
        self.__elamat = 5

    def pelin_aloitus(self):
        sanavarasto = []
        from random import choice
        with open("sanat.txt") as tiedosto:
            for rivi in tiedosto:
                sana = rivi.strip()
                sanavarasto.append(sana)
        vastaus = choice(sanavarasto)
        arvattava = len(vastaus) * "_"
        print(vastaus)
        print(arvattava)

    def ohje_pelatessa(self):
        print("Kirjoita yksi kirjain.")

    def piirra_hirsipuu(self):
        pass

    def piirra_sana(self):
        pass

    def pelaa(self):
        self.pelin_aloitus()

class HirsipuuValikko:
    def __init__(self):
        self.__hirsipuupeli = HirsipuuPeli()
        self.__historia = Pelihistoria()
    
    def suorita(self):
        print("* * * Hirsipuu * * *")
        while True:
            print("")
            print("1 - aloita peli, 2 - katsele historiaa, 3 - lopeta")
            komento = input("Komento: ")
            if komento == "1":
                self.__hirsipuupeli.pelaa()
            elif komento == "2":
                self.__historia.hae_historia()
            elif komento == "3":
                break

class Pelihistoria:
    def hae_historia(self):
        pass

peli = HirsipuuValikko()
peli.suorita()