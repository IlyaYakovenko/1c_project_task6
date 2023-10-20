from datetime import datetime
from logic import *
from tkinter import *
from tkinter import messagebox


def update_map():
    for i in members:
        canvas.create_oval(int(i.positions_[-1].x_) - 20, int(i.positions_[-1].y_) - 20, int(i.positions_[-1].x_) + 20, int(i.positions_[-1].y_) + 20, fill="black")


class Position:
    def __init__(self, x, y):
        self.x_ = x
        self.y_ = y
        self.date_ = datetime.now().date()
        self.time_ = datetime.now().time()


class Member:
    def __init__(self, name, x, y):
        self.name_ = name
        self.start_pos_ = Position(x, y)
        self.positions_ = []
        self.positions_.append(self.start_pos_)


def add_member(name, start_x, start_y, window_arg):
    print(name, start_x, start_y)
    member = Member(name, start_x, start_y)
    members.append(member)
    update_map()
    window_arg.destroy()


def insert_memb_name():
    add_window = Tk()
    add_window.geometry('500x100')
    add_window.title('Добавление героя')
    lbl1 = Label(add_window, text='Введите имя героя:')
    lbl1.grid(column=0, row=0)

    ent1 = Entry(add_window)
    ent1.grid(column=0, row=1)
    ent1.focus()

    lbl2 = Label(add_window, text='Введите положение по х:')
    lbl2.grid(column=1, row=0)

    ent2 = Entry(add_window)
    ent2.grid(column=1, row=1)

    lbl3 = Label(add_window, text='Введите положение по у:')
    lbl3.grid(column=2, row=0)

    ent3 = Entry(add_window)
    ent3.grid(column=2, row=1)

    btn_start = Button(add_window, text='Добавить',
                       command=lambda x="lambda": add_member(ent1.get(), ent2.get(), ent3.get(), add_window))
    btn_start.grid(column=1, row=4)


window = Tk()

window.title("Members tracker")
window.geometry("1000x750")

members = []


app_map, width, height = map_create()

canvas = Canvas(window, width=width, height=height)

canvas.pack(side="top", fill="both", expand="no")

canvas.create_image(0, 0, anchor="nw", image=app_map)

b_add = Button(window, text="Добавить участника", width=15, command=insert_memb_name, bg='LightSalmon3')
canvas.create_window((850, 80), window=b_add)






def on_closing():
    if messagebox.askokcancel("", "Закрыть программу?"):
        window.destroy()


window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()
