from char_class import Class
from feature import ClassFeature
from choice import *

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
        # self.resources.update({
        #     'Action Surge': ['0'] + ['1']*16 + ['2']*3,
        #     'Indomitable': ['0']*8 + ['1']*4 + ['2']*4 + ['3']*4
        # })
        self.features += [
            ClassFeature(
                "Fighting Style.",
                "You adopt a particular style of fighting as your specialty. Choose one of the following options. You can't take a Fighting Style option more than once, even if you later get to choose again.",
                level=1,
                gcode=
                """fs = Decision("Choose a fighting style:", {
                    '1': Choice("Archery.", Feature("Archery", "You gain a +2 bonus to attack rolls you make with ranged weapons.")),
                    '2': Choice("Blind Fighting.", Feature("Blind Fighting", "You have blindsight with a range of 10 feet. Within that range, you can effectively see anything that isn't behind total cover, even if you're blinded or in darkness. Moreover, you can see an invisible creature within that range, unless the creature successfully hides from you.")),
                    '3': Choice("Defense.", Feature("Defense", "While you are wearing armor, you gain a +1 bonus to AC.")),
                    '4': Choice("Dueling.", Feature("Dueling", "When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.")),
                    '5': Choice("Great Weapon Fighting.", Feature("Great Weapon Fighting", "When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll, even if the new roll is a 1 or a 2. The weapon must have the two-handed or versatile property for you to gain this benefit.")),
                    '6': Choice("Interception.", Feature("Interception", "When a creature you can see hits a target, other than you, within 5 feet of you with an attack, you can use your reaction to reduce the damage the target takes by 1d10 + your proficiency bonus (to a minimum of 0 damage). You must be wielding a shield or a simple or martial weapon to use this reaction.")),
                    '7': Choice("Protection.", Feature("Protection", "When a creature you can see attacks a target other than you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield.")),
                    '8': Choice("Superior Technique.", Feature("Superior Technique", "You learn one maneuver of your choice from among those available to the Battle Master archetype. If a maneuver you use requires your target to make a saving throw to resist the maneuver's effects, the saving throw DC equals 8 + your proficiency bonus + your Strength or Dexterity modifier (your choice.) You gain one superiority die, which is a d6 (this die is added to any superiority dice you have from another source). This die is used to fuel your maneuvers. A superiority die is expended when you use it. You regain your expended superiority dice when you finish a short or long rest.")),
                    '9': Choice("Thrown Weapon Fighting.", Feature("Thrown Weapon Fighting", "You can draw a weapon that has the thrown property as part of the attack you make with the weapon. In addition, when you hit with a ranged attack using a thrown weapon, you gain a +2 bonus to the damage roll.")),
                    '10': Choice("Two-Weapon Fighting.", Feature("Two-Weapon Fighting", "When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack.")),
                    '11': Choice("Unarmed Fighting.", Feature("Unarmed Fighting", "Your unarmed strikes can deal bludgeoning damage equal to 1d6 + your Strength modifier on a hit. If you aren't wielding any weapons or a shield when you make the attack roll, the d6 becomes a d8. At the start of each of your turns, you can deal 1d4 bludgeoning damage to one creature grappled by you.")),
                }).choose()\np.features += [fs]"""
            ),
            ClassFeature(
                "Second Wind",
                "You have a limited well of stamina that you can draw on to protect yourself from harm. On your turn, you can use a bonus action to regain hit points equal to 1d10 + your fighter level. Once you use this feature, you must finish a short or long rest before you can use it again.",
                level=1
            ),
            ClassFeature(
                "Action Surge",
                "Starting at 2nd level, you can push yourself beyond your normal limits for a moment. On your turn, you can take one additional action. Once you use this feature, you must finish a short or long rest before you can use it again. Starting at 17th level, you can use it twice before a rest, but only once on the same turn.",
                level=2,
                lcode="""arr = ['0'] + ['1']*16 + ['2']*3\np.resources.update({'Action Surge': arr[p.levels['Fighter']-1]})"""
            ),
            ClassFeature(
                "Martial Archetype",
                "At 3rd level, you choose an archetype that you strive to emulate in your combat styles and techniques. The archetype you choose grants you features at 3rd level and again at 7th, 10th, 15th, and 18th level.",
                level=3
            ),
            ClassFeature(
                "Extra Attack",
                "Beginning at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn. The number of attacks increases to three when you reach 11th level in this class and to four when you reach 20th level in this class.",
                level=5
            ),
            ClassFeature(
                "Martial Archetype",
                "At 3rd level, you choose an archetype that you strive to emulate in your combat styles and techniques. The archetype you choose grants you features at 3rd level and again at 7th, 10th, 15th, and 18th level.",
                level=3
            ),
            ClassFeature(
                "ASI.",
                "You can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1.",
                level=6,
                gcode="p.asi()"
            ),
            ClassFeature(
                "Indomitable",
                "Beginning at 9th level, you can reroll a saving throw that you fail. If you do so, you must use the new roll, and you can't use this feature again until you finish a long rest. You can use this feature twice between long rests starting at 13th level and three times between long rests starting at 17th level.",
                level=9,
                lcode="""arr = ['0']*8 + ['1']*4 + ['2']*4 + ['3']*4\np.resources.update({'Indomitable': arr[p.levels['Fighter']-1]})"""
                
            ),
            ClassFeature(
                "Martial Archetype",
                "At 3rd level, you choose an archetype that you strive to emulate in your combat styles and techniques. The archetype you choose grants you features at 3rd level and again at 7th, 10th, 15th, and 18th level.",
                level=3
            ),
            ClassFeature(
                "ASI.",
                "You can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1.",
                level=12,
                gcode="p.asi()"
            ),
            ClassFeature(
                "ASI.",
                "You can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1.",
                level=14,
                gcode="p.asi()"
            ),
            ClassFeature(
                "ASI.",
                "You can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1.",
                level=16,
                gcode="p.asi()"
            ),
            ClassFeature(
                "ASI.",
                "You can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1.",
                level=19,
                gcode="p.asi()"
            ),

        ]

