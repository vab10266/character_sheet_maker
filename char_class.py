# from random import choice
from feature import ClassFeature
from choice import *

class Class:
    def __init__(self, stats_set=False):
        self.stat_preferences = []
        self.start_hp = 1
        self.st_prof = []
        self.features = []
        self.sc_lvl = 1
        self.resources = {}
        
class Bard(Class):
    def __init__(self, stats_set=False):
        super().__init__()
        self.start_hp = 8
        if stats_set is False:
            self.stat_preference =  Decision("Select Stat Priority:", {
                "1": Choice("Spell", ["Cha", "Con", "Dex", "Wis", "Str", "Int"]),
                "2": Choice("Damage", ["Dex", "Cha", "Con", "Wis", "Str", "Int"]),
                "3": Choice("Tank", ["Con", "Cha", "Dex", "Wis", "Int", "Str"]),
            }).choose()
        else:
            self.stat_preference = None
        self.sc_lvl = 3
        self.c_name = "Bard"
        
class Fighter(Class):
    def __init__(self, stats_set=False):
        super().__init__()
        self.start_hp = 10
        if stats_set is False:
            self.stat_preference = Decision("Select Stat Priority:", {
                "1": Choice("Str based", ["Str", "Con", "Dex", "Wis", "Int", "Cha"]),
                "2": Choice("Dex Based", ["Dex", "Con", "Wis", "Str", "Cha", "Int"]),
            }).choose()
        else:
            self.stat_preference = None
        self.sc_lvl = 3
        self.c_name = "Fighter"

class Swords(Bard):
    def __init__(self):
        super().__init__()
        # self.stat_preference = choice([
        #     ["Cha", "Dex", "Con", "Wis", "Str", "Int"],
        #     ["Cha", "Dex", "Con", "Wis", "Int", "Str"]
        # ])
        self.sc_name = "Swords"

class Valor(Bard):
    def __init__(self):
        super().__init__()
        # self.stat_preference = choice([
        #     ["Cha", "Con", "Dex", "Wis", "Str", "Int"],
        #     ["Cha", "Con", "Dex", "Wis", "Int", "Str"]
        # ])
        self.sc_name = "Valor"

