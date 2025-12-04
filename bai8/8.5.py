
import tkinter as tk

root = tk.Tk()
v = tk.IntVar()
v.set(1) # initializing the choice, i.e., Python

languages = [
("Python", 1),
("Perl", 2),
("Java", 3),
("C++", 4),
("C", 5)
]
def ShowChoice():
    print(v.get())

tk.Label(
root,
text="Choose your favorite programming language:",
justify=tk.LEFT,
padx=20
).pack()

for val, language in enumerate(languages):
    tk.Radiobutton(
    root,
    text=language[0],
    indicatoron=0, # Thay thế radio button thành indicator như hình
    width=20,
    padx=20,
    variable=v,
    command=ShowChoice,
    value=language[1]
    ).pack(anchor=tk.W)
    root.mainloop()
