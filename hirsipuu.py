class HirsipuuPeli:
    def __init__(self):
        self.__elamat = 0
        self.__vastaus = ""
        self.__arvattava = []

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
        while len(self.__arvattava) < len(self.__vastaus):
            self.__arvattava.append("_")
        print(self.__vastaus)       #tämä poistetaan toki näkyvistä myöhemmin

    def piirra_hirsipuu(self):
        pass

    def arvaa(self):
        syote = input("Kirjoita yksi kirjain tai arvaa koko sana: ")
        if len(syote) == 1:
            apuri = 0
            while apuri < len(self.__vastaus):
                if syote == self.__vastaus[apuri]:
                    self.__arvattava[apuri] = syote
                apuri += 1

    def pelaa(self):
        self.pelin_aloitus()
        while self.__elamat > 0:
            print(self.__arvattava)
            print("")
            print(f"yrityksiä jäljellä {self.__elamat * '¤'}")
            self.arvaa()
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