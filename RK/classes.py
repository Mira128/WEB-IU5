
class Batonist:

    def __init__(self, IDbat, SecondName, ExperienceTime, Age, IDorc):
        self.IDbat = IDbat
        self.SecondName = SecondName
        self.ExperienceTime = ExperienceTime
        self.Age = Age
        self.IDorc = IDorc

class Orchestra:

    def __init__(self, IDorch, Name, MemberNum):
        self.IDorch = IDorch
        self.Name = Name
        self.MemberNum = MemberNum

class OrchestraBatonists:

    def __init__(self, IDbat, IDorc):
        self.IDbat = IDbat
        self.IDorc = IDorc

class OrcheNamesMinAges:

    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age

def batonistsAgeGet(OrcheNamesMinAges):
        return OrcheNamesMinAges.Age

Batonists = [Batonist(1, "Yanova", 10, 43, 1),
             Batonist(2, "Padilov", 8, 33, 1),
             Batonist(3, "Macichan", 5, 31, 2),
             Batonist(4, "Sokolov", 9, 34, 3),
             Batonist(5, "Kochetkov", 12, 40, 3),
             Batonist(6, "Volkov", 10, 41, 4),
             Batonist(7, "Gilyajeva", 8, 30, 5),
             Batonist(8, "Antropov", 3, 27, 6),
             Batonist(9, "Abramov", 18, 48, 6)
             ]

Orchestras = [Orchestra(1, "Simple music ensemble", 20),
              Orchestra(2, "Neorchestra", 13),
              Orchestra(3, "Imperialis Orchestra ", 28),
              Orchestra(4, "TCHAIKOVSKY ORCHESTRA ", 18),
              Orchestra(5, "Acapella-Sakartvelo", 12),
              Orchestra(6, "Russian Folk Orchestra Moscow", 80)
              ]

OrchestraBatonistsList = [
              OrchestraBatonists(1, 1),
              OrchestraBatonists(2, 1),
              OrchestraBatonists(3, 2),
              OrchestraBatonists(4, 3),
              OrchestraBatonists(5, 3),
              OrchestraBatonists(6, 4),
              OrchestraBatonists(7, 5),
              OrchestraBatonists(8, 6),
              OrchestraBatonists(9, 6)
              ]

"""1 inquiry"""
FirstLetter = "A"
BatonistsBeginA = list(x for x in Batonists if x.SecondName.startswith(FirstLetter))
IDOrchestrasWithBatA = list(map(lambda x: x.IDorc, BatonistsBeginA))
OrchestrasWithBatA = list(map(lambda x: (x.Name, x.IDorch), filter(lambda x: x.IDorch in IDOrchestrasWithBatA, Orchestras)))

OrchestrasById = {}
for (Name, IDorch) in OrchestrasWithBatA:
    OrchestrasById[IDorch] = Name

print("Batonist Surname | Orchestra name")

for i in BatonistsBeginA:
    print(i.SecondName, "  |  ", OrchestrasById[i.IDorc], "\n")
print("\n")

"""2 inquiry"""

IDOrchestras = list(map(lambda x: x.IDorch, Orchestras))
Ages = list(map(lambda x: (x.Age, x.IDorc), filter(lambda x: x.IDorc in IDOrchestras, Batonists)))

MinAgeByID = {}
for (Age, IDorc) in Ages:
    if IDorc not in MinAgeByID or MinAgeByID[IDorc] > Age:
        MinAgeByID[IDorc] = Age

ListOrchestraMinAges = list()
for i in Orchestras:
    ListOrchestraMinAges.append(OrcheNamesMinAges(i.Name, MinAgeByID[i.IDorch]))

ListOrchestraMinAges.sort(key= batonistsAgeGet)

print("Orchestra name | Batonist min age")

for i in ListOrchestraMinAges:
    print(i.Name, "  |  ", i.Age, "\n")
print("\n")

"""3 inquiry"""

BatonistsInfo = list(map(lambda x: (x.IDorc, x.SecondName, x.ExperienceTime), 
                            filter(lambda x: x.IDorc in IDOrchestras, Batonists)))

BatonistsInfo.sort(key= lambda x: x[2])

print("Batonist Secondname  |  Batonist exp  |  Orchesra name  |  Orchesra MemberNum")
for i in BatonistsInfo:
    for j in Orchestras:
        if ( i[0] == j.IDorch):{
            print(i[1], "  |  ", i[2], "  |  ", j.Name, "  |  ", j.MemberNum, "\n")
        }

