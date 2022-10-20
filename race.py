from choice import Decision, Choice
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
        self.features += [
            Feature(
                "Ability Score Increase.",
                "Your ability scores each increase by 1.",
                gcode="""p.stats['Str'] += 1\np.stats['Dex'] += 1\np.stats['Con'] += 1\np.stats['Int'] += 1\np.stats['Wis'] += 1\np.stats['Cha'] += 1\n"""
            )
        ]

class Dwarf(Race):
    def __init__(self):
        super().__init__()
        self.speed = 25
        self.languages += ['Dwarven']
        self.features += [
            Feature(
                "Ability Score Increase.",
                "Your Constitution score increases by 2.",
                gcode="""p.stats['Con'] += 2"""
            ),
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
        subrace = Decision("Choose your subrace:", {'1': Choice("Hill Dwarf", "h"), '2': Choice("Mountain Dwarf", "m")}).choose()
        if subrace == 'h':
            self.features += [
            Feature(
                "Ability Score Increase.",
                "Your Wisdom score increases by 1.",
                gcode="""p.stats['Wis'] += 1"""
            ),
                Feature(
                    "Dwarven Toughness.",
                    "Your hit point maximum increases by 1, and it increases by 1 every time you gain a level.",
                    lcode="""p.hp += 1"""
                )
            ]
        else:
            self.features += [
            Feature(
                "Ability Score Increase.",
                "Your Strength  score increases by 2.",
                gcode="""p.stats['Str'] += 2"""
            ),
                Feature(
                    "Dwarven Armor Training.",
                    "You have proficiency with light and medium armor."
                )
            ]
            self.proficiencies += ["Light Armor", "Medium Armor"]

class Elf(Race):
    def __init__(self):
        super().__init__()
        self.speed = 30
        self.languages += ['Elven']
        self.proficiencies += ["Perception"]
        self.features += [
            Feature(
                "Ability Score Increase.",
                "Your Dexterity score increases by 2.",
                gcode="""p.stats['Dex'] += 2"""
            ),
            Feature(
                "Darkvision",
                "Accustomed to twilit forests and the night sky, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
            ),
            Feature(
                "Fey Ancestry",
                "You have advantage on saving throws against being charmed, and magic can't put you to sleep."
            ),
            Feature(
                "Trance",
                "Elves do not sleep. Instead they meditate deeply, remaining semi-conscious, for 4 hours a day. The Common word for this meditation is 'trance.' While meditating, you dream after a fashion; such dreams are actually mental exercises that have become reflexive after years of practice. After resting in this way, you gain the same benefit a human would from 8 hours of sleep."
            ),
        ]
        subrace = Decision("Choose your subrace:", {
            '1': Choice("High Elf", "h"), 
            '2': Choice("Wood Elf", "w"),
            '3': Choice("Dark Elf", "d")
        }).choose()
        if subrace == 'h':
            self.proficiencies += ["longsword", "shortsword", "shortbow", "longbow"]
            self.languages += ['*'] 
            self.features += [
                Feature(
                    "Ability Score Increase.",
                    "Your Intelligence score increases by 2.",
                    gcode="""p.stats['Int'] += 1"""
                ),
                Feature(
                    "Cantrip",
                    "You know one cantrip of your choice from the Wizard spell list. Intelligence is your spellcasting ability for it."
                ),
            ]
        elif subrace == 'w':
            self.proficiencies += ["longsword", "shortsword", "shortbow", "longbow"]
            self.speed = 35 
            self.features += [
                Feature(
                    "Ability Score Increase.",
                    "Your Wisdom score increases by 2.",
                    gcode="""p.stats['Wis'] += 1"""
                ),
                Feature(
                    "Mask of the Wild",
                    "You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena."
                ),
            ]
        else:
            self.proficiencies += ["rapier", "shortsword", "hand crossbow"]
            self.features += [
                Feature(
                    "Ability Score Increase.",
                    "Your Charisma score increases by 2.",
                    gcode="""p.stats['Cha'] += 1"""
                ),
                Feature(
                    "Superior Darkvision",
                    "Your darkvision has a range of 120 feet, instead of 60."
                ),
                Feature(
                    "Sunlight Sensitivity",
                    "You have disadvantage on attack rolls and Wisdom (Perception) checks that rely on sight when you, the target of the attack, or whatever you are trying to perceive is in direct sunlight."
                ),
                Feature(
                    "Drow Magic",
                    "You know the Dancing Lights cantrip. When you reach 3rd level, you can cast the Faerie Fire spell once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the Darkness spell onceand regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these spells."
                ),
            ]

class HalfOrc(Race):
    def __init__(self):
        super().__init__()
        self.languages += ['Orc']
        self.proficiencies += ['Intimidation']
        self.features += [
            Feature(
                "Ability Score Increase.",
                "Your Strength score increases by 2, and your Constitution score increases by 1.",
                gcode="""p.stats['Str'] += 2\np.stats['Con'] += 1"""
            ),
            Feature(
                "Darkvision",
                "Thanks to your orc blood, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
            ),
            Feature(
                "Relentless Endurance",
                "When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can't use this feature again until you finish a long rest."
            ),
            Feature(
                "Savage Attacks",
                "When you score a critical hit with a melee weapon attack, you can roll one of the weapon's damage dice one additional time and add it to the extra damage of the critical hit."
            ),
        ]
