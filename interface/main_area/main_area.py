import tkinter as tk

# Main Window
window = tk.Tk()
window.title("Note 3.3")
window.geometry("800x600")

# Top bar
header = tk.Frame(window, bg="#8a2be2", height=50)
header.pack(fill=tk.X)

# Title and Date
title = tk.Label(header, text="Note 3.3", font=("Arial", 20, "bold"), bg="#8a2be2", fg="white")
title.pack(side=tk.LEFT, padx=10)
date = tk.Label(header, text="November 17th, 2021", font=("Arial", 12), bg="#8a2be2", fg="white")
date.pack(side=tk.RIGHT, padx=10)

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

# Formatting options
formatting = tk.Frame(main, bg="#f0f0f0", height=50)
formatting.pack(fill=tk.X)
options = ["Bold", "Italic", "Underline", "Font", "Size", "Color"]
for option in options:
    button = tk.Button(formatting, text=option, font=("Arial", 12), bg="#f0f0f0", fg="black")
    button.pack(side=tk.LEFT, padx=10, pady=10)

# Textbox
text = tk.Text(main, font=("Arial", 12), bg="white", fg="black")
text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Remove and Edit buttons
edit = tk.Button(main, text="Edit", font=("Arial", 12), bg="#8a2be2", fg="#8a2be2", width=15)
edit.pack(side=tk.RIGHT, padx=10, pady=10)
remove = tk.Button(main, text="Remove", font=("Arial", 12), bg="#8a2be2", fg="#8a2be2", width=15)
remove.pack(side=tk.RIGHT, padx=10, pady=10)

window.mainloop()