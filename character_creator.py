from character import Character
from char_class import Bard
from classes.fighter import *
from classes.barbarian import *
from choice import Decision
from race import *
from choice import *
from utils import describe_features, show_stats
from equipment import armor_choices, weapon_choices


# class_list = {"1": Barbarian, "2": Bard, "3": Fighter}
classes = {
    "1": Choice("Barbarian", Barbarian),
    "2": Choice("Bard", Bard),
    "3": Choice("Fighter", Fighter),
}
# race_list = {"1": Human, "21": HillDwarf, "22": MountainDwarf}
races = {
    "1": Choice("Human", Human),
    "2": Choice("Dwarf", Dwarf),
    "3": Choice("Elf", Elf),
}


class CharacterCreator:
    def __init__(self, custom=False):
        self.custom = custom

    def create(self):
        # player_char = Character()
        print("Select Character Level: ", end="")
        level = int(input())
        char_race = None
        while char_race is None:
            """
            print("Level: " + str(l+1) + "\nChoose race:\n\t1: Human\n\tDwarf\n\t\t21: Hill Dwarf\n\t\t22: Mountain Dwarf\n: ", end="")
            c = input()
            try:
                char_race = race_list[c]
            except KeyError as e:
                print("invalid")
            """
            char_race = Decision("Choose race:", races).choose()
        first_class = None
        for l in range(level):
            char_class = None
            if self.custom is False:
                char_class = first_class
            while char_class is None:
                """
                print("Level: " + str(l+1) + "\n  Choose class:\n\t1: Barbarian\n\t\t11: BearTotem\n\t\t12: EagleTotem\n\t2: Bard\n\t\t21: Swords\n\t\t22: Valor\n: ", end="")
                c = input()
                try:
                    char_class = class_list[c]
                except KeyError as e:
                    print("invalid")
                """
                char_class = Decision("Choose class for level " + str(l+1) + ":", classes).choose()
            
            if l == 0:           
                first_class = char_class
                player_char = Character(first_class(), char_race())
            else:
                player_char.add_level(char_class(stats_set=True))
        player_char.process()        
        return player_char
        

    
if __name__ == "__main__":
    c = CharacterCreator(False)
    p = c.create()
    print(
        p.first_class,
        p.race,
        p.levels,
        p.stats,
        p.ac,
        p.speed,
        p.languages
    )
    # for f in p.features:
    #     print(f.title, "\t\t\t|", f.text)
    print(describe_features(p.features))
    exec("""print("hello world")""")
    
    print('ac: ', p.ac, '\nhp: ', p.hp)
    exec("")
    # temp = Decision("Choose your armor:", armor_choices).choose()

    # temp = Decision("Choose your weapon:", weapon_choices).choose()

    print(show_stats(p.stats))
    print(p.resources)
    print(p.proficiencies)
    # p.asi()