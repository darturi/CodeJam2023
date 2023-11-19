import tkinter as tk
from datetime import datetime
from PIL import Image, ImageTk

# Main Window
window = tk.Tk()
window.title("Notes")
window.geometry("800x600")

# Top bar
header = tk.Frame(window, bg="#8a2be2", height=50)
header.pack(fill=tk.X)

# Title and Date
title = tk.Label(header, text="OurNotes", font=("Arial", 20, "bold"), bg="#8a2be2", fg="white")
title.pack(side=tk.LEFT, padx=10)

def update_date_label():
    today = datetime.now().strftime("%B %d, %Y")
    date.config(text=today,font=("Times New Roman", 20, "bold"))

def increase_font_size():
    current_size = text.cget("font").split(" ")[-1]
    new_size = int(current_size) + 2
    text.configure(font=("Arial", new_size))

# Function to decrease the text size
def decrease_font_size():
    current_size = text.cget("font").split(" ")[-1]
    new_size = max(8, int(current_size) - 2)  # Ensure the font size doesn't go below 8
    text.configure(font=("Arial", new_size))

def toggle_text_underline():
    start_index = text.index("sel.first")
    end_index = text.index("sel.last")
    tags = text.tag_names(start_index)
    current_size = text.cget("font").split(" ")[-1]

    if "underline" in tags:
        text.tag_remove("underline", start_index, end_index)
        text.tag_configure("normal", font=("Arial", current_size))

    else:
        text.tag_add("underline", start_index, end_index)
        if "bold" and "italic" in tags:
            text.tag_configure("underline", font=("Arial", current_size, "underline", "bold", "italic"))
        elif "italic" in tags:
            text.tag_configure("underline", font=("Arial", current_size, "underline", "italic"))
        elif "bold" in tags:
            text.tag_configure("underline", font=("Arial", current_size, "underline", "bold"))
        else:
            text.tag_configure("underline", font=("Arial", current_size, "underline"))


def toggle_text_italic():
    start_index = text.index("sel.first")
    end_index = text.index("sel.last")
    tags = text.tag_names(start_index)
    current_size = text.cget("font").split(" ")[-1]
    if "italic" in tags:
        text.tag_remove("italic", start_index, end_index)
        text.tag_configure("normal", font=("Arial", current_size))
    else:
        text.tag_add("italic", start_index, end_index)
        if "bold" and "underline" in tags:
            text.tag_configure("italic", font=("Arial", current_size, "underline", "bold", "italic"))
        elif "underline" in tags:
            text.tag_configure("italic", font=("Arial", current_size, "underline", "italic"))
        elif "bold" in tags:
            text.tag_configure("italic", font=("Arial", current_size, "italic", "bold"))
        else:
            text.tag_configure("italic", font=("Arial", current_size, "italic"))


def toggle_text_bold():
    start_index = text.index("sel.first")
    end_index = text.index("sel.last")
    tags = text.tag_names(start_index)
    current_size = text.cget("font").split(" ")[-1]
    if "bold" in tags:
        text.tag_remove("bold", start_index, end_index)
        text.tag_configure("normal", font=("Arial", current_size))
    else:
        text.tag_add("bold", start_index, end_index)
        if "italic" and "underline" in tags:
            text.tag_configure("bold", font=("Arial", current_size, "underline", "bold", "italic"))
        elif "underline" in tags and "italic" not in tags:
            text.tag_configure("bold", font=("Arial", current_size, "underline", "bold"))
        elif "italic" in tags:
            text.tag_configure("bold", font=("Arial", current_size, "italic", "bold"))
        else:
            text.tag_configure("bold", font=("Arial", current_size, "bold"))

# Date Label
date = tk.Label(header, text="", font=("Arial", 12), bg="#8a2be2", fg="white")
date.pack(side=tk.RIGHT, padx=10)
update_date_label()

# Side Frame
sidebar = tk.Frame(window, bg="#f0f0f0", width=200)
sidebar.pack(side=tk.LEFT, fill=tk.Y)

# New Note and New Folder Buttons
new_note = tk.Button(sidebar, text="New Note", font=("Arial", 12), highlightbackground="#f0f0f0", fg="#8a2be2", width=15, borderwidth=0)
new_note.pack(side=tk.BOTTOM, padx=10, pady=10)
new_folder = tk.Button(sidebar, text="New Folder", font=("Arial", 12), highlightbackground="#f0f0f0", fg="#8a2be2", width=15, borderwidth=0)
new_folder.pack(side=tk.BOTTOM, padx=10, pady=10)

