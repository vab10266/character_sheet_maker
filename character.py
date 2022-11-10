from typing import Dict
from classes.barbarian import *
from classes.fighter import *
from stat_roller import StatRoller
from choice import *
from utils import *

class Character:
    def __init__(self, first_class, race, stats=None):
        # Class_name: level
        self.first_class = first_class
        self.classes = [first_class]
        self.race = race
        self.level = 0
        self.levels = {}
        if stats is None:
            self.generate_stats()
        else:
            self.stats = stats
        self.armor="Unarmored"
        self.ac = 10 + (self.stats["Dex"] - 10) // 2
        self.hp = first_class.start_hp // 2 - 1
        self.speed = race.speed
        self.size = race.size
        self.proficiencies = race.proficiencies
        self.languages = race.languages
        self.features = race.features
        self.subclasses = []
        self.resources = {}
        
        # for f in self.features:
        #     f.gain(self)


        self.add_level(first_class)

    def generate_stats(self):

        # print("Select Stat mode:\n\t1: standard\n\t2: random\n\t3: manual\n: ", end="")
        # sm = int(input())
        sm = Decision("Select Stat Generation Method:", {
            "1": Choice("Standard", 1),
            "2": Choice("Random", 2),
            "3": Choice("Manual", 3),
            }).choose()
        if sm == 2:
            # print("Mode:\n\t1: '3d6'\n\t2: '2d6p6'\n: ", end="")
            # mode = ['3d6', '2d6p6'][int(input())-1]
            mode = Decision("Mode:", {
                "1": Choice("3d6", '3d6'),
                "2": Choice("2d6 plus 6", '2d6p6'),
            }).choose()
            sr = StatRoller(mode)
            stats = sr.roll_stats()
            # stats.sort(reverse=True)
            # stats[0] += 2
            # stats[1] += 1
            self.stats = dict(zip(self.first_class.stat_preference, stats))

        elif sm == 1:
            stats = [15, 14, 13, 12, 10, 8]
            self.stats = dict(zip(self.first_class.stat_preference, stats))

        else:
            print("Manually Enter Stats w/ Racial Bonus")
            print("Str: ", end="")
            str = int(input())
            print("Dex: ", end="")
            dex = int(input())
            print("Con: ", end="")
            con = int(input())
            print("Int: ", end="")
            intel = int(input())
            print("Wis: ", end="")
            wis = int(input())
            print("Cha: ", end="")
            cha = int(input())
            self.stats = {
                "Str": str, 
                "Dex": dex,
                "Con": con, 
                "Int": intel, 
                "Wis": wis, 
                "Cha": cha
            }

        print(self.stats)

    def add_level(self, c):
        self.level += 1
        if c.c_name in self.levels:
            self.levels[c.c_name] += 1
        else:
            self.levels[c.c_name] = 1
            if self.level != 1:
                self.classes += [c]

        if c.sc_lvl == self.levels[c.c_name]:
            self.add_subclass(c.c_name)

        
        # print(self.hp)
        self.hp += c.start_hp // 2 + 1 + (self.stats["Con"] - 10) // 2
        # print(self.hp)
        # print("lvl_num_features: ", len(self.features))
        for f in self.features:
            f.update(self)

        if self.armor=="Unarmored" and self.ac < (10 + (self.stats["Dex"] - 10) // 2):
            self.ac = (10 + (self.stats["Dex"] - 10) // 2)
        

    def process(self):
        # print("num_features: ", len(self.features))
        for i in range(len(self.classes)):
            c = self.classes[i]
            if self.levels[c.c_name] >= c.sc_lvl:
                for sub in self.subclasses:
                    if sub.c_name == c.c_name:
                        self.classes[i] = sub
        # print("num_features: ", len(self.features))
                
        for c in self.classes:
            # print('a', self.classes, self.subclasses)
            for r in c.resources.keys():
                self.resources[r] = c.resources[r][self.levels[c.c_name] - 1]
            for f in c.features:
                if f.level <= self.levels[c.c_name]:
                    self.features += [f]
        # print("num_features: ", len(self.features))

        for f in self.features:
            # print(f.title)
            f.gain(self)
        for f in self.features:
            f.update(self)
        # print("num_features: ", len(self.features))

    def asi(self):
        stat_choices = {
            "1": Choice('Str', 'Str'),
            "2": Choice('Dex', 'Dex'),
            "3": Choice('Con', 'Con'),
            "4": Choice('Int', 'Int'),
            "5": Choice('Wis', 'Wis'),
            "6": Choice('Cha', 'Cha')    
        }
        print(show_stats(self.stats))
        fasi = Decision("Choose your first ASI:", stat_choices).choose()
        self.stats[fasi] += 1
        print(show_stats(self.stats))
        sasi = Decision("Choose your second ASI:", stat_choices).choose()
        self.stats[sasi] += 1
        print(show_stats(self.stats))

    def add_subclass(self, c):
        if c == 'Barbarian':
            sc_choices = {
                '1': Choice("Totem", Totem),
                '2': Choice("Zealot", Zealot)
            }
            sc = Decision("Choose your Primal Path:", sc_choices).choose()(stats_set=True)
            # print(type(sc))
        if c == 'Fighter':
            sc_choices = {
                '1': Choice("Champion", Champion),
                '2': Choice("Battle Master", BattleMaster)
            }
            sc = Decision("Choose your Primal Path:", sc_choices).choose()(stats_set=True)
            # print(type(sc))
            # self.subclasses += [sc]
        self.subclasses += [sc]
        for i in range(len(self.classes)):
            c = self.classes[i]
            if sc.c_name == c.c_name:
                self.classes[i] = sc

