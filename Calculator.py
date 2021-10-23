import tkinter as tk

root = tk.Tk()
root.title("Calculator")


class Widget:
    def __init__(self, open, close):
        self.open = open
        self.close = close
        self.savedcalculation = []

    def open(self, calculato):
        pass


e = tk.Entry(root, text="888888888888", width=40, borderwidth=10)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=20)


def button_click(number):
    global current
    current = e.get()
    e.delete(0, "end")

    e.insert(0, str(current) + str(number))





def add():
    number = e.get()
    global first
    global math
    math = "addition"
    first = int(number)
    e.delete(0, "end")


def subtract():
    number = e.get()
    global first
    global math
    math = "subtraction"
    first = int(number)
    e.delete(0, "end")


def multiply():
    number = e.get()
    global first
    global math
    math = "multiply"
    first = int(number)
    e.delete(0, "end")


def division():
    number = e.get()
    global first
    global math
    math = "division"
    first = int(number)
    e.delete(0, "end")


def clear():
    e.delete(0, "end")


def equals():
    second_number = e.get()
    e.delete(0, "end")
    if math == "addition":
        e.insert(0, first + int(second_number))
    elif math == "subtraction":
        e.insert(0, first - int(second_number))
    elif math == "multiply":
        e.insert(0, first * int(second_number))
    elif math == "division":
        divided = first/int(second_number)
        e.insert(0, int(divided))



button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))

button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))

button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))

button_equal = tk.Button(root, text="=", padx=80, pady=20, command=equals)
button_add = tk.Button(root, text="+", padx=40, pady=20, command=add)
button_multiply = tk.Button(root, text="*", padx=40, pady=20, command=multiply)
button_divide = tk.Button(root, text="/", padx=40, pady=20, command=division)
button_subtract = tk.Button(root, text="-", padx=40, pady=20, command=subtract)
button_clear = tk.Button(root, text="Clear", padx=80, pady=20, command=clear)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_equal.grid(row=5, column=1, columnspan=2)
button_divide.grid(row=5, column=0)
button_multiply.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_subtract.grid(row=4, column=2)
button_clear.grid(row=6, column=0, columnspan=3)
root.mainloop()
