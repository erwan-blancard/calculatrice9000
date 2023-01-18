from tkinter import *
from tkinter import font
import os


def click(char):
    if calc_field.cget("text") == "Error!":
        calc_field.config(text=char)
    else:
        calc_field.config(text=(calc_field.cget("text")+char))


def process_statement():
    statement = calc_field.cget("text")
    if statement != "":
        try:
            result = str(eval(statement))
            calc_field.config(text=result)
            add_to_history(statement, result)
        except:
            calc_field.config(text="Error!")


def clear_statement():
    calc_field.config(text="")


def del_char():
    statement = calc_field.cget("text")
    statement = statement[:-1]
    calc_field.config(text=statement)


def load_history():
    if os.path.exists("history.txt"):
        file = open("history.txt")
        h_list = []
        statement_list = []
        result_list = []
        for line in file:
            h_list += [line]

        j = 0
        while j < len(h_list):
            h_list[j] = h_list[j].replace("\n", "")

            separator_index = 0
            for c in h_list[j]:
                if c == ",":
                    statement_list += [h_list[j][0:separator_index]]
                    result_list += [h_list[j][separator_index+1:]]
                    break
                separator_index += 1
            j += 1

        i = 0
        while i < len(statement_list):
            add_to_history(statement_list[i], result_list[i], False)
            i += 1
        file.close()


def add_to_history(statement, result, append_to_file=True):
    label_filled = statement+" = "+result
    global menuhistory
    if menuhistory.entrycget(END, "label") != label_filled:
        menuhistory.add_command(label=label_filled, command=lambda line=statement: load_to_calc_field(line))
        if append_to_file:
            if os.path.exists("history.txt"):
                file = open("history.txt", "a")
                file.write(statement+","+result+"\n")
                file.close()
            else:
                file = open("history.txt", "w")
                file.write(statement+","+result+"\n")
                file.close()


def load_to_calc_field(line):
    calc_field.config(text=line)


def clear_history():
    if os.path.exists("history.txt"):
        os.remove("history.txt")
    global menubar
    menuhistory.delete(0, END)
    menuhistory.add_command(label="Effacer l'historique", command=lambda: clear_history())


window = Tk(className="Calculatrice 9000")
font.nametofont("TkDefaultFont").configure(size=14)
window.iconbitmap("calc_IDI_CALC_ICON.ico")
# window.geometry("400x556")
window.geometry("400x572")
window.resizable(width=False, height=False)

# history
menubar = Menu(window)
menuhistory = Menu(menubar, tearoff=0)
menuhistory.add_command(label="Effacer l'historique", command=lambda: clear_history())
menubar.add_cascade(label="Historique", menu=menuhistory)
load_history()
window.config(menu=menubar)

main_frame = Frame(window, padx=4, pady=4)
button_frame = Frame(window, padx=4, pady=4)

calc_field = Label(main_frame, relief="sunken", borderwidth=6, width=384, background="#e1ecf4", justify=CENTER, font=('Arial', 20))
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
clearB = Button(button_frame, text="CE", width=7, height=2, command=lambda:clear_statement()).grid(row=1, column=3, pady=3, padx=3)
delB = Button(button_frame, text="DEL", width=7, height=2, command=lambda:del_char()).grid(row=1, column=4, pady=3, padx=3)

main_frame.pack()
button_frame.pack()

window.mainloop()