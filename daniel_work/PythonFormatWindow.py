import os
import pickle

from NoteFrame import NoteFrame
import tkinter as tk


class MainWindow(tk.Frame):
    window_title = "OurNotes"
    window_geometry = "1283x720"
    accent_color = "#8a2be2"
    main_foreground = "white"
    light_grey = "#f0f0f0"

    def __init__(self, parent, *args, **kwargs):
        raise Exception()
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.note_stockpile = []

        self.parent.title(MainWindow.window_title)
        self.parent.geometry(MainWindow.window_geometry)

        # Top bar
        self.header = tk.Frame(self.parent, bg=MainWindow.accent_color, height=50)
        self.header.pack(fill=tk.X)

        # Title and Date
        self.title = tk.Label(self.header, text="OurNotes", font=("Arial", 20, "bold"),
                         bg=MainWindow.accent_color, fg=MainWindow.main_foreground)
        self.title.pack(side=tk.LEFT, padx=10)
        self.date = tk.Label(self.header, text="", font=("Arial", 12),
                        bg=MainWindow.accent_color, fg=MainWindow.main_foreground)
        self.date.pack(side=tk.RIGHT, padx=10)

        # Side Frame
        self.sidebar = tk.Frame(self.parent, bg=MainWindow.light_grey, width=200)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)

        # Create Note Links in sidebar
        self.notes_container = tk.LabelFrame(self.sidebar, text="Notes", font=("Arial", 12, "bold"),
                                             bg=MainWindow.light_grey, fg=MainWindow.accent_color)
        self.notes_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # New Note and New Folder Buttons
        self.new_note = tk.Button(self.sidebar, text="New Note", font=("Arial", 12),
                                  bg=MainWindow.accent_color, fg=MainWindow.accent_color, width=15,
                                  command=self.new_note_cmd)
        self.new_note.pack(side=tk.BOTTOM, padx=10, pady=10)
        self.new_folder = tk.Button(self.sidebar, text="Import File", font=("Arial", 12),
                                    bg=MainWindow.accent_color, fg=MainWindow.accent_color, width=15,
                                    command=self.import_note_popup)
        self.new_folder.pack(side=tk.BOTTOM, padx=10, pady=10)

        # Define Note-Taking Frame
        self.note_frame = tk.Frame(self.parent, bg=MainWindow.main_foreground)
        self.note_frame.pack(fill=tk.BOTH, expand=True)

        self.frames_dict = {}
        self.note_frame_sub = tk.Frame(self.note_frame, bg=MainWindow.main_foreground)
        self.note_frame_sub.rowconfigure(0, weight=10)
        self.note_frame_sub.columnconfigure(0, weight=1)

        self.note_frame_sub.grid(columnspan=3)

    def import_note_popup(self):
        top = tk.Toplevel()
        top.geometry("400x300")
        top.title("Import Selection Window")

        viable_files = []
        for fname in os.listdir('.'):
            if fname.endswith(".pkl") or fname.endswith(".txt"):
                viable_files.append(fname)

        if not viable_files:
            tk.Label(top, text="Sorry, we didn't find any compatible files",
                     font=("Arial", 20)).pack()
            tk.Button(top, text="close", font=("Arial", 16),
                      bg=MainWindow.accent_color, fg=MainWindow.accent_color,
                      width=15, command=top.destroy).pack()

        else:
            tk.Label(top, text="Choose From the Below Files").pack(side="top")

            options_frame = tk.Frame(top)
            options_frame.pack(side="bottom", fill=tk.Y, expand=True)

            for f in viable_files:
                note_btn = tk.Button(options_frame, text=f, font=("Arial", 12),
                                     bg=MainWindow.accent_color, fg=MainWindow.accent_color, width=15,
                                     command=lambda x=f: self.import_general_file(x)
                                     )
                note_btn.pack(fill=tk.X, side="top", expand=False, padx=10)

    def import_general_file(self, f_name):
        if f_name[-4:] == ".txt":
            self.import_txt_file(f_name)
        else:
            self.import_pkl_file(f_name)

    def import_txt_file(self, f_name):
        f = open(f_name, "r")
        contents = f.read()
        f.close()
        self.new_note_cmd()
        new_note = self.note_stockpile[-1]
        first_pad = new_note.pad_list[0]
        first_pad.input.insert("end", contents)
        first_pad.update_size()

        new_note.name = f_name[:-4]

        new_note.title_field.insert("end", f_name[:-4])
        self.update_side_bar()

    def import_pkl_file(self, f_name):
        f = open(f_name, "rb")
        saved_obj = pickle.load(f)

        self.new_note_cmd()
        new_note = self.note_stockpile[-1]
        new_note_pad_list = new_note.pad_list

        for i in range(len(saved_obj)):
            if i == 0:
                new_note_pad_list[0].input.insert("end", saved_obj[0][:-1])
                new_note_pad_list[0].update_size()
            else:
                if i % 2 == 1:
                    new_note.add_code_block()
                    new_note_pad_list[i].input.insert("end", saved_obj[i][:-1])
                    new_note_pad_list[i].format()
                    new_note_pad_list[i].update_size()
                else:
                    new_note_pad_list[i].input.insert("end", saved_obj[i][:-1])
                    new_note_pad_list[i].update_size()

        new_note.name = f_name[:-4]

        new_note.title_field.insert("end", f_name[:-4])
        self.update_side_bar()

    def switch(self, frame_id):
        self.update_side_bar()
        self.frames_dict[frame_id].tkraise()

    def new_note_cmd(self):
        raise Exception()
        self.forget_frame_contents(self.note_frame_sub)

        self.intermediate_frame = tk.Frame(self.note_frame_sub, bg=MainWindow.main_foreground)
        self.intermediate_frame.grid(row=0, column=0, sticky="nsew", columnspan=3)

        new_note = NoteFrame(self.intermediate_frame)
        self.note_stockpile.append(new_note)
        self.update_side_bar()

        self.intermediate_frame.grid(row=0, column=0, sticky="nsew", columnspan=3)
        self.frames_dict[new_note.get_id()] = self.intermediate_frame

        self.switch(new_note.get_id())

    def open_note(self, note_id):
        self.forget_frame_contents(self.note_frame_sub)

        for note in self.note_stockpile:
            if note.get_id() == note_id:
                self.switch(note.get_id())
                break

    def load_note_into_note_frame(self, new_note):
        self.note = new_note
        self.note.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def update_side_bar(self):
        self.clear_frame(self.notes_container)

        for i in range(len(self.note_stockpile)):
            note = self.note_stockpile[i]

            note_btn = tk.Button(self.notes_container, text=note.get_title(), font=("Arial", 12),
                                 bg=MainWindow.accent_color, fg=MainWindow.accent_color, width=15,
                                 command=lambda x=i: self.open_note(x))
            note_btn.pack(fill=tk.X, side="top", expand=False, padx=10)

    @staticmethod
    def clear_frame(frame_victim):
        for widgets in frame_victim.winfo_children():
            widgets.destroy()

    @staticmethod
    def forget_frame_contents(victim_frame):
        for widgets in victim_frame.winfo_children():
            widgets.pack_forget()


def demo():
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    demo()
