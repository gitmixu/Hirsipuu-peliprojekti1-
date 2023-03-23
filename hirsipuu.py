class HirsipuuPeli:
    def __init__(self):
        self.__sanavarasto = []

    def pelin_aloitus(self):
        pass

    def ohje_pelatessa(self):
        print("Kirjoita yksi kirjain.")

    def piirra_hirsipuu(self):
        pass

    def piirra_sana(self):
        pass

    def hae_sana(self):
        from random import choice
        with open("sanat.txt") as tiedosto:
            for rivi in tiedosto:
                sana = rivi.strip()
                self.__sanavarasto.append(sana)
        arvattava = choice(self.__sanavarasto)

    def pelaa(self):
        pass

class HirsipuuValikko:
    def __init__(self):
        self.__hirsipuupeli = HirsipuuPeli()
        self.__historia = Pelihistoria()
    
    def ohje_aloitus(self):
        print("Hirsipuu")
        print("1 - aloita peli, 2 - katsele historiaa, 3 - lopeta")
    
    def suorita(self):
        self.ohje_aloitus()
        while True:
            print("")
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