class Hirsipuu:
    pass #sovelluslogiikka

class HirsipuuPeli:
    def __init__(self):
        self.__hirsipuu = Hirsipuu()
    
    def hae_historia(self):
        pass
    
    def ohje_aloitus(self):
        print("Hirsipuu")
        print("1 - aloita peli, 2 - katsele historiaa, 3 - lopeta")

    def ohje_pelatessa(self):
        print("Kirjoita yksi kirjain.")

    def piirra_hirsipuu(self):
        pass

    def piirra_sana(self):
        pass
    
    def pelaa(self):
        self.ohje_aloitus()
        while True:
            print("")
            komento = input("Komento: ")
            if komento == "1":
                pass
            elif komento == "2":
                self.hae_historia()
            elif komento == "3":
                break

class Pelihistoria:
    pass #Pelatut pelit tallennetaan täällä?