from NoteFrame import NoteFrame
import tkinter as tk


class MainWindow(tk.Frame):
    window_title = "OurNotes"
    window_geometry = "800x600"
    accent_color = "#8a2be2"
    main_foreground = "white"
    light_grey = "#f0f0f0"

    def __init__(self, parent, *args, **kwargs):
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
        for note in self.note_stockpile:
            note_btn = tk.Button(self.notes_container, text=note.get_title(), font=("Arial", 12),
                                 bg=MainWindow.accent_color, fg=MainWindow.accent_color, width=15)
            note_btn.pack(fill="x", expand=True)

        # New Note and New Folder Buttons
        self.new_note = tk.Button(self.sidebar, text="New Note", font=("Arial", 12),
                                  bg=MainWindow.accent_color, fg=MainWindow.accent_color, width=15,
                                  command=self.new_note_cmd)
        self.new_note.pack(side=tk.BOTTOM, padx=10, pady=10)
        self.new_folder = tk.Button(self.sidebar, text="New Folder", font=("Arial", 12),
                                    bg=MainWindow.accent_color, fg=MainWindow.accent_color, width=15)
        self.new_folder.pack(side=tk.BOTTOM, padx=10, pady=10)

        # Define Note-Taking Frame
        self.note_frame = tk.Frame(self.parent, bg=MainWindow.main_foreground)
        self.note_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        #self.note_frame.grid_rowconfigure(0, weight=1)
        #self.note_frame.grid_columnconfigure(0, weight=1)

        #self.note_frame_dict = {}

        """ # Set up start frame
        start_frame = tk.Frame(self.note_frame, bg=MainWindow.main_foreground)
        start_frame_frame = start_frame(parent=self.note_frame, controller=self)
        self.note_frame_dict["start frame"] = start_frame_frame
        start_frame_frame.grid(row=0, column=0, sticky="nsew")"""

        #for note in self.note_stockpile:
        #    frame = note(parent=self.note_frame, controller=self)
        #    self.note_frame_dict[note.get_title()] = frame
        #    frame.grid(row=0, column=0, sticky="nsew")

        # Define Empty Note-Taking Area Placeholder
        # self.note = tk.Frame(self.note_frame, bg=MainWindow.main_foreground)
        # self.note.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def new_note_cmd(self):
        # return None
        # self.note_frame.forget()
        if len(self.note_stockpile) > 0:
            self.note_stockpile[-1].forget_self()
        self.forget_frame_contents(self.note_frame)
        self.update()
        #    self.note.forget()
        #self.note.destroy()

        new_note = NoteFrame(self.note_frame, self)
        self.note_stockpile.append(new_note)
        print(len(self.note_stockpile))
        self.update_side_bar()
        #self.note.pack_forget()
        #for note in self.note_stockpile[:-1]:
        #    note.pack_forget()

        self.note = new_note
        self.note.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def update_side_bar(self):
        self.clear_frame(self.notes_container)

        for note in self.note_stockpile:
            note_btn = tk.Button(self.notes_container, text=note.get_title(), font=("Arial", 12),
                                 bg=MainWindow.accent_color, fg=MainWindow.accent_color, width=15)
            note_btn.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    @staticmethod
    def clear_frame(frame_victim):
        for widgets in frame_victim.winfo_children():
            widgets.destroy()

    @staticmethod
    def forget_frame_contents(victim_frame):
        for widgets in victim_frame.winfo_children():
            widgets.pack_forget()

    def load_note(self, note_name):
        return None



def demo():
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    demo()
