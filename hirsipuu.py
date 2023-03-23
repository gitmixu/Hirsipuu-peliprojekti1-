class HirsipuuPeli:
    def __init__(self):
        self.__elamat = 0
        self.__vastaus = ""
        self.__arvattava = ""

    def pelin_aloitus(self):
        sanavarasto = []
        from random import choice
        with open("sanat.txt") as tiedosto:
            for rivi in tiedosto:
                sana = rivi.strip()
                if "Ã¤" in sana:
                    sana = sana.replace("Ã¤", "ä")
                if "Ã¶" in sana:
                    sana = sana.replace("Ã¶", "ö")
                sanavarasto.append(sana)
        self.__elamat = 5
        self.__vastaus = choice(sanavarasto)
        self.__arvattava = len(self.__vastaus) * "_"
        print(self.__vastaus)
        print(self.__arvattava)

    def piirra_hirsipuu(self):
        pass

    def piirra_sana(self):
        pass

    def pelaa(self):
        self.pelin_aloitus()
        while self.__elamat > 0:
            print("")
            print(f"yrityksiä jäljellä {self.__elamat * '¤'}")
            syote = input("Kirjoita yksi kirjain tai arvaa koko sana: ")
            self.__elamat -= 1

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
                self.__historia.tallenna_historia()
                break

class Pelihistoria:
    def hae_historia(self):
        pass

    def tallenna_historia(self):
        pass

peli = HirsipuuValikko()
peli.suorita()