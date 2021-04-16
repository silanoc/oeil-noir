import json


class Perso:   
    
    def __init__(self,**tous_les_monstres):
        for attr_name, attr_value in tous_les_monstres.items():
            setattr(self, attr_name, attr_value)
            #
            # self.pvencours=self.pvmax



def main():
    for tous_les_monstres in json.load(open("data_monstre.json")):
        monstre = Perso(**tous_les_monstres)
        print(tous_les_monstres)
        print(monstre)
        print(monstre.classe)
        print(monstre.pvmax)
        print(monstre.pvencours)
        print("---")

main()

