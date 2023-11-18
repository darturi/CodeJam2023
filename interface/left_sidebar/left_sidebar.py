from tkinter import *
import tkinter.ttk as ttk

window = Tk()
window.title("Barth Daniel Juliette & Martin's Text Editor")
window.geometry('250x1010')

frame = Frame(window, bg='white', height=1010, width=250)
#frame.pack()


new_folder = Button(window, text="New Folder")
new_folder.configure(bg='mediumpurple', activebackground='blueviolet', font=('calibri', 12), relief=RAISED)

new_file = Button(window, text="New File")
new_file.configure(bg='mediumpurple', activebackground='blueviolet', font=('calibri', 12), relief=RAISED)

save = Button(window, text="Save As...")
save.configure(bg='mediumpurple', activebackground='blueviolet', font=('calibri', 12), relief=RAISED)

save.pack(side='bottom', fill='x', pady=20)
new_folder.pack(side='bottom', fill='x')
new_file.pack(side='bottom', fill='x')


# Dropdown file button
#options = ["File1", "Option 2", "Option 3", "Option 4"]
#dropdown_button = OptionMenu(window, selected_option, *options)



window.mainloop()
