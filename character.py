from typing import Dict
from stat_roller import StatRoller
from choice import *
from utils import *

class Character:
    def __init__(self, first_class, race):
        # Class_name: level
        self.first_class = first_class
        self.classes = [first_class]
        self.race = race
        self.level = 0
        self.levels = {}
        self.generate_stats()
        self.armor=""
        self.ac = 10 + (self.stats["Dex"] - 10) // 2
        self.hp = first_class.start_hp // 2 - 1
        self.speed = race.speed
        self.size = race.size
        self.proficiencies = race.proficiencies
        self.languages = race.languages
        self.features = race.features
        
        for f in self.features:
            f.gain(self)


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
            stats.sort(reverse=True)
            stats[0] += 2
            stats[1] += 1
            self.stats = dict(zip(self.first_class.stat_preference, stats))

        elif sm == 1:
            stats = [16, 16, 13, 12, 10, 8]
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

        for f in c.features:
            if f.level == self.levels[c.c_name]:
                self.features += [f]
                f.gain(self)
        print(self.hp)
        self.hp += c.start_hp // 2 + 1 + (self.stats["Con"] - 10) // 2
        print(self.hp)
        for f in self.features:
            f.lvl_up(self)

    def change_stat(self, stat, x):
        self.stats[stat] += x
    