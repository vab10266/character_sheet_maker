import expression as expr
import cell as cell


class Character(object):
    def __init__(self):
        basic = [
            'Race',
            'Class',
            'Class Level'
        ]

        stats = [
            # Strength
            'Strength Modifier',
            'Strength Score',
            'Strength Saving Throws',
            'Athletics',
            # Dexterity
            'Dexterity Modifier',
            'Dexterity Score',
            'Dexterity Saving Throws',
            'Acrobatics',
            'Sleight of Hand',
            'Stealth',
            # Constitution
            'Constitution Modifier',
            'Constitution Score',
            'Constitution Saving Throws',
            # Intelligence
            'Intelligence Modifier',
            'Intelligence Score',
            'Intelligence Saving Throws',
            'Arcana',
            'History',
            'Investigation',
            'Nature',
            'Religion',
            # Wisdom
            'Wisdom Modifier',
            'Wisdom Score',
            'Wisdom Saving Throws',
            'Animal Handling',
            'Insight',
            'Medicine',
            'Perception',
            'Survival',
            # Charisma
            'Charisma Modifier',
            'Charisma Score',
            'Charisma Saving Throws',
            'Deception',
            'Intimidation',
            'Performance',
            'Persuasion'
        ]

        misc = [
            'Proficiency',
            'Inspiration',
            'Passive Perception',
            'Passive Insight',
            'Armor Class',
            'Initiative',
            'Speed'
        ]

        extra = [
            'Hit Dice',
            'Health Points'
        ]

        all_cells = basic + stats + misc + extra
        self.cells = {
            cell_name: cell.Cell(
                cell_name,
                expr.Int(0))
            for cell_name
            in all_cells}

        for cell_name in ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']:
            score = f'{cell_name} Score'
            self.cells[f'{cell_name} Modifier'].expr = (
                expr.CellRef(score) - expr.Int(10)) // expr.Int(2)

    def copy(self):
        result = Character()
        result.cells = {
            name: cell.copy()
            for name, cell
            in self.cells.items()}
        return result


    def describe(self):
        return '\n'.join(
            f'{cell.name}: {cell.expr.describe()}, with val {cell.expr.evaluate(self.cells)}'
            for cell
            in self.cells.values())


class CharHistoryNode(object):
    def __init__(self, char):
        self.parent = None
        self.value = char
        self.children = []

    def add_child(self, new_char):
        new_node = CharHistoryNode(new_char)
        self.children.append(new_node)
        new_node.parent = self


class CharacterHistory(object):
    def __init__(self):
        self.cursor = CharHistoryNode(Character())

    def update_with(self, updater):
        previous = self.cursor
        new = CharHistoryNode(previous.value.copy())
        updater(new.value)
        previous.add_child(new)
        self.cursor = new

    def undo(self):
        previous = self.cursor.parent
        if previous is None:
            return
        else:
            self.cursor = previous
