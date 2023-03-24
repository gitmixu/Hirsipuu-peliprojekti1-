class HirsipuuPeli:
    def __init__(self):
        self.__historia = Pelihistoria()
        self.__elamat = 0
        self.__vastaus = ""
        self.__arvattava = []
        self.__voitto = 0           #0 merkitsee tappiota, suuremmat arvot voittoa

    def pelin_aloitus(self):
        self.__arvattava.clear()
        self.__voitto = 0
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
        self.__vastaus = choice(sanavarasto)
        self.__elamat = len(self.__vastaus) // 2 + 2        #elämien määrä riippuu sanan pituudesta?
        while len(self.__arvattava) < len(self.__vastaus):
            self.__arvattava.append("_")
        print(self.__vastaus)       #tämä poistetaan toki näkyvistä myöhemmin

    def piirra_hirsipuu(self):
        pass

    def arvaa(self):
        syote = input("Kirjoita yksi kirjain tai arvaa koko sana: ")
        print()
        if len(syote) == 1:
            apuri = 0
            while apuri < len(self.__vastaus):
                if syote == self.__vastaus[apuri]:
                    self.__arvattava[apuri] = syote
                apuri += 1
            verrokki = ""
            for kirjain in self.__arvattava:
                verrokki += kirjain
            if verrokki == self.__vastaus:
                self.__voitto += 1
        else:
            if syote == self.__vastaus:
                self.__voitto += 1

    def pelaa(self):
        self.pelin_aloitus()
        while self.__elamat > 0:
            for kirjain in self.__arvattava:
                print(kirjain, end="")
            print("", end="\n")
            print()
            print(f"Yrityksiä jäljellä {self.__elamat * '*'}")
            self.arvaa()
            if self.__voitto != 0:
                break
            self.__elamat -= 1
        if self.__voitto == 0:
            print(f"Parempi onni ensi kerralla! Oikea vastaus oli {self.__vastaus}.")
        else:
            print(f"Upeaa! Arvasit sanan {self.__vastaus}!")

class HirsipuuValikko:
    def __init__(self):
        self.__hirsipuupeli = HirsipuuPeli()
        self.__historia = Pelihistoria()
    
    def suorita(self):
        print("HIRSIPUU")
        print("|   0  0")
        print("|    0 0")
        print("o      0")
        print("T      0")
        print("^      0")
        print("      ¤¤¤")
        print("     ¤¤¤¤¤")
        print("    ¤¤¤¤¤¤¤")
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