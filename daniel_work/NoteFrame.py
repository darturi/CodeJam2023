import random
import tkinter as tk
from datetime import date
from tkinter import font
import pickle


class Pad(tk.Frame):
    orange_label_name = "orange_coloring"
    green_label_name = "green_coloring"
    yellow_label_name = "yellow_coloring"
    pink_label_name = "pink_coloring"
    purple_label_name = "purple_coloring"
    grey_label_name = "grey_coloring"
    py_dict = {
        # Keywords
        "False": ["False", orange_label_name],
        "await": ["await ", orange_label_name],
        "else": ["else:", orange_label_name],
        "import": ["import ", orange_label_name],
        "pass": ["pass", orange_label_name],
        "None": ["None", orange_label_name],
        "break": ["break", orange_label_name],
        "except": ["except:", orange_label_name],
        " in ": [" in ", orange_label_name],
        "raise": ["raise ", orange_label_name],
        "True": ["True", orange_label_name],
        "class": ["class ", orange_label_name],
        "finally": ["finally:", orange_label_name],
        " is ": [" is ", orange_label_name],
        "return": ["return", orange_label_name],
        "and ": [" and ", orange_label_name],
        "continue": ["continue", orange_label_name],
        "for": ["for ", orange_label_name],
        "lambda": ["lambda ", orange_label_name],
        "try": ["try:", orange_label_name],
        "as ": [" as ", orange_label_name],
        "def": ["def ", orange_label_name],
        "from": [" from ", orange_label_name],
        "nonlocal": ["nonlocal ", orange_label_name],
        "while": ["while ", orange_label_name],
        "assert": ["assert ", orange_label_name],
        "del": ["del ", orange_label_name],
        "global": ["global ", orange_label_name],
        "not": ["not ", orange_label_name],
        "with": ["with ", orange_label_name],
        "async": ["async ", orange_label_name],
        "elif": ["elif ", orange_label_name],
        "if": ["if ", orange_label_name],
        "or": [" or ", orange_label_name],
        "yield": ["yield ", orange_label_name],

        # Grammer
        ",": [",", orange_label_name],
        # "\\": ["\ ", orange_label_name],

        # Brackets / Parenthesis
        "(": ["(", yellow_label_name],
        ")": [")", yellow_label_name],
        "[": ["[", yellow_label_name],
        "]": ["]", yellow_label_name],
        "{": ["{", yellow_label_name],
        "}": ["}", yellow_label_name],

        # self
        "self": ["self.", purple_label_name],

        # MAYBE ADD NUMBERS????
    }
    symbol_enclosure = {
        '__': [r'(?:__).*(?:__)', pink_label_name],
        '\'\'\'': [r'(?:\'\'\').*(?:\'\'\')', green_label_name],
        '\"': [r'(?:").*(?:")', green_label_name],
        "\'": [r"(?:').*(?:')", green_label_name],
        '#': [r'(?:#).*(?:\n)', grey_label_name],
        '\"\"\"': [r'(?:""").*(?:""")', green_label_name],
    }

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # Define Font Constants
        self.font_size = 14
        self.font_family = "Andale Mono"

        # Define empty toolbar
        self.toolbar = tk.Frame(self, bg="#eee")
        self.toolbar.pack(side="bottom", fill="x")

        # Define format button
        self.format_btn = tk.Button(self.toolbar, text="Format", command=self.format)
        self.format_btn.pack(side="right")

        # Define textbox for user input
        self.input = tk.Text(self, height=2)

        # Configure default color of text window
        self.input.config(fg="white", bg="#2B2B2B", insertbackground="white")

        # self.input.insert("end", "IN -- Select part of text and then click 'Bold'...")
        self.input.focus()
        self.input.pack(fill="both", expand=True)
        # self.input.bind("<Command-v>", self.update_size) BUG
        self.input.bind("<Key>", self.update_size)

        # Define colored fonts
        self.input.tag_configure(Pad.orange_label_name, foreground="orange")
        self.input.tag_configure(Pad.yellow_label_name, foreground="yellow")
        self.input.tag_configure(Pad.green_label_name, foreground="green")
        self.input.tag_configure(Pad.purple_label_name, foreground="#936080")
        self.input.tag_configure(Pad.pink_label_name, foreground="hot pink")
        self.input.tag_configure(Pad.grey_label_name, foreground="#848484")

    def format(self):
        # Words with set/defined length
        for word_key in Pad.py_dict:
            search_term, color = Pad.py_dict[word_key]
            offset = '+%dc' % (len(word_key))
            pos_start = self.input.search(search_term, '1.0', "end")
            while pos_start:
                print(word_key)
                print("---" + search_term + "---")
                print(color)
                # create end position by adding (as string "+5c") number of chars in searched word
                pos_end = pos_start + offset
                print("\t" + str(pos_start))
                print("\t" + str(pos_end))

                # add tag
                self.input.tag_add(color, pos_start, pos_end)

                # search again from pos_end to the end of text (END)
                pos_start = self.input.search(word_key, pos_end, "end")

        # Colored sections with no set length (enclosed in color)
        for enclosure_key in Pad.symbol_enclosure:
            char_count = tk.IntVar()
            word_key, color = Pad.symbol_enclosure[enclosure_key]
            pos_start = self.input.search(word_key, "1.0", "end", count=char_count, regexp=True)
            while pos_start:
                start = "%s + 0 chars" % pos_start
                end = "%s + %d chars" % (pos_start, char_count.get())
                print(enclosure_key)
                print(start, type(start))
                print(end)
                self.input.tag_add(color, start, end)

                pos_start = self.input.search(word_key, end, "end", count=char_count, regexp=True)

    def update_size(self, event):
        widget_height = self.get_optimal_height()
        self.input.config(height=widget_height)

    def get_optimal_height(self):
        # Calculate the optimal height based on the content
        widget_height = int(self.input.index(tk.END).split('.')[0])
        widget_width = int(self.input.cget("width"))

        line_count = 1
        current_line_length = 0

        for char in self.input.get("1.0", tk.END):
            if char == '\n' or current_line_length >= widget_width:
                line_count += 1
                current_line_length = 0
            else:
                current_line_length += 1

        return max(2, line_count)


