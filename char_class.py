# from random import choice
from feature import ClassFeature
from choice import *

class Class:
    def __init__(self, stats_set=False):
        self.stat_preferences = []
        self.start_hp = 1
        self.st_prof = []
        self.features = []
        

class Barbarian(Class):
    def __init__(self, stats_set=False):
        super().__init__()
        self.start_hp = 12
        if stats_set is False:
            self.stat_preference = Decision("Select Stat Priority:", {
                "1": Choice("Damage", ["Str", "Con", "Dex", "Wis", "Cha", "Int"]),
                "2": Choice("Tank", ["Con", "Str", "Dex", "Wis", "Int", "Cha"]),
            }).choose()
        else:
            self.stat_preference = None
    
        self.c_name = "Barbarian"
        self.features += [
            ClassFeature(
                "Rage",
                "In battle, you fight with primal ferocity. On your turn, you can enter a rage as a bonus action. While raging, you gain the following benefits if you aren't wearing heavy armor: You have advantage on Strength checks and Strength saving throws. When you make a melee weapon attack using Strength, you gain a bonus to the damage roll that increases as you gain levels as a barbarian, as shown in the Rage Damage column of the Barbarian table. You have resistance to bludgeoning, piercing, and slashing damage. If you are able to cast spells, you can't cast them or concentrate on them while raging. Your rage lasts for 1 minute. It ends early if you are knocked unconscious or if your turn ends and you haven't attacked a hostile creature since your last turn or taken damage since then. You can also end your rage on your turn as a bonus action. Once you have raged the number of times shown for your barbarian level in the Rages column of the Barbarian table, you must finish a long rest before you can rage again.",
                level=1
            ),
            ClassFeature(
                "Unarmored Defense.",
                "While you are not wearing any armor, your armor class equals 10 + your Dexterity modifier + your Constitution modifier. You can use a shield and still gain this benefit.",
                lcode="""if p.armor=="" and p.ac < (10 + (p.stats["Dex"] - 10) // 2 + (p.stats["Con"] - 10) // 2):\n\tp.ac = (10 + (p.stats["Dex"] - 10) // 2 + (p.stats["Con"] - 10) // 2)""",
                level=1
            ),
            ClassFeature(
                "Danger Sense",
                "At 2nd level, you gain an uncanny sense of when things nearby aren't as they should be, giving you an edge when you dodge away from danger. You have advantage on Dexterity saving throws against effects that you can see, such as traps and spells. To gain this benefit, you can't be blinded, deafened, or incapacitated.",
                level=2
            ),
            ClassFeature(
                "Reckless Attack",
                "Starting at 2nd level, you can throw aside all concern for defense to attack with fierce desperation. When you make your first attack on your turn, you can decide to attack recklessly. Doing so gives you advantage on melee weapon attack rolls using Strength during this turn, but attack rolls against you have advantage until your next turn.",
                level=2
            )
        ]

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
        self.c_name = "Fighter"

# class BearTotem(Barbarian):
#     def __init__(self):
#         super().__init__()
#         # self.stat_preference = choice([
#         #     ["Str", "Con", "Dex", "Wis", "Cha", "Int"],
#         #     ["Str", "Con", "Dex", "Wis", "Int", "Cha"]
#         # ])
#         self.sc_name = "BearTotem"

# class EagleTotem(Barbarian):
#     def __init__(self):
#         super().__init__()
#         # self.stat_preference = choice([
#         #     ["Str", "Dex", "Con", "Wis", "Cha", "Int"],
#         #     ["Str", "Dex", "Con", "Wis", "Int", "Cha"]
#         # ])
#         self.sc_name = "EagleTotem"

# class Swords(Bard):
#     def __init__(self):
#         super().__init__()
#         # self.stat_preference = choice([
#         #     ["Cha", "Dex", "Con", "Wis", "Str", "Int"],
#         #     ["Cha", "Dex", "Con", "Wis", "Int", "Str"]
#         # ])
#         self.sc_name = "Swords"

# class Valor(Bard):
#     def __init__(self):
#         super().__init__()
#         # self.stat_preference = choice([
#         #     ["Cha", "Con", "Dex", "Wis", "Str", "Int"],
#         #     ["Cha", "Con", "Dex", "Wis", "Int", "Str"]
#         # ])
#         self.sc_name = "Valor"

