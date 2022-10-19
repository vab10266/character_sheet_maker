from typing import Dict
from utils import describe_choices

class Choice:
    def __init__(self, text: str, val:object) -> None:
        self.text = text
        self.val = val

class Decision:
    def __init__(self, text: str, choices: Dict[str, Choice]) -> None:
        self.text = text
        self.choices = choices
        self.chosen = None

    def choose(self):
        print()
        print(self.text)
        while self.chosen is None:
            print(describe_choices(self.choices), end="")
            x = input()
            try:
                self.chosen = self.choices[x].val
            except KeyError as e:
                print("invalid")
        return self.chosen
    