# List of Folders and Documents
folders = tk.LabelFrame(sidebar, text="Folders", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#8a2be2")
folders.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
folder_names = ["Folder #1", "Folder #2", "Folder #3", "Folder #4"]
for name in folder_names:
    folder = tk.Label(folders, text=name, font=("Arial", 12), bg="#f0f0f0", fg="black")
    folder.pack(anchor=tk.W, padx=10, pady=5)
notes = tk.LabelFrame(sidebar, text="Loose Notes", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#8a2be2")
notes.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
note_names = ["Loose Note #1"]
for name in note_names:
    note = tk.Label(notes, text=name, font=("Arial", 12), bg="#f0f0f0", fg="black")
    note.pack(anchor=tk.W, padx=10, pady=5)

# Note-taking area
main = tk.Frame(window, bg="white")
main.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Formatting Buttons
formatting = tk.Frame(main, bg="#f0f0f0", height=50)
formatting.pack(fill=tk.X)
options = ["Font", "Color"]

original_bold = Image.open('bold_b.png')
resized_bold = original_bold.resize((18,18), Image.Resampling.LANCZOS)
bold_image = ImageTk.PhotoImage(resized_bold)
bold_button = tk.Button(formatting, image=bold_image, command=toggle_text_bold, borderwidth=0)
bold_button.pack(side=tk.LEFT, padx=5, pady=10)

original_under = tk.PhotoImage(file='underlined_u.pgm')
underline_image = original_under.subsample(55,55)
underline_button = tk.Button(formatting, image=underline_image, borderwidth=0, command=toggle_text_underline)
underline_button.pack(side=tk.LEFT, padx=5, pady=10)

original_italic = Image.open('italic_i.png')
resized_italic = original_italic.resize((18,18), Image.Resampling.LANCZOS)
italic_image = ImageTk.PhotoImage(resized_italic)
italic_button = tk.Button(formatting, image=italic_image, borderwidth=0, command=toggle_text_italic)
italic_button.pack(side=tk.LEFT, padx=5, pady=10)

# Add code button
original_image_pil = Image.open('add_code.png')
resized_code = original_image_pil.resize((100,32))
code_image = ImageTk.PhotoImage(resized_code)
add_code_button = tk.Button(formatting, image=code_image, borderwidth=0, highlightbackground="#f0f0f0")
add_code_button.pack(side=tk.RIGHT, padx=10, pady=10)

def change_text_color(color):
    start_index = text.index("sel.first")
    end_index = text.index("sel.last")
    tag_name = f"highlight_{color}"
    text.tag_add(tag_name, start_index, end_index)
    text.tag_configure(tag_name, foreground=color)

# Create a list of 10 colors
color_options = ["Black", "Red", "Green", "Blue", "Purple", "Orange", "Brown", "Pink", "Gray", "Cyan"]

# Create a StringVar to store the selected color
selected_color = tk.StringVar()

# Set the default color
selected_color.set(color_options[0])

# Create an OptionMenu to choose the color
color_menu = tk.OptionMenu(formatting, selected_color, *color_options)
color_menu.configure(bg="#f0f0f0", fg="black", activeforeground="black")
color_menu.pack(pady=10, side=tk.LEFT)

# Create a button to apply the selected color
apply_button = tk.Button(formatting, text="Apply Color", command=lambda: change_text_color(selected_color.get()), highlightbackground="#f0f0f0")
apply_button.pack(pady=10, side=tk.LEFT)

# Add the "+" and "-" buttons for adjusting text size
decrease_button = tk.Button(formatting, text="-", font=("Arial", 12), bg="#f0f0f0", fg="black", command=decrease_font_size, borderwidth=0, highlightbackground="#f0f0f0")
decrease_button.pack(side=tk.LEFT, pady=10)

increase_button = tk.Button(formatting, text="+", font=("Arial", 12), bg="#f0f0f0", fg="black", command=increase_font_size, borderwidth=0, highlightbackground="#f0f0f0")
increase_button.pack(side=tk.LEFT, pady=10)

# Textbox
text = tk.Text(main, font=("Arial", 12), bg="white", fg="black", insertbackground='black')
text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


window.mainloop()