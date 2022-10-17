from typing import List

from choice import Choice


class Armor:
    def __init__(self, name: str, ty: str, ac: int, stealth_dis: bool=False, str: int=None) -> None:
        self.name = name
        self.ty = ty
        self.ac = ac
        self.stealth_dis = stealth_dis

    def to_choice(self):
        return Choice(self.name, self)
        
class Weapon:
    def __init__(self, name: str, dmg: str, ty: str, dty: str, properties: List=[]) -> None:
        self.ty = ty
        self.name = name
        self.dmg = dmg
        self.dty = dty
        self.properties = properties
        
    def to_choice(self):
        return Choice(self.name, self)



armor_list = {
    "Unarmored": Armor(
        "Unarmored", 
        'None', 
        10,
        True
    ),
    "Padded": Armor(
        "Padded", 
        'Light', 
        11,
        True
    ),
    "Leather": Armor(
        "Leather", 
        'Light', 
        11
    ),
    "Studded Leather": Armor(
        "Studded Leather", 
        'Light', 
        11
    ),

    
    "Hide": Armor(
        "Hide", 
        'Medium', 
        12
    ),
    "Chain Shirt": Armor(
        "Chain Shirt", 
        'Medium', 
        13
    ),
    "Scale Mail": Armor(
        "Scale Mail", 
        'Medium', 
        14,
        True
    ),
    "Spiked Armor": Armor(
        "Spiked Armor", 
        'Medium', 
        14,
        True
    ),
    "Breastplate": Armor(
        "Breastplate", 
        'Medium', 
        14
    ),
    "Halfplate": Armor(
        "Halfplate", 
        'Medium', 
        15,
        True
    ),

    
    "Ring Mail": Armor(
        "Ring Mail", 
        'Heavy', 
        14,
        True
    ),
    "Chain Mail": Armor(
        "Chain Mail", 
        'Heavy', 
        16,
        True,
        13
    ),
    "Splint": Armor(
        "Split", 
        'Heavy', 
        17,
        True,
        15
    ),
    "Plate": Armor(
        "Plate", 
        'Heavy', 
        18,
        True,
        15
    ),
}

