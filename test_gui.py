# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Welcome to GeekForGeeks")
# Set geometry(widthxheight)
root.geometry('350x600')
def m_new():
	lbl.configure(text = "Are you a Geek?")

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
lbl = Label(root, text = "Are you a Geek?")
lbl.pack()

# adding Entry Field
txt = Entry(root, width=10)
txt.pack()


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
