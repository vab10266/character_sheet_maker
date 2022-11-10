from typing import Dict
from utils import describe_choices
from tkinter import *

class Choice:
    def __init__(self, text: str, val:object) -> None:
        self.text = text
        self.val = val

class Decision:
    def __init__(self, text: str, choices: Dict[str, Choice]) -> None:
        self.text = text
        self.choices = choices
        self.chosen = None

    def choose(self, choice=None):
        if choice is None:
            print()
            print(self.text)
            while self.chosen is None:
                print(describe_choices(self.choices), end="")
                x = input()
                try:
                    self.chosen = self.choices[x].val
                except KeyError as e:
                    print("invalid")
        else:
            self.chosen = self.choices[choice].val
        return self.chosen
    
class GuiDecision(Decision):
    def __init__(self, root, text: str, choices: Dict[str, Choice]) -> None:
        super().__init__(text, choices)
        self.root = root
        self.w = []

        clbl = Label(self.root, text = self.text)
        clbl.grid(row=0, column=2)
        self.w += [clbl]

        self.v = StringVar(self.root, "1")
        # Dictionary to create multiple buttons
        
        # Loop is used to create multiple Radiobuttons
        # rather than creating each button separately
        r=0
        
        for (text, value) in self.choices.items():
            temp = Radiobutton(self.root, text = value.text, variable = self.v,
                        value = text, indicator = 0, width=20,
                        background = "light blue")
            self.w += [temp]
            temp.grid(row=r, column=3)
            r += 1
        btn = Button(self.root, text = "enter" ,
                command=self.choose)
        # Set Button Grid
        btn.grid(row=r, column=1)
        self.w += [btn]

    def choose(self, choice=None):
        if choice is None:

           
            print(type(self))
            self.chosen = self.choices[self.v.get()]
            print(self.chosen)
            for widget in self.w:
                widget.grid_remove()

            # while self.chosen is None:
            #     pass
            
        else:
            self.chosen = self.choices[choice].val
        return self.chosen