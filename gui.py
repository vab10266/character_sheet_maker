# Import Module
from tkinter import *
from character import Character
from char_class import Bard
from classes.fighter import *
from classes.barbarian import *
from choice import GuiDecision
from race import *
from choice import *
from utils import describe_features, show_stats, describe_char
from equipment import armor_choices, weapon_choices

_classes = {
    "1": Barbarian,
    "2": Bard,
    "3": Fighter,
}
# race_list = {"1": Human, "21": HillDwarf, "22": MountainDwarf}
_races = {
    "1": Human,
    "2": Elf,
    "3": Dwarf,
    "4": HalfOrc,

}

class_dict = {
    "1": Choice("Barbarian", Barbarian),
    "2": Choice("Bard", Bard),
    "3": Choice("Fighter", Fighter),
}
def m_new():
	root = GuiCharacterCreator()


		

class GuiCharacterCreator:
	def __init__(self):

		# create root window
		root = Tk()

		# root window title and dimension
		root.title("Welcome to GeekForGeeks")
		# Set geometry(widthxheight)
		root.geometry('600x600')

		# adding menu bar in root window
		# new item in menu bar labelled as 'New'
		# adding more items in the menu bar
		menu = Menu(root)
		# item = Menu(menu)
		# item.add_command(label='New')
		# menu.add_cascade(label='File', menu=item)
		root.config(menu=menu)
		filemenu = Menu(menu)
		menu.add_cascade(label='File', menu=filemenu)
		filemenu.add_command(label='New', command=m_new)
		filemenu.add_command(label='Open...')
		filemenu.add_separator()
		filemenu.add_command(label='Exit', command=root.quit)
		helpmenu = Menu(menu)
		menu.add_cascade(label='Help', menu=helpmenu)
		helpmenu.add_command(label='About')

		# adding a label to the root window
		rlbl = Label(root, text = "Choose your race: ")
		rlbl.grid(row=0, column=0)

		# adding Entry Field# Tkinter string variable
		# able to store any string value
		v1 = StringVar(root, "1")
		
		# Dictionary to create multiple buttons
		races = {"Human" : "1",
				"Elf" : "2",
				"Dwarf" : "3",
				"Half-Orc" : "4",
				}
		
		# Loop is used to create multiple Radiobuttons
		# rather than creating each button separately
		r = 0
		rbs = []
		for (text, value) in races.items():
			temp = Radiobutton(root, text = text, variable = v1,
						value = value, indicator = 0, width=20,
						background = "light blue")
			rbs += [temp]
			temp.grid(row=r, column=1)
			r += 1
		
		
		# adding a label to the root window
		clbl = Label(root, text = "Choose your class: ")
		clbl.grid(row=0, column=2)

		v2 = StringVar(root, "1")
		# Dictionary to create multiple buttons
		classes = {"Barbarian" : "1",
				"Bard" : "2",
				"Fighter" : "3"}
		
		# Loop is used to create multiple Radiobuttons
		# rather than creating each button separately
		max_r = r
		r=0
		
		for (text, value) in classes.items():
			temp = Radiobutton(root, text = text, variable = v2,
						value = value, indicator = 0, width=20,
						background = "light blue")
			rbs += [temp]
			temp.grid(row=r, column=3)
			r += 1

		if r > max_r:
			max_r = r
		r = max_r

		
		stats_lbl = Label(root, text = "Choose your stats: ")
		stats_lbl.grid(row=r, column=0)
		r += 1
		
		str_lbl = Label(root, text = "Strength: ")
		str_lbl.grid(row=r, column=0)
		str = Entry(root, width=10)
		str.grid(row=r, column=1)
		r += 1

		dex_lbl = Label(root, text = "Dexterity: ")
		dex_lbl.grid(row=r, column=0)
		dex = Entry(root, width=10)
		dex.grid(row=r, column=1)
		r += 1
		
		con_lbl = Label(root, text = "Constitution: ")
		con_lbl.grid(row=r, column=0)
		con = Entry(root, width=10)
		con.grid(row=r, column=1)
		r += 1

		int_lbl = Label(root, text = "Intelligence: ")
		int_lbl.grid(row=r, column=0)
		intel = Entry(root, width=10)
		intel.grid(row=r, column=1)
		r += 1
		
		wis_lbl = Label(root, text = "Wisdom: ")
		wis_lbl.grid(row=r, column=0)
		wis = Entry(root, width=10)
		wis.grid(row=r, column=1)
		r += 1

		cha_lbl = Label(root, text = "Charisma: ")
		cha_lbl.grid(row=r, column=0)
		cha = Entry(root, width=10)
		cha.grid(row=r, column=1)
		r += 1

			
		def choose_class():
			choice = GuiDecision(root, 'Choose a class to level up: ', class_dict)
			# c = choice.choose()
			# print(type(c))
			# while choice.chosen is None:
			# 	pass
		# 	clbl = Label(root, text = "Choose your class: ")
		# 	clbl.grid(row=0, column=0)

		# 	v3 = StringVar(root, "1")
		# 	# Dictionary to create multiple buttons
		# 	classes = {"Barbarian" : "1",
		# 			"Bard" : "2",
		# 			"Fighter" : "3"}
			
		# 	# Loop is used to create multiple Radiobuttons
		# 	# rather than creating each button separately
		# 	r=0
		# 	rbs = []
		# 	for (text, value) in classes.items():
		# 		temp = Radiobutton(root, text = text, variable = v3,
		# 					value = value, indicator = 0, width=20,
		# 					background = "light blue")
		# 		rbs += [temp]
		# 		temp.grid(row=r, column=2)
		# 		r += 1
		# 	def select_class():
		# 		print(v3.get())
		# 	btn = Button(root, text = "select" ,
		# 				command=select_class)
		# 	# Set Button Grid
		# 	btn.grid(row=r, column=2)


		def clicked():
			print(v1.get())
			print(v2.get())
			stats = {
                "Str": int(str.get()), 
                "Dex": int(dex.get()),
                "Con": int(con.get()), 
                "Int": int(intel.get()), 
                "Wis": int(wis.get()), 
                "Cha": int(cha.get())
            }
			print(_classes[v2.get()], _races[v1.get()])
			player_char = Character(_classes[v2.get()](stats_set=True), _races[v1.get()](), stats)

			for rb in rbs:
				rb.grid_remove()
			# btn.destroy()
			rlbl.grid_remove()
			clbl.grid_remove()
			stats_lbl.grid_remove()
			str_lbl.grid_remove()
			dex_lbl.grid_remove()
			con_lbl.grid_remove()
			int_lbl.grid_remove()
			wis_lbl.grid_remove()
			cha_lbl.grid_remove()
			str.grid_remove()
			dex.grid_remove()
			con.grid_remove()
			intel.grid_remove()
			wis.grid_remove()
			cha.grid_remove()
			btn.grid_remove()
			choose_class()

		# button widget with red color text inside
		btn = Button(root, text = "enter" ,
					command=clicked)
		# Set Button Grid
		btn.grid(row=r, column=2)
		
		root.mainloop()
