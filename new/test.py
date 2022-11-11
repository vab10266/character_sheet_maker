import character as chartr
import expression as expr

my_character = chartr.CharacterHistory()


def add_race(race_name):
    def race_adder(char):
        char.cells['Race'].expr = expr.String(race_name)

        if race_name == 'Human':
            for stat in ['Strength', 'Dexterity', 'Constitution', 'Wisdom', 'Intelligence', 'Charisma']:
                cell_name = f'{stat} Score'
                char.cells[cell_name].expr += expr.Int(1)
    return race_adder


def add_class(class_name, class_level):
    def class_adder(char):
        char.cells['Class'].expr = expr.String(class_name)
        char.cells['Class Level'].expr = expr.Int(class_level)

        if class_name == 'Fighter':
            char.cells['Health Points'].expr = char.cells['Constitution Modifier'].expr + \
                expr.Int(10)
            char.cells['Hit Dice'].expr = expr.DiceThrow(expr.Int(1), expr.Int(10))
    return class_adder


def add_ability_scores(ability_scores):
    def ability_adder(char):
        for score in ability_scores:
            char.cells[score].expr += expr.Int(ability_scores[score])
    return ability_adder


my_character.update_with(add_race('Human'))
my_character.update_with(add_class('Fighter', 1))
my_character.update_with(add_ability_scores({
    'Strength Score': 12,
    'Dexterity Score': 15,
    'Constitution Score': 14,
    'Wisdom Score': 13,
    'Charisma Score': 10,
    'Intelligence Score': 8,
}))

print(my_character.cursor.value.describe())
