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
        self.sc_lvl = 3
    
        self.c_name = "Barbarian"
        self.resources.update({
            'Rage': ['2']*2 + ['3']*3 + ['4']*6 + ['5']*5 + ['6']*3 + ['Unlimited'],
            'Rage Damage': ['+2']*8 + ['3']*7 + ['4']*5
        })
        self.features += [
            ClassFeature(
                "Rage",
                "In battle, you fight with primal ferocity. On your turn, you can enter a rage as a bonus action. While raging, you gain the following benefits if you aren't wearing heavy armor: You have advantage on Strength checks and Strength saving throws. When you make a melee weapon attack using Strength, you gain a bonus to the damage roll that increases as you gain levels as a barbarian, as shown in the Rage Damage column of the Barbarian table. You have resistance to bludgeoning, piercing, and slashing damage. If you are able to cast spells, you can't cast them or concentrate on them while raging. Your rage lasts for 1 minute. It ends early if you are knocked unconscious or if your turn ends and you haven't attacked a hostile creature since your last turn or taken damage since then. You can also end your rage on your turn as a bonus action. Once you have raged the number of times shown for your barbarian level in the Rages column of the Barbarian table, you must finish a long rest before you can rage again.",
                level=1
            ),
            ClassFeature(
                "Unarmored Defense.",
                "While you are not wearing any armor, your armor class equals 10 + your Dexterity modifier + your Constitution modifier. You can use a shield and still gain this benefit.",
                lcode="""if p.armor=="Unarmored" and p.ac < (10 + (p.stats["Dex"] - 10) // 2 + (p.stats["Con"] - 10) // 2):\n\tp.ac = (10 + (p.stats["Dex"] - 10) // 2 + (p.stats["Con"] - 10) // 2)\nelse:\n\tprint('oof')""",
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
            ),
            ClassFeature(
                "Subclass Choice",
                "At 3rd level, you choose a path that shapes the nature of your rage. Your choice grants you features at 3rd level and again at 6th, 10th, and 14th levels.",
                level=3,
                # gcode="p.add_subclass('Barbarian')"
            ),
            ClassFeature(
                "ASI.",
                "You can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1.",
                level=4,
                gcode="p.asi()"
            ),
            ClassFeature(
                "Extra Attack",
                "Beginning at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn.",
                level=5
            ),
            ClassFeature(
                "Fast Movement",
                "Starting at 5th level, your speed increases by 10 feet while you aren't wearing heavy armor.",
                level=5
            ),
            ClassFeature(
                "Feral Instinct",
                "By 7th level, your instincts are so honed that you have advantage on initiative rolls. Additionally, if you are surprised at the beginning of combat and aren't incapacitated, you can act normally on your first turn, but only if you enter your rage before doing anything else on that turn.",
                level=7
            ),
            ClassFeature(
                "ASI.",
                "You can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1.",
                level=8,
                gcode="p.asi()"
            ),
            ClassFeature(
                "Brutal Critical",
                "Beginning at 9th level, you can roll one additional weapon damage die when determining the extra damage for a critical hit with a melee attack. This increases to two additional dice at 13th level and three additional dice at 17th level.",
                level=9
            ),
            ClassFeature(
                "Relentless Rage",
                "Starting at 11th level, your rage can keep you fighting despite grievous wounds. If you drop to 0 hit points while you're raging and don't die outright, you can make a DC 10 Constitution saving throw. If you succeed, you drop to 1 hit point instead. Each time you use this feature after the first, the DC increases by 5. When you finish a short or long rest, the DC resets to 10.",
                level=11
            ),
            ClassFeature(
                "ASI.",
                "You can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1.",
                level=12,
                gcode="p.asi()"
            ),
            ClassFeature(
                "Persistent Rage",
                "Beginning at 15th level, your rage is so fierce that it ends early only if you fall unconscious or if you choose to end it.",
                level=15
            ),
            ClassFeature(
                "ASI.",
                "You can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1.",
                level=16,
                gcode="p.asi()"
            ),
            ClassFeature(
                "Indomitable Might",
                "Beginning at 18th level, if your total for a Strength check is less than your Strength score, you can use that score in place of the total.",
                level=18
            ),
            ClassFeature(
                "ASI.",
                "You can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1.",
                level=19,
                gcode="p.asi()"
            ),
            ClassFeature(
                "Primal Champion.",
                "At 20th level, you embody the power of the wilds. Your Strength and Constitution scores increase by 4. Your maximum for those scores is now 24.",
                level=20,
                gcode="""p.stats['Str'] += 4\np.stats['Con'] += 4"""
            ),
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

class Totem(Barbarian):
    def __init__(self, stats_set=True):
        super().__init__(stats_set)
        # self.stat_preference = choice([
        #     ["Str", "Con", "Dex", "Wis", "Cha", "Int"],
        #     ["Str", "Con", "Dex", "Wis", "Int", "Cha"]
        # ])
        self.sc_name = "Totem"
        self.features += [
            ClassFeature(
                "Spirit Seeker",
                "Yours is a path that seeks attunement with the natural world, giving you a kinship with beasts. At 3rd level when you adopt this path, you gain the ability to cast the Beast Sense and Speak with Animals spells, but only as rituals.",
                level=3
            ),
            ClassFeature(
                "Totem Spirit.",
                "At 3rd level, when you adopt this path, you choose a totem spirit and gain its feature. You must make or acquire a physical totem object – an amulet or similar adornment – that incorporates fur or feathers, claws, teeth, or bones of the totem animal. At your option, you also gain minor physical attributes that are reminiscent of your totem spirit. For example, if you have a bear totem spirit, you might be unusually hairy and thick-skinned, or if your totem is the eagle, your eyes turn bright yellow. Your totem animal might be an animal related to those listed here but more appropriate to your homeland. For example, you could choose a hawk or vulture in place of an eagle.",
                level=3,
                gcode=
                """totem3 = Decision("Choose your totem spirit:", {
                    "Bear": Choice("While raging, you have resistance to all damage except psychic damage. The spirit of the bear makes you tough enough to stand up to any punishment.", ClassFeature("Bear Totem 3", "While raging, you have resistance to all damage except psychic damage. The spirit of the bear makes you tough enough to stand up to any punishment.", level=3)),

                    "Eagle": Choice("While you're raging and aren't wearing heavy armor, other creatures have disadvantage on opportunity attack rolls against you, and you can use the Dash action as a bonus action on your turn. The spirit of the eagle makes you into a predator who can weave through the fray with ease.", ClassFeature("Eagle Totem 3", "While you're raging and aren't wearing heavy armor, other creatures have disadvantage on opportunity attack rolls against you, and you can use the Dash action as a bonus action on your turn. The spirit of the eagle makes you into a predator who can weave through the fray with ease.", level=3)),

                    "Elk": Choice("While you're raging and aren't wearing heavy armor, your walking speed increases by 15 feet. The spirit of the elk makes you extraordinarily swift.", ClassFeature("Elk Totem 3", "While you're raging and aren't wearing heavy armor, your walking speed increases by 15 feet. The spirit of the elk makes you extraordinarily swift.", level=3)),

                    "Tiger": Choice("While raging, you can add 10 feet to your long jump distance and 3 feet to your high jump distance. The spirit of the tiger empowers your leaps.", ClassFeature("Tiger Totem 3", "While raging, you can add 10 feet to your long jump distance and 3 feet to your high jump distance. The spirit of the tiger empowers your leaps.", level=3)),

                    "Wolf": Choice("While you're raging, your friends have advantage on melee attack rolls against any creature within 5 feet of you that is hostile to you. The spirit of the wolf makes you a leader of hunters.", ClassFeature("Wolf Totem 3", "While you're raging, your friends have advantage on melee attack rolls against any creature within 5 feet of you that is hostile to you. The spirit of the wolf makes you a leader of hunters.", level=3)),
                }).choose()\np.features += [totem3]
                """
            ),
            ClassFeature(
                "Aspect of the Beast",
                "At 6th level, you gain a magical benefit based on the totem animal of your choice. You can choose the same animal you selected at 3rd level or a different one.",
                level=6,
                gcode=
                """totem6 = Decision("Choose your totem spirit:", {
                    "Bear": Choice("You gain the might of a bear. Your carrying capacity (including maximum load and maximum lift) is doubled, and you have advantage on Strength checks made to push, pull, lift, or break objects.", ClassFeature("Bear Totem 6", "", level=6)),

                    "Eagle": Choice("You gain the eyesight of an eagle. You can see up to 1 mile away with no difficulty, able to discern even fine details as though looking at something no more than 100 feet away from you. Additionally, dim light doesn't impose disadvantage on your Wisdom (Perception) checks.", ClassFeature("Eagle Totem 6", "", level=6)),

                    "Elk": Choice("Whether mounted or on foot, your travel pace is doubled, as is the travel pace of up to ten companions while they're within 60 feet of you and you're not incapacitated. The elk spirit helps you roam far and fast.", ClassFeature("Elk Totem 6", "", level=6)),

                    "Tiger": Choice("You gain proficiency in two skills from the following list: Athletics, Acrobatics, Stealth, and Survival. The cat spirit hones your survival instincts.", ClassFeature("Tiger Totem 6", "", level=6)),

                    "Wolf": Choice("You gain the hunting sensibilities of a wolf. You can track other creatures while traveling at a fast pace, and you can move stealthily while traveling at a normal pace.", ClassFeature("Wolf Totem 6", "", level=6)),
                }).choose()\np.features += [totem6]
                """
            ),
            ClassFeature(
                "Spirit Walker",
                "At 10th level, you can cast the Commune with Nature spell, but only as a ritual. When you do so, a spiritual version of one of the animals you chose for Totem Spirit or Aspect of the Beast appears to you to convey the information you seek.",
                level=10
            ),
            ClassFeature(
                "Totemic Attunement",
                "At 14th level, you gain a magical benefit based on a totem animal of your choice. You can choose the same animal you selected previously or a different one.",
                level=14,
                gcode=
                """totem14 = Decision("Choose your totem spirit:", {
                    "Bear": Choice("While you're raging, any creature within 5 feet of you that's hostile to you has disadvantage on attack rolls against targets other than you or another character with this feature. An enemy is immune to this effect if it can't see or hear you or if it can't be frightened.", ClassFeature("Bear Totem 14", "While you're raging, any creature within 5 feet of you that's hostile to you has disadvantage on attack rolls against targets other than you or another character with this feature. An enemy is immune to this effect if it can't see or hear you or if it can't be frightened.", level=14)),

                    "Eagle": Choice("While raging, you have a flying speed equal to your current walking speed. This benefit works only in short bursts; you fall if you end your turn in the air and nothing else is holding you aloft.", ClassFeature("Eagle Totem 14", "While raging, you have a flying speed equal to your current walking speed. This benefit works only in short bursts; you fall if you end your turn in the air and nothing else is holding you aloft.", level=14)),

                    "Elk": Choice("While raging, you can use a bonus action during your move to pass through the space of a Large or smaller creature. That creature must succeed on a Strength saving throw (DC 8 + your Strength bonus + your proficiency bonus) or be knocked prone and take bludgeoning damage equal to 1d12 + your Strength modifier.", ClassFeature("Elk Totem 14", "While raging, you can use a bonus action during your move to pass through the space of a Large or smaller creature. That creature must succeed on a Strength saving throw (DC 8 + your Strength bonus + your proficiency bonus) or be knocked prone and take bludgeoning damage equal to 1d12 + your Strength modifier.", level=14)),

                    "Tiger": Choice("While you're raging, if you move at least 20 feet in a straight line toward a Large or smaller target right before making a melee weapon attack against it, you can use a bonus action to make an additional melee weapon attack against it.", ClassFeature("Tiger Totem 14", "While you're raging, if you move at least 20 feet in a straight line toward a Large or smaller target right before making a melee weapon attack against it, you can use a bonus action to make an additional melee weapon attack against it.", level=14)),

                    "Wolf": Choice("While you're raging, you can use a bonus action on your turn to knock a Large or smaller creature prone when you hit it with melee weapon attack.", ClassFeature("Wolf Totem 14", "While you're raging, you can use a bonus action on your turn to knock a Large or smaller creature prone when you hit it with melee weapon attack.", level=14)),
                }).choose()\np.features += [totem14]
                """
            ),
            ]

class Zealot(Barbarian):
    def __init__(self, stats_set=True):
        super().__init__(stats_set)
        # self.stat_preference = choice([
        #     ["Str", "Dex", "Con", "Wis", "Cha", "Int"],
        #     ["Str", "Dex", "Con", "Wis", "Int", "Cha"]
        # ])
        self.sc_name = "Zealot"
        self.features += [
            ClassFeature(
                "Divine Fury",
                "Starting when you choose this path at 3rd level, you can channel divine fury into your weapon strikes. While you're raging, the first creature you hit on each of your turns with a weapon attack takes extra damage equal to 1d6 + half your Barbarian level. The extra damage is necrotic or radiant; you choose the type of damage when you gain this feature.",
                level=3
            ),
            ClassFeature(
                "Warrior of the Gods",
                "At 3rd level, your soul is marked for endless battle. If a spell, such as Raise Dead, has the sole effect of restoring you to life (but not undeath), the caster doesn't need material components to cast the spell on you.",
                level=3
            ),
            ClassFeature(
                "Fanatical Focus",
                "Starting at 6th level, the divine power that fuels your rage can protect you. If you fail a saving throw while raging, you can reroll it, and you must use the new roll. You can use this ability only once per rage.",
                level=6
            ),
            ClassFeature(
                "Zealous Presence",
                "At 10th level, you learn to channel divine power to inspire zealotry in others. As a bonus action, you unleash a battle cry infused with divine energy. Up to ten other creatures of your choice within 60 feet of you that can hear you gain advantage on attack rolls and saving throws until the start of your next turn. Once you use this feature, you can’t use it again until you finish a long rest.",
                level=10
            ),
            ClassFeature(
                "Rage Beyond Death",
                "Beginning at 14th level, the divine power that fuels your rage allows you to shrug off fatal blows. While you're raging, having 0 hit points doesn’t knock you unconscious. You still must make death saving throws, and you suffer the normal effects of taking damage while at 0 hit points. However, if you would die due to failing death saving throws, you don’t die until your rage ends, and you die then only if you still have 0 hit points.",
                level=14
            ),
        ]

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