class Champion(Fighter):
    def __init__(self, stats_set=True):
        super().__init__(stats_set)
        self.sc_name = "Champion"
        self.features += [
            ClassFeature(
                "Improved Critical",
                "Beginning when you choose this archetype at 3rd level, your weapon attacks score a critical hit on a roll of 19 or 20.",
                level=3
            ),
            ClassFeature(
                "Remarkable Athlete",
                "Starting at 7th level, you can add half your proficiency bonus (rounded up) to any Strength, Dexterity, or Constitution check you make that doesn't already use your proficiency bonus. In addition, when you make a running long jump, the distance you can cover increases by a number of feet equal to your Strength modifier.",
                level=7
            ),
            ClassFeature(
                "Additional Fighting Style.",
                "At 10th level, you can choose a second option from the Fighting Style class feature. You can't take a Fighting Style option more than once, even if you later get to choose again.",
                level=10,
                gcode=
                """fs = Decision("Choose a fighting style:", {
                    '1': Choice("Archery.", Feature("Archery", "You gain a +2 bonus to attack rolls you make with ranged weapons.")),
                    '2': Choice("Blind Fighting.", Feature("Blind Fighting", "You have blindsight with a range of 10 feet. Within that range, you can effectively see anything that isn't behind total cover, even if you're blinded or in darkness. Moreover, you can see an invisible creature within that range, unless the creature successfully hides from you.")),
                    '3': Choice("Defense.", Feature("Defense", "While you are wearing armor, you gain a +1 bonus to AC.")),
                    '4': Choice("Dueling.", Feature("Dueling", "When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.")),
                    '5': Choice("Great Weapon Fighting.", Feature("Great Weapon Fighting", "When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll, even if the new roll is a 1 or a 2. The weapon must have the two-handed or versatile property for you to gain this benefit.")),
                    '6': Choice("Interception.", Feature("Interception", "When a creature you can see hits a target, other than you, within 5 feet of you with an attack, you can use your reaction to reduce the damage the target takes by 1d10 + your proficiency bonus (to a minimum of 0 damage). You must be wielding a shield or a simple or martial weapon to use this reaction.")),
                    '7': Choice("Protection.", Feature("Protection", "When a creature you can see attacks a target other than you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield.")),
                    '8': Choice("Superior Technique.", Feature("Superior Technique", "You learn one maneuver of your choice from among those available to the Battle Master archetype. If a maneuver you use requires your target to make a saving throw to resist the maneuver's effects, the saving throw DC equals 8 + your proficiency bonus + your Strength or Dexterity modifier (your choice.) You gain one superiority die, which is a d6 (this die is added to any superiority dice you have from another source). This die is used to fuel your maneuvers. A superiority die is expended when you use it. You regain your expended superiority dice when you finish a short or long rest.")),
                    '9': Choice("Thrown Weapon Fighting.", Feature("Thrown Weapon Fighting", "You can draw a weapon that has the thrown property as part of the attack you make with the weapon. In addition, when you hit with a ranged attack using a thrown weapon, you gain a +2 bonus to the damage roll.")),
                    '10': Choice("Two-Weapon Fighting.", Feature("Two-Weapon Fighting", "When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack.")),
                    '11': Choice("Unarmed Fighting.", Feature("Unarmed Fighting", "Your unarmed strikes can deal bludgeoning damage equal to 1d6 + your Strength modifier on a hit. If you aren't wielding any weapons or a shield when you make the attack roll, the d6 becomes a d8. At the start of each of your turns, you can deal 1d4 bludgeoning damage to one creature grappled by you.")),
                }).choose()\np.features += [fs]"""
            ),
            ClassFeature(
                "Superior Critical",
                "Starting at 15th level, your weapon attacks score a critical hit on a roll of 18-20.",
                level=15
            ),
            ClassFeature(
                "Survivor",
                "At 18th level, you attain the pinnacle of resilience in battle. At the start of each of your turns, you regain hit points equal to 5 + your Constitution modifier if you have no more than half of your hit points left. You don't gain this benefit if you have 0 hit points.",
                level=18
            ),
        ]