weapon_list = {
    "Unarmed": Weapon(
        "Unarmed",
        "1d1",
        "Simple",
        "bludgeoning",
        []
    ),
    "Club": Weapon(
        "Club",
        "1d4",
        "Simple",
        "bludgeoning",
        ["Light"]
    ),
    "Dagger": Weapon(
        "Dagger",
        "1d4",
        "Simple",
        "piercing",
        ["Finesse", "Light", "Thrown (20/60)"]
    ),
    "Greatclub": Weapon(
        "Greatclub",
        "1d8",
        "Simple",
        "bludgeoning",
        ["Two-handed"]
    ),
    "Handaxe": Weapon(
        "Handaxe",
        "1d6",
        "Simple",
        "slashing",
        ["Light", "Thrown (20/60)"]
    ),
    "Javelin": Weapon(
        "Javelin",
        "1d6",
        "Simple",
        "piercing",
        ["Light", "Thrown (30/120)"]
    ),
    "Light hammer": Weapon(
        "Light hammer",
        "1d4",
        "Simple",
        "bludgeoning",
        ["Light", "Thrown (20/60)"]
    ),
    "Mace": Weapon(
        "Mace",
        "1d6",
        "Simple",
        "bludgeoning",
        []
    ),
    "Quarterstaff": Weapon(
        "Quarterstaff",
        "1d6",
        "Simple",
        "bludgeoning",
        ["Versatile (1d8)"]
    ),
    "Sickle": Weapon(
        "Sickle",
        "1d4",
        "Simple",
        "slashing",
        ["Light"]
    ),
    "Spear": Weapon(
        "Spear",
        "1d6",
        "Simple",
        "piercing",
        ["Thrown (20/60), versatile (1d8)"]
    ),
    
    "Crossbow, light": Weapon(
        "Crossbow, light",
        "1d8",
        "Simple",
        "bludgeoning",
        ["Ammunition", "range (80/320)", "loading", "two-handed"]
    ),
    "Dart": Weapon(
        "Dart",
        "1d4",
        "Simple",
        "piercing",
        ["Finesse", "thrown (20/60)"]
    ),
    "Shortbow": Weapon(
        "Shortbow",
        "1d6",
        "Simple",
        "piercing",
        ["Ammunition", "range (80/320)", "two-handed"]
    ),
    "Sling": Weapon(
        "Sling",
        "1d4",
        "Simple",
        "piercing",
        ["Ammunition", "range (30/120)"]
    ),

    "Battleaxe": Weapon(
        "Battleaxe",
        "1d8",
        "Martial",
        "slashing",
        ["Versatile (1d10)"]
    ),
    "Flail": Weapon(
        "Flail",
        "1d8",
        "Martial",
        "bludgeoning",
        []
    ),
    "Glaive": Weapon(
        "Glaive",
        "1d10",
        "Martial",
        "slashing",
        ["Heavy", "reach", "two-handed"]
    ),
    "Greataxe": Weapon(
        "Greataxe",
        "1d12",
        "Martial",
        "slashing",
        ["Heavy", "two-handed"]
    ),
    "Greatsword": Weapon(
        "Greatsword",
        "2d6",
        "Martial",
        "slashing",
        ["Heavy", "two-handed"]
    ),
    "Halberd": Weapon(
        "Halberd",
        "1d10",
        "Martial",
        "slashing",
        ["Heavy", "reach", "two-handed"]
    ),
    "Lance": Weapon(
        "Lance",
        "1d12",
        "Martial",
        "piercing",
        ["Reach", "You have disadvantage when you use a lance to attack a target within 5 feet of you. Also, a lance requires two hands to wield when you aren't mounted."]
    ),
    "Longsword": Weapon(
        "Longsword",
        "1d8",
        "Martial",
        "slashing",
        ["Versatile (1d10)"]
    ),
    "Maul": Weapon(
        "Maul",
        "2d6",
        "Martial",
        "bludgeoning",
        ["Heavy", "two-handed"]
    ),
    "Morningstar": Weapon(
        "Morningstar",
        "1d8",
        "Martial",
        "piercing",
        []
    ),
    "Pike": Weapon(
        "Pike",
        "1d10",
        "Martial",
        "piercing",
        ["Heavy", "reach", "two-handed"]
    ),
    "Rapier": Weapon(
        "Rapier",
        "1d8",
        "Martial",
        "piercing",
        ["Finesse"]
    ),
    "Scimitar": Weapon(
        "Scimitar",
        "1d6",
        "Martial",
        "slashing",
        ["Finesse", "light"]
    ),
    "Shortsword": Weapon(
        "Shortsword",
        "1d6",
        "Martial",
        "piercing",
        ["Finesse", "light"]
    ),
    "Trident": Weapon(
        "Trident",
        "1d6",
        "Martial",
        "piercing",
        ["Thrown (20/60)", "versatile (1d8)"]
    ),
    "War pick": Weapon(
        "War pick",
        "1d8",
        "Martial",
        "piercing",
        []
    ),
    "Warhammer": Weapon(
        "Warhammer",
        "1d8",
        "Martial",
        "bludgeoning",
        ["Versatile (1d10)"]
    ),
    "Whip": Weapon(
        "Whip",
        "1d4",
        "Martial",
        "slashing",
        ["Finesse", "reach"]
    ),
    
    "Blowgun": Weapon(
        "Blowgun",
        "1d1",
        "Martial",
        "piercing",
        ["Ammunition, range (25/100), loading"]
    ),
    "Crossbow, hand": Weapon(
        "Crossbow, hand",
        "1d6",
        "Martial",
        "piercing",
        ["Ammunition", "range (30/120)", "light", "loading"]
    ),
    "Crossbow, heavy": Weapon(
        "Crossbow, heavy",
        "1d10",
        "Martial",
        "piercing",
        ["Versatile"]
    ),
    "Longbow": Weapon(
        "Longbow",
        "1d8",
        "Martial",
        "piercing",
        ["Ammunition", "range (150/600)", "heavy", "two-Handed"]
    ),
    "Net": Weapon(
        "Net",
        "0d1",
        "Martial",
        "",
        ["Thrown (5/15)", " A Large or smaller creature hit by a net is restrained until it is freed. A net has no effect on creatures that are formless, or creatures that are Huge or larger. A creature can use its action to make a DC 10 Strength check, freeing itself or another creature within its reach on a success. Dealing 5 slashing damage to the net (AC 10) also frees the creature without harming it, ending the effect and destroying the net. When you use an action, bonus action, or reaction to attack with a net, you can make only one attack regardless of the number of attacks you can normally make."]
    ),
}

armor_choices = {}
for i in range(len(armor_list)):
    key = list(armor_list.keys())[i]
    val = armor_list[key]
    armor_choices[str(1+i)] = val.to_choice()

weapon_choices = {}
for i in range(len(weapon_list)):
    key = list(weapon_list.keys())[i]
    val = weapon_list[key]
    weapon_choices[str(1+i)] = val.to_choice()