from feature import Feature


class Race:
    def __init__(self):
        self.speed = 30
        self.features = []
        self.size = "Medium"
        self.proficiencies = []
        self.languages = ['Common']


class Human(Race):
    def __init__(self):
        super().__init__()
        self.languages += ['*']

class Dwarf(Race):
    def __init__(self):
        super().__init__()
        self.speed = 25
        self.languages += ['Dwarven']
        self.features += [
            Feature(
                "Darkvision",
                "Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
            ),
            Feature(
                "Dwarven Resilience", 
                "You have advantage on saving throws against poison, and you have resistance against poison damage."
            ),
            Feature(
                "Dwarven Combat Training", 
                "You have proficiency with the battleaxe, handaxe, light hammer, and warhammer."
            ),
            Feature(
                "Stonecunning",
                "Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus."
            )
        ]
        self.proficiencies += ["Smiths' Tools"]
    
class HillDwarf(Dwarf):
    def __init__(self):
        super().__init__()
        self.features += [
            Feature(
                "Dwarven Toughness.",
                "Your hit point maximum increases by 1, and it increases by 1 every time you gain a level.",
                lcode="""p.hp += 1"""
            )
        ]
    
class MountainDwarf(Dwarf):
    def __init__(self):
        super().__init__()
        self.features += [
            Feature(
                "Dwarven Armor Training.",
                "You have proficiency with light and medium armor."
            )
        ]
        self.proficiencies += ["Light Armor", "Medium Armor"]