class PlainPad(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # Define Font Constants
        self.font_size = 14
        self.font_family = "Helvetica"

        # Define textbox for user input
        self.input = tk.Text(self, height=2)

        self.input.focus()
        self.input.pack(fill="x", expand=False)
        self.input.bind("<Key>", self.update_size)

        # Defining Font Alterations
        self.italics_font = font.Font(self.input, self.input.cget("font"))
        self.italics_font.configure(slant="italic")
        self.bold_font = font.Font(self.input, self.input.cget("font"))
        self.bold_font.configure(weight='bold')
        self.bold_italic_font = font.Font(self.input, self.input.cget("font"))
        self.bold_italic_font.configure(weight='bold', slant="italic")

        # Configure tags
        self.input.tag_configure("italic", font=self.italics_font)
        self.input.tag_configure("bold", font=self.bold_font)
        self.input.tag_configure("bold_italic", font=self.bold_italic_font)

    def update_size(self, event):
        widget_height = self.get_optimal_height()
        self.input.config(height=widget_height)

    def get_optimal_height(self):
        # Calculate the optimal height based on the content
        widget_height = int(self.input.index(tk.END).split('.')[0])
        widget_width = int(self.input.cget("width"))

        line_count = 1
        current_line_length = 0

        for char in self.input.get("1.0", tk.END):
            if char == '\n' or current_line_length >= widget_width:
                line_count += 1
                current_line_length = 0
            else:
                current_line_length += 1

        return max(2, line_count)


    def italics_it(self):
        try:
            # Define Current tags
            current_tags = self.input.tag_names("sel.first")
            if "bold" in current_tags and "italics" not in current_tags:
                self.input.tag_remove("bold", "sel.first", "sel.last")
                self.input.tag_add("bold_italic", "sel.first", "sel.last")

            elif "bold_italic" in current_tags:
                self.input.tag_remove("bold_italic", "sel.first", "sel.last")
                self.input.tag_add("bold", "sel.first", "sel.last")

            # If statment to see if tag has been set
            elif "italic" in current_tags:
                self.input.tag_remove("italic", "sel.first", "sel.last")
            else:
                self.input.tag_add("italic", "sel.first", "sel.last")
        except:
            pass

    def bold_it(self):
        try:
            # Define Current tags
            current_tags = self.input.tag_names("sel.first")
            # print("Bold")
            # print('\t', current_tags)
            if "italic" in current_tags and "bold" not in current_tags:
                self.input.tag_remove("italic", "sel.first", "sel.last")
                self.input.tag_add("bold_italic", "sel.first", "sel.last")

            elif "bold_italic" in current_tags:
                self.input.tag_remove("bold_italic", "sel.first", "sel.last")
                # self.input.tag_add("bold", "sel.first", "sel.last")
                self.input.tag_add("italic", "sel.first", "sel.last")

            # If statment to see if tag has been set
            elif "bold" in current_tags:
                self.input.tag_remove("bold", "sel.first", "sel.last")
            else:
                self.input.tag_add("bold", "sel.first", "sel.last")
        except:
            pass


class NoteFrame(tk.Frame):
    note_counter = 0

    def __init__(self, parent, controller=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.controller = controller

        self.name = str(random.random())
        self.id = NoteFrame.note_counter + 0
        NoteFrame.note_counter += 1
        print(NoteFrame.note_counter)
        self.date_created = date.today().strftime("%B %d, %Y")

        self.note_contents = []

        # Define Font Constants
        self.font_size = 14
        self.font_family = "Helvetica"

        self.parent = parent
        self.associated_folder = None

        # Create Header Frame
        self.header_frame = tk.Frame(self.parent)
        self.header_frame.pack(side="top", fill="x")

        # Define Title Area
        self.title_frame = tk.Frame(self.header_frame)
        self.title_frame.pack(side="top", fill="x")

        # Grid Within The title area

        # Title area 0,0 --> Title entry field
        self.title_field = tk.Entry(self.title_frame, font="Helvetica 24", width=35)
        self.title_field.grid(row=0, column=0)

        # Title area 0,1 --> Set title button
        self.add_title_btn = tk.Button(self.title_frame, text="Save", command=self.save_note)
        self.add_title_btn.grid(row=0, column=1)

        # Title area 1,0 --> Date note was created
        self.date_label = tk.Label(self.title_frame, text=self.date_created, fg="grey")
        self.date_label.grid(row=1, column=0, sticky="w")

        # Title area 1,1 --> export button
        self.export_btn = tk.Button(self.title_frame, text="Export", command=self.export_as_txt)
        self.export_btn.grid(row=1, column=1, sticky="e")

        # Define empty toolbar
        self.toolbar = tk.Frame(self.header_frame, bg="#eee")
        self.toolbar.pack(side="bottom", fill="x")

        # Toolbar Area 0,0 --> Text editing
        self.toolbar_text_edit = tk.Frame(self.toolbar, bg="#eee")
        self.toolbar_text_edit.grid(row=0, column=0)

        # Define note frame
        self.note_frame = tk.Frame(self.parent)
        self.note_frame.focus()
        self.note_frame.pack(side="bottom", fill="both", expand=True)

        # Toolbar area 0,0 --> bold button
        self.bold_btn = tk.Button(self.toolbar_text_edit, text="Bold", command=self.bold_text_cmd)
        self.bold_btn.grid(row=0, column=0)

        # Toolbar area 0,1 --> italics button
        self.italics_btn = tk.Button(self.toolbar_text_edit, text="Italics", command=self.italicize_text_cmd)
        self.italics_btn.grid(row=0, column=1)

        # Toolbar area 0,2 --> underline button
        self.underline_btn = tk.Button(self.toolbar_text_edit, text="Underline") #, command=self.underline_text_cmd)
        self.underline_btn.grid(row=0, column=2)

        # Toolbar area 0,3 --> add code block button
        self.add_code_block_btn = tk.Button(self.toolbar, text="Add Code Block", command=self.add_code_block)
        self.add_code_block_btn.grid(row=0, column=1, sticky="e", padx=(240, 0))

        # Define pad list
        self.pad_list = [PlainPad(self.note_frame)]

        for pad in self.pad_list:
            pad.pack(fill="x", expand=False)

    def __name__(self):
        return self.get_title()

    # Save contents of note
    def save_note(self):
        self.set_title_cmd()
        for pad in self.pad_list:
            self.note_contents.append(pad.input.get("1.0", "end"))
        f = open(self.name + ".pkl", "wb")
        pickle.dump(self.note_contents, f)
        f.close()

    def forget_self(self):
        self.controller.pack_forget()

    # Some Get Methods
    def get_title(self):
        self.set_title_cmd()
        return self.name

    def get_id(self):
        return self.id

    def get_date(self):
        return self.date_created

    def add_code_block(self):
        self.pad_list.append(Pad(self.note_frame))
        self.pad_list.append(PlainPad(self.note_frame))

        for pad in self.pad_list:
            pad.pack(fill="x", expand=False)

    def set_title_cmd(self):
        proposed_name = self.title_field.get()
        if proposed_name == "" or proposed_name in []:  # replace this with a list of all other notes
            return
        self.name = proposed_name

    def export_as_txt(self):
        self.set_title_cmd()
        text_list = []
        for pad in self.pad_list:
            text_list.append(pad.input.get("1.0", "end"))
        f = open(self.name + ".txt", "w")
        print(text_list)
        f.write("".join(text_list))
        f.close()

    def bold_text_cmd(self):
        for pad in self.pad_list:
            if type(pad) == PlainPad:
                pad.bold_it()

    def italicize_text_cmd(self):
        for pad in self.pad_list:
            if type(pad) == PlainPad:
                pad.italics_it()


def demo():
    root = tk.Tk()
    NoteFrame(root, root).pack(expand=1, fill="both")
    root.mainloop()


if __name__ == "__main__":
    demo()