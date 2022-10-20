from utils import show_stats
from choice import Choice, Decision

class Feature:
    def __init__(self, title, text, gcode="", lcode=""):
        self.title = title
        self.text = text
        self.gcode = gcode
        self.lcode = lcode
        self.level = 0

    def gain(self, p):
        exec(self.gcode)

    def update(self, p):
        print(self.lcode)
        exec(self.lcode)

class ClassFeature(Feature):
    def __init__(self, title, text, gcode="", lcode="", level=1):
        super().__init__(title, text, gcode=gcode, lcode=lcode)
        self.level = level


