from character import Character
from char_class import *
from choice import Decision
from race import *
from choice import *
from utils import describe_features, show_stats
from equipment import armor_choices, weapon_choices
from feature import asi


# class_list = {"1": Barbarian, "2": Bard, "3": Fighter}
classes = {
    "1": Choice("Barbarian", Barbarian),
    "2": Choice("Bard", Bard),
    "3": Choice("Fighter", Fighter),
}
# race_list = {"1": Human, "21": HillDwarf, "22": MountainDwarf}
races = {
    "1": Choice("Human", Human),
    "21": Choice("Dwarf, Hill", HillDwarf),
    "22": Choice("Dwarf, Mountian", MountainDwarf),
}


class CharacterCreator:
    def __init__(self, custom=False):
        self.custom = custom

    def create(self):
        # player_char = Character()
        print("Select Character Level: ", end="")
        level = int(input())
        for l in range(level):
            char_class = None
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
                player_char = Character(char_class(), char_race())
            else:
                player_char.add_level(char_class(stats_set=True))
        return player_char
        

    
if __name__ == "__main__":
    c = CharacterCreator(True)
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
    asi(p)