class Varasto:
    def __init__(self):
        self.tuotteet={}
        #lopeta metodia varten
        self.paalla=True

        
        print("Varastonhallinta!")
        self.tiedosto = str(input("Anna tiedoston nimi: "))
        #testaa onko olemassa, tästä osasta kyllä epävarma toimisiko :D
        try:
            kirjanpito = open(self.tiedosto, "r")
            for rivi in kirjanpito:
                tuoteinfot = rivi.split()
                self.tuotteet[tuoteinfot[0]] = int(tuoteinfot[1])
            kirjanpito.close()
        except:
            pass
        
        
        
        self.paalooppi()
    def paalooppi(self):
        
        while self.paalla:
            toiminto = self.pyyda_komentoa()
            #jaotellaan merkkijono käsittelyä varten
            toiminto_lista = toiminto.split()
            
            #ohjelman pyörittämismetodit
            if toiminto_lista[0] == "apua":
                self.apua()
            elif toiminto_lista[0] == "lopeta":
                self.lopeta()

            #sanakirja metodit
            elif toiminto_lista[0] == "lisaa":
                self.lisaa(toiminto_lista[1])
            elif toiminto_lista[0] == "poista":
                self.poista(toiminto_lista[1])

            #rndm metodit
            elif toiminto_lista[0] == "listaa":
                self.listaa()
            elif toiminto_lista[0] == "hae":
                self.hae(toiminto_lista[1])
            
            #virheilmo
            else:
                print("Tuntematon komento")
        #päivittää tiedoston, kirjottaa koko hoidon uusiksi. Jättää typerästi yhden tyhjän rivin kyllä :D 
        kirjanpito = open(self.tiedosto, "w")
        for tuote, maara in self.tuotteet.items():
            kirjanpito.write(f"{tuote} {maara}\n")
        kirjanpito.close()
        print("Kiitos!")
    
    #pyytää komentoa ja muodostaa str
    def pyyda_komentoa(self):
        komento = str(input("Syötä komento: "))
        return komento


    #eri toimminnallisuudet
    def lisaa(self, tuote):
        self.tuotteet[tuote] = self.tuotteet.get(tuote, 0) +1
    
    def poista(self, tuote):
        self.tuotteet[tuote] = self.tuotteet.get(tuote) -1
        if self.tuotteet[tuote] == 0:
            self.tuotteet.pop(tuote)

    def listaa(self):
        print("Varaston sisältö:")
        for i, j in self.tuotteet.items():
            print(f"{i} {j} kpl")
    def hae(self, tuote):
        if tuote in self.tuotteet:
            print(f"Esinettä {tuote} varastossa {self.tuotteet[tuote]} kpl")
        elif tuote not in self.tuotteet:
            print("Esinettä sukat ei löydy varastosta")

    def apua(self):
        return print(f"Komennot:\n lisaa <esine> -- lisää yhden kappaleen esinettä varastoon\n listaa -- listaa kaikki varaston esineet\n hae <esine> -- kertoo esineen varastotilanteen\n poista <esine> -- poistaa yhden kappaleen esinettä varastosta\n apua -- tulostaa komennot\n lopeta -- lopettaa ohjelman suorituksen")
    def lopeta(self):
        self.paalla = False



if __name__ == "__main__":
    Varasto()
