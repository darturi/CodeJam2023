import tkinter as tk


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

        # Boilerplate
        self.toolbar = tk.Frame(self, bg="#eee")
        self.toolbar.pack(side="top", fill="x")

        # Define format button
        self.bold_btn = tk.Button(self.toolbar, text="Format", command=self.format)
        self.bold_btn.pack(side="left")

        # Define textbox for user input
        self.input = tk.Text(self)

        # Configure default color of text window
        self.input.config(fg="white", bg="#2B2B2B", insertbackground="white")

        self.input.insert("end", "IN -- Select part of text and then click 'Bold'...")
        self.input.focus()
        self.input.pack(fill="both", expand=True)

        # Define colored fonts
        self.input.tag_configure(Pad.orange_label_name, foreground="orange")
        self.input.tag_configure(Pad.yellow_label_name, foreground="yellow")
        self.input.tag_configure(Pad.green_label_name, foreground="green")
        self.input.tag_configure(Pad.purple_label_name, foreground="purple")
        self.input.tag_configure(Pad.pink_label_name, foreground="hot pink")
        self.input.tag_configure(Pad.grey_label_name, foreground="#848484")

    """
    def format(self):
        # DRAFT OF ALGORITHM
        keywords = [
            "False", "await ", "import ", "pass", "None", "break", "def ",
            " in ", "raise", "True", "class", "finally", "is", "return", " and ",
            "continue", "for ", "lambda", " as ", "from ", "nonlocal",
            "while ", "assert", "del ", "global ", "not ", "with", "async", "elif ", "if ",
            " or ", "yield"
        ]

        keywords_w_colon = [
            "except",
            "raise", "True", "class", "finally", "is", "return",
            "continue", "for ", "lambda", "try", "nonlocal",
            "assert", "with", "async", "elif ", "if ",
            "yield"
        ]

        for word in keywords:
            offset = '+%dc' % len(word)
            pos_start = self.input.search(word, '1.0', "end")
            while pos_start:
                print(word)
                # create end position by adding (as string "+5c") number of chars in searched word
                pos_end = pos_start + offset
                print("\t" + str(pos_start))
                print("\t" + str(pos_end))

                # add tag
                self.input.tag_add('orange_coloring', pos_start, pos_end)

                # search again from pos_end to the end of text (END)
                pos_start = self.input.search(word, pos_end, "end")
    """

    def format(self):
        # DRAFT OF ALGORITHM

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
                # end = "%s + %d chars" % (index, char_count.get())
                end = "%s + %d chars" % (pos_start, char_count.get())
                print(enclosure_key)
                print(start, type(start))
                print(end)
                self.input.tag_add(color, start, end)

                pos_start = self.input.search(word_key, end, "end", count=char_count, regexp=True)


def demo():
    root = tk.Tk()
    Pad(root).pack(expand=1, fill="both")
    root.mainloop()


if __name__ == "__main__":
    demo()
