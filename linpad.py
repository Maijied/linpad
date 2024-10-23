#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from tkinter import font
import keyword
import webbrowser

class Linpad:
    def __init__(self, root):
        self.root = root
        self.root.title("Linpad")
        self.root.geometry("800x600")

        self.text_area = tk.Text(self.root, undo=True, wrap='word')
        self.text_area.pack(fill=tk.BOTH, expand=1)
        self.text_area.bind("<KeyRelease>", self.update_status_bar)

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_command(label="Print", command=self.print_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"))
        self.edit_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"))
        self.edit_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"))
        self.edit_menu.add_command(label="Delete", command=lambda: self.text_area.delete("sel.first", "sel.last"))
        self.edit_menu.add_command(label="Select All", command=lambda: self.text_area.tag_add("sel", "1.0", "end"))
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Find", command=self.find_text)
        self.edit_menu.add_command(label="Replace", command=self.replace_text)
        self.edit_menu.add_command(label="Word Count", command=self.word_count)

        self.format_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Format", menu=self.format_menu)
        self.format_menu.add_command(label="Font", command=self.choose_font)
        self.format_menu.add_command(label="Toggle Dark Mode", command=self.toggle_dark_mode)
        self.format_menu.add_command(label="Zoom In", command=self.zoom_in)
        self.format_menu.add_command(label="Zoom Out", command=self.zoom_out)

        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.show_about)
        self.help_menu.add_command(label="Documentation", command=self.show_documentation)

        self.status_bar = tk.Label(self.root, text="Line 1, Column 1", anchor='w')
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        self.bind_shortcuts()

    def update_status_bar(self, _=None):
        row, col = self.text_area.index(tk.INSERT).split('.')
        self.status_bar.config(text=f"Line {int(row)}, Column {int(col) + 1}")
        self.highlight_syntax()

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.update_status_bar()

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())
            self.update_status_bar()

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"),
                                                            ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"),
                                                            ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))

    def print_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".ps",
                                                 filetypes=[("PostScript files", "*.ps")])
        if file_path:
            self.text_area.postscript(file=file_path)
            messagebox.showinfo("Print", "File saved for printing.")

    def choose_font(self):
        font_name = simpledialog.askstring("Font", "Enter font family (e.g., Arial):")
        font_size = simpledialog.askinteger("Font Size", "Enter font size:")
        if font_name and font_size:
            new_font = font.Font(family=font_name, size=font_size)
            self.text_area.config(font=new_font)

    def find_text(self):
        find_string = simpledialog.askstring("Find", "Enter text to find:")
        self.text_area.tag_remove('found', '1.0', tk.END)
        if find_string:
            idx = '1.0'
            while True:
                idx = self.text_area.search(find_string, idx, nocase=1, stopindex=tk.END)
                if not idx:
                    break
                lastidx = f'{idx}+{len(find_string)}c'
                self.text_area.tag_add('found', idx, lastidx)
                idx = lastidx
            self.text_area.tag_config('found', foreground='white', background='blue')

    def replace_text(self):
        find_string = simpledialog.askstring("Find", "Enter text to find:")
        replace_string = simpledialog.askstring("Replace", "Enter text to replace with:")
        if find_string and replace_string:
            content = self.text_area.get("1.0", tk.END)
            new_content = content.replace(find_string, replace_string)
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, new_content)

    def word_count(self):
        content = self.text_area.get("1.0", tk.END)
        word_count = len(content.split())
        char_count = len(content)

    def highlight_syntax(self, event=None):
        content = self.text_area.get('1.0', tk.END).split()
        for word in content:
            if word in keyword.kwlist:
                idx = self.text_area.search(word, '1.0', stopindex=tk.END)
                while idx:
                    end_idx = f"{idx}+{len(word)}c"
                    self.text_area.tag_add('keyword', idx, end_idx)
                    idx = self.text_area.search(word, end_idx, stopindex=tk.END)
        self.text_area.tag_config('keyword', foreground='blue')

    def toggle_dark_mode(self):
        current_bg = self.text_area.cget("background")
        if current_bg == "black":
            self.text_area.config(background="white", foreground="black")
            self.status_bar.config(background="white", foreground="black")
        else:
            self.text_area.config(background="black", foreground="white")
            self.status_bar.config(background="black", foreground="white")

    def zoom_in(self):
        current_font = font.nametofont(self.text_area.cget("font"))
        new_size = current_font.actual()["size"] + 2
        new_font = font.Font(family=current_font.actual()["family"], size=new_size)
        self.text_area.config(font=new_font)

    def zoom_out(self):
        current_font = font.nametofont(self.text_area.cget("font"))
        new_size = current_font.actual()["size"] - 2
        new_font = font.Font(family=current_font.actual()["family"], size=new_size)
        self.text_area.config(font=new_font)

    def show_about(self):
        messagebox.showinfo(
            "About", 
            "Linpad Version 1.0\n\n"
            "Linpad is a simple text editor with syntax highlighting and word count functionality. "
            "I am going to make this open-source via GitHub, so everyone can collaborate to enhance and expand its features. "
            "Let me know if you have some good ideas to make it better. You will find me here: mdshuvo40@gmail.com"
        )

    def show_documentation(self):
        try:
            webbrowser.open_new_tab("https://github.com/Maijied/linpad/blob/main/DOCUMENTATION.md")
        except webbrowser.Error:
            messagebox.showinfo("Documentation", "Please connect to the internet to view the documentation.")

    def bind_shortcuts(self):
        self.root.bind("<Control-n>", lambda event: self.new_file())
        self.root.bind("<Control-n>", lambda _: self.new_file())
        self.root.bind("<Control-o>", lambda _: self.open_file())
        self.root.bind("<Control-s>", lambda _: self.save_file())
        self.root.bind("<Control-Shift-S>", lambda _: self.save_as_file())
        self.root.bind("<Control-p>", lambda _: self.print_file())
        self.root.bind("<Control-q>", lambda _: self.root.quit())

        self.root.bind("<Control-z>", lambda _: self.text_area.edit_undo())
        self.root.bind("<Control-y>", lambda _: self.text_area.edit_redo())
        self.root.bind("<Control-x>", lambda _: self.text_area.event_generate("<<Cut>>"))
        self.root.bind("<Control-c>", lambda _: self.text_area.event_generate("<<Copy>>"))
        self.root.bind("<Control-v>", lambda _: self.text_area.event_generate("<<Paste>>"))
        self.root.bind("<Delete>", lambda _: self.text_area.delete("sel.first", "sel.last"))
        self.root.bind("<Control-a>", lambda _: self.text_area.tag_add("sel", "1.0", "end"))

        self.root.bind("<Control-f>", lambda _: self.find_text())
        self.root.bind("<Control-h>", lambda _: self.replace_text())
        self.root.bind("<Control-w>", lambda _: self.word_count())

        self.root.bind("<Control-equal>", lambda _: self.zoom_in())
        self.root.bind("<Control-d>", lambda _: self.toggle_dark_mode())
if __name__ == "__main__":
    root = tk.Tk()
    app = Linpad(root)
    root.mainloop()
