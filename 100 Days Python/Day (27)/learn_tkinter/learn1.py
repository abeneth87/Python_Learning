from tkinter import *


def button_clicked():
    new_text = input.get()
    my_label["text"] = new_text


window = Tk()
window.title("Abe's GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# Label
my_label = Label(text="I am Label", font=("Arial", 24, "italic"))
# my_label.pack()
my_label.grid(column=0, row=0)

# button
button = Button(text="Click Me", command=button_clicked)
#button.pack()
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)


# Entry
input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)


window.mainloop()
