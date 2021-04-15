import json

"""
class Agent:

    def __init__(self, position, **agent_attributes):
        self.position = position
        for attr_name, attr_value in agent_attributes.items():
            setattr(self, attr_name, attr_value)

for agent_attributes in json.load(open("agents-100k.json")):
        latitude = agent_attributes.pop("latitude")
        longitude = agent_attributes.pop("longitude")
        position = Position(latitude, longitude)
        agent = Agent(position, **agent_attributes)
        print(agent.position.longitude)
        print(agent.position.latitude)
"""

class Perso:
    def __init__(self, **caract_monstre):
        for attr_name, attr_value in caract_monstre.items():
            setattr(self, attr_name, attr_value)
        

#for caract_monstre in json.load(open("/home/gabriel-le/Téléchargements/la_poo_avec_python-00_setup/agents-100k.json")):
for caract_monstre in json.load(open("data_monstre.json")):
    monstre=Perso(**caract_monstre)

print(caract_monstre)
print(monstre.classe)
print(monstre.pvmax)
#print(monstre.sex)