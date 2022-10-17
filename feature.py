from utils import show_stats
from choice import Choice, Decision

class Feature:
    def __init__(self, title, text, gcode="", lcode=""):
        self.title = title
        self.text = text
        self.gcode = gcode
        self.lcode = lcode

    def gain(self, c):
        exec(self.gcode)

    def lvl_up(self, p):
        exec(self.lcode)

class ClassFeature(Feature):
    def __init__(self, title, text, gcode="", lcode="", level=1):
        super().__init__(title, text, gcode=gcode, lcode=lcode)
        self.level = level

def asi(char):
    stat_choices = {
        "1": Choice('Str', 'Str'),
        "2": Choice('Dex', 'Dex'),
        "3": Choice('Con', 'Con'),
        "4": Choice('Int', 'Int'),
        "5": Choice('Wis', 'Wis'),
        "6": Choice('Cha', 'Cha')    
    }
    print(show_stats(char.stats))
    fasi = Decision("Choose your first ASI:", stat_choices).choose()
    char.change_stat(fasi, 1)
    print(show_stats(char.stats))
    sasi = Decision("Choose your second ASI:", stat_choices).choose()
    char.change_stat(sasi, 1)
    print(show_stats(char.stats))
