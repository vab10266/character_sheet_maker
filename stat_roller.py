from random import randint
class StatRoller:
    def __init__(self, mode):
        self.mode = mode
    
    def roll_stats(self):
        if self.mode == '3d6':
            return StatRoller.roll_3d6()
        if self.mode == '2d6p6':
            return StatRoller.roll_2d6p6()

    def roll_3d6():
        return [ 
            randint(1, 6) + randint(1, 6) + randint(1, 6),
            randint(1, 6) + randint(1, 6) + randint(1, 6),
            randint(1, 6) + randint(1, 6) + randint(1, 6),
            randint(1, 6) + randint(1, 6) + randint(1, 6),
            randint(1, 6) + randint(1, 6) + randint(1, 6),
            randint(1, 6) + randint(1, 6) + randint(1, 6)
        ]

    def roll_2d6p6():
        return [ 
            randint(1, 6) + randint(1, 6) + 6,
            randint(1, 6) + randint(1, 6) + 6,
            randint(1, 6) + randint(1, 6) + 6,
            randint(1, 6) + randint(1, 6) + 6,
            randint(1, 6) + randint(1, 6) + 6,
            randint(1, 6) + randint(1, 6) + 6,
        ]
