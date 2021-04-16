import json


class Perso:   
    def __init__(self,**tous_les_monstres):
        for attr_name, attr_value in tous_les_monstres.items():
            setattr(self, attr_name, attr_value)
        self.pvencours=self.pvmax



def main():
    monstre=[]
    for tous_les_monstres in json.load(open("data_monstre.json")):
        monstre.append(Perso(**tous_les_monstres))
    print(monstre)
    for i in range(len(monstre)):
        print(monstre[i].classe)
        print(monstre[i].pvmax)
        
    
main()

