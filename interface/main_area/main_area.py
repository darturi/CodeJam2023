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
title = tk.Label(header, text="Note 3.3", font=("Arial", 20, "bold"), bg="#8a2be2", fg="white")
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

def toggle_text_bold():
    start_index = text.index("sel.first")
    end_index = text.index("sel.last")

    # Check if the selected text is already bold
    tags = text.tag_names(start_index)
    if "bold" in tags:
        text.tag_remove("bold", start_index, end_index)
    else:
        # Get the font configuration of the first character in the selection
        font_config = text.tag_cget(text.tag_names(start_index), "font")

        # Extract the font size from the font configuration or set a default size
        if font_config:
            font_size = int(font_config.split()[1])
        else:
            # Set a default font size if not retrieved
            font_size = 12  # You can adjust this default size as needed

        # Configure the selected text to be bold or revert to normal with preserved font size
        if "bold" in tags:
            # Revert to normal text while maintaining font size
            normal_font = ("TkDefaultFont", font_size)
            text.tag_configure("normal", font=normal_font)
            text.tag_add("normal", start_index, end_index)
            text.tag_remove("bold", start_index, end_index)
        else:
            # Configure the selected text to be bold while retaining the font size
            bold_font = ("TkDefaultFont", font_size, "bold")
            text.tag_configure("bold", font=bold_font)
            text.tag_add("bold", start_index, end_index)

# Date Label
date = tk.Label(header, text="", font=("Arial", 12), bg="#8a2be2", fg="white")
date.pack(side=tk.RIGHT, padx=10)
update_date_label()

# Side Frame
sidebar = tk.Frame(window, bg="#f0f0f0", width=200)
sidebar.pack(side=tk.LEFT, fill=tk.Y)

# New Note and New Folder Buttons
new_note = tk.Button(sidebar, text="New Note", font=("Arial", 12), bg="#8a2be2", fg="#8a2be2", width=15)
new_note.pack(side=tk.BOTTOM, padx=10, pady=10)
new_folder = tk.Button(sidebar, text="New Folder", font=("Arial", 12), bg="#8a2be2", fg="#8a2be2", width=15)
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
options = ["Font", "Size", "Color"]

bold_image = tk.PhotoImage(file='bold-b.pgm')
true_bold = bold_image.subsample(30, 30)
bold_button = tk.Button(formatting, image=true_bold, command=toggle_text_bold)
bold_button.pack(side=tk.LEFT, padx=5, pady=10)

underline_image = tk.PhotoImage(file='underlined_u.pgm')
true_underline = underline_image.subsample(55,55)
underline_button = tk.Button(formatting, image=true_underline)
underline_button.pack(side=tk.LEFT, padx=5, pady=10)

italic_image = tk.PhotoImage(file='italic-i.pgm')
true_italic = italic_image.subsample(30,30)
italic_button = tk.Button(formatting, image=true_italic)
italic_button.pack(side=tk.LEFT, padx=5, pady=10)

# Add code button
original_image_pil = Image.open('add_code.png')
resized_code = original_image_pil.resize((100,32))
code_image = ImageTk.PhotoImage(resized_code)
add_code_button = tk.Button(formatting, image=code_image)
add_code_button.pack(side=tk.RIGHT, padx=10, pady=10)


for option in options:
    button = tk.Button(formatting, text=option, font=("Arial", 12), bg="#f0f0f0", fg="black")
    button.pack(side=tk.LEFT, padx=20, pady=10)

# options = ["Bold", "Italic", "Underline", "Font", "Size", "Add Code"]
# for option in options:
#     button = tk.Button(formatting, text=option, font=("Times New Roman", 12), bg="#f0f0f0", fg="black")
#     button.pack(side=tk.LEFT, padx=20, pady=10)

# Add the "+" and "-" buttons for adjusting text size
decrease_button = tk.Button(formatting, text="-", font=("Arial", 12), bg="#f0f0f0", fg="black", command=decrease_font_size)
decrease_button.pack(side=tk.LEFT, pady=10)

increase_button = tk.Button(formatting, text="+", font=("Arial", 12), bg="#f0f0f0", fg="black", command=increase_font_size)
increase_button.pack(side=tk.LEFT, pady=10)

# Textbox
text = tk.Text(main, font=("Arial", 12), bg="white", fg="black")
text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

window.mainloop()