if __name__ == '__main__':
	g = GuiCharacterCreator()
"""
# function to display user text when
# button is clicked
def clicked():
	res = "You wrote " + txt.get()
	lbl.configure(text = res)

# button widget with red color text inside
btn = Button(root, text = "Click me" ,
			command=clicked)
# Set Button Grid
btn.pack()

Lb = Listbox(root)
Lb.insert(1, 'Python')
Lb.insert(2, 'Java')
Lb.insert(3, 'C++')
Lb.insert(4, 'Any other')
Lb.pack()
# Execute Tkinter
# filemenu.add_command(label='New', command=m_new)
w = Spinbox(root, from_ = 0, to = 10)
w.pack()


# Python3 program to get selected
# # value(s) from tkinter listbox

# # Import tkinter
# from tkinter import *

# # Create the root window
# root = Tk()
# root.geometry('180x200')

# Create a listbox
listbox = Listbox(root, width=40, height=10, selectmode=MULTIPLE)

# Inserting the listbox items
listbox.insert(1, "Data Structure")
listbox.insert(2, "Algorithm")
listbox.insert(3, "Data Science")
listbox.insert(4, "Machine Learning")
listbox.insert(5, "Blockchain")
listbox.insert(6, "Data Structure")
listbox.insert(7, "Algorithm")
listbox.insert(8, "Data Science")
listbox.insert(9, "Machine Learning")
listbox.insert(10, "Blockchain")

# Function for printing the
# selected listbox value(s)
def selected_item():
	
	# Traverse the tuple returned by
	# curselection method and print
	# corresponding value(s) in the listbox
	for i in listbox.curselection():
		print(listbox.get(i))

# Create a button widget and
# map the command parameter to
# selected_item function
btn = Button(root, text='Print Selected', command=selected_item)

# Placing the button and listbox
btn.pack(side='bottom')
listbox.pack()


root.mainloop()
"""