from tkinter import *
from tkinter import font


def click(char):
    # if not (char == "0" and calc_field.get() == "0"):
    if calc_field.get() == "Error!":
        calc_field.delete(0, END)
        calc_field.insert(0, char)
    else:
        calc_field.insert(len(calc_field.get()), char)


def process_statement():
    statement = calc_field.get()
    if statement != "":
        try:
            result = str(eval(statement))
            calc_field.delete(0, END)
            calc_field.insert(0, result)
        except:
            calc_field.delete(0, END)
            calc_field.insert(0, "Error!")


def clear_statement():
    calc_field.delete(0, END)


window = Tk(className="Calculatrice 9000")
font.nametofont("TkDefaultFont").configure(size=14)
window.iconbitmap("calc_IDI_CALC_ICON.ico")
window.geometry("400x542")
window.resizable(width=False, height=False)

main_frame = Frame(window, padx=4, pady=4)
button_frame = Frame(window, padx=4, pady=4)

calc_field = Entry(main_frame, width=384, background="#e1ecf4", justify=CENTER, font=('Arial', 20))
calc_field.pack(padx=12, pady=10, ipady=8)

n0 = Button(button_frame, text="0", width=16, height=2, command=lambda:click("0")).grid(row=6, column=1, columnspan=2, pady=3, padx=3)
n1 = Button(button_frame, text="1", width=7, height=2, command=lambda:click("1")).grid(row=5, column=1, pady=3, padx=3)
n2 = Button(button_frame, text="2", width=7, height=2, command=lambda:click("2")).grid(row=5, column=2, pady=3, padx=3)
n3 = Button(button_frame, text="3", width=7, height=2, command=lambda:click("3")).grid(row=5, column=3, pady=3, padx=3)
n4 = Button(button_frame, text="4", width=7, height=2, command=lambda:click("4")).grid(row=4, column=1, pady=3, padx=3)
n5 = Button(button_frame, text="5", width=7, height=2, command=lambda:click("5")).grid(row=4, column=2, pady=3, padx=3)
n6 = Button(button_frame, text="6", width=7, height=2, command=lambda:click("6")).grid(row=4, column=3, pady=3, padx=3)
n7 = Button(button_frame, text="7", width=7, height=2, command=lambda:click("7")).grid(row=3, column=1, pady=3, padx=3)
n8 = Button(button_frame, text="8", width=7, height=2, command=lambda:click("8")).grid(row=3, column=2, pady=3, padx=3)
n9 = Button(button_frame, text="9", width=7, height=2, command=lambda:click("9")).grid(row=3, column=3, pady=3, padx=3)

equB = Button(button_frame, text="=", background="#ffbb48", activebackground="#ffbb48", width=7, height=2, command=lambda:process_statement()).grid(row=6, column=4, pady=3, padx=3)
dotB = Button(button_frame, text=".", width=7, height=2, command=lambda:click(".")).grid(row=6, column=3, pady=3, padx=3)
addB = Button(button_frame, text="+", width=7, height=2, command=lambda:click("+")).grid(row=5, column=4, pady=3, padx=3)
remB = Button(button_frame, text="-", width=7, height=2, command=lambda:click("-")).grid(row=4, column=4, pady=3, padx=3)
multB = Button(button_frame, text="*", width=7, height=2, command=lambda:click("*")).grid(row=3, column=4, pady=3, padx=3)
divB = Button(button_frame, text="/", width=7, height=2, command=lambda:click("/")).grid(row=2, column=4, pady=3, padx=3)
modB = Button(button_frame, text="%", width=7, height=2, command=lambda:click("%")).grid(row=1, column=1, pady=3, padx=3)
powB = Button(button_frame, text="xⁿ", width=7, height=2, command=lambda:click("**")).grid(row=2, column=2, pady=3, padx=3)
sqrtB = Button(button_frame, text="²√", width=7, height=2, command=lambda:click("**(0.5)")).grid(row=2, column=3, pady=3, padx=3)
invB = Button(button_frame, text="xˉ¹", width=7, height=2, command=lambda:click("**(-1)")).grid(row=2, column=1, pady=3, padx=3)
expB = Button(button_frame, text="exp", width=7, height=2, command=lambda:click("E")).grid(row=1, column=2, pady=3, padx=3)
clearB = Button(button_frame, text="CE", width=16, height=2, command=lambda:clear_statement()).grid(row=1, column=3, columnspan=2, pady=3, padx=3)

main_frame.pack()
button_frame.pack()

window.mainloop()