class BattleMaster(Fighter):
    def __init__(self, stats_set=True):
        super().__init__(stats_set)
        self.sc_name = "BattleMaster"
        self.resources.update({
            'Superiority Dice': ['0']*2 + ['4d8']*4 + ['5d8']*3 + ['5d10']*5 + ['6d10']*3 + ['6d12']*3,
            'Maneuvers Known': ['0']*2 + ['3']*4 + ['5']*3 + ['7']*5 + ['9']*6
        })
        self.features += [
            ClassFeature(
                "Combat Superiority",
                "When you choose this archetype at 3rd level, you learn maneuvers that are fueled by special dice called superiority dice. Maneuvers. You learn three maneuvers of your choice. Many maneuvers enhance an attack in some way. You can use only one maneuver per attack. You learn two additional maneuvers of your choice at 7th, 10th, and 15th level. Each time you learn new maneuvers, you can also replace one maneuver you know with a different one. Superiority Dice. You have four superiority dice, which are d8s. A superiority die is expended when you use it. You regain all of your expended superiority dice when you finish a short or long rest. You gain another superiority die at 7th level and one more at 15th level. Saving Throws. Some of your maneuvers require your target to make a saving throw to resist the maneuver's effects. The saving throw DC is calculated as follows: Maneuver save DC = 8 + your proficiency bonus + your Strength or Dexterity modifier (your choice)",
                level=3,
                lcode=
                """print(p.resources['Maneuvers Known'])\nprint(p.levels['Fighter']-1)\nnm = int(p.resources['Maneuvers Known'])\nprint(nm)\nfor i in range(nm):\n\tprint('test')"""
            ),
            ClassFeature(
                "Student of War",
                "At 3rd level, you gain proficiency with one type of artisan's tools of your choice.",
                level=3
            ),
            ClassFeature(
                "Know Your Enemy",
                "Starting at 7th level, if you spend at least 1 minute observing or interacting with another creature outside combat, you can learn certain information about its capabilities compared to your own. The DM tells you if the creature is your equal, superior, or inferior in regard to two of the following characteristics of your choice: (Strength score, Dexterity score, Constitution score, Armor Class, Current hit points, Total class levels if any, Fighter class levels if any)",
                level=7
            ),
            ClassFeature(
                "Improved Combat Superiority.",
                "At 10th level, your superiority dice turn into d10s. At 18th level, they turn into d12s.",
                level=10
            ),
            ClassFeature(
                "Relentless",
                "Starting at 15th level, when you roll initiative and have no superiority dice remaining, you regain 1 superiority die.",
                level=15
            ),
        ]