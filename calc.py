from tkinter import *

root = Tk()


def reusable_btn(text, function_name, row, column):
    return Button(root, text=text, command=function_name, width=10,
                  height=3, bd=6, bg='powder blue', font=('Arial', 10, 'bold')
                  ).grid(row=row, column=column)


def btn_Click(number):
    opera = str(answer.get())
    number = opera + number
    answer.set(number)


def btn_Clear():
    operator = ""
    answer.set(operator)


def btn_Eval():
    try:
        operator = eval(str(answer.get()))
        answer.set(operator)
    except ZeroDivisionError:
        answer.set("Cannot Divide By Zero!")


answer = StringVar()
text_answer = Entry(root, bd=6, width=30, bg='powder blue', font=('Arial', 16, 'bold'),
                    textvariable=answer)
text_answer.grid(row=0, column=0, columnspan=6)

reusable_btn('9', lambda: btn_Click('9'), 1, 0)
reusable_btn('8', lambda: btn_Click('8'), 1, 1)
reusable_btn('7', lambda: btn_Click('7'), 1, 2)
reusable_btn('+', lambda: btn_Click('+'), 1, 3)

reusable_btn('6', lambda: btn_Click('6'), 2, 0)
reusable_btn('5', lambda: btn_Click('5'), 2, 1)
reusable_btn('4', lambda: btn_Click('4'), 2, 2)
reusable_btn('-', lambda: btn_Click('-'), 2, 3)

reusable_btn('3', lambda: btn_Click('3'), 3, 0)
reusable_btn('2', lambda: btn_Click('2'), 3, 1)
reusable_btn('1', lambda: btn_Click('1'), 3, 2)
reusable_btn('*', lambda: btn_Click('*'), 3, 3)

reusable_btn('0', lambda: btn_Click('0'), 4, 0)
reusable_btn('C', lambda: btn_Clear(), 4, 1)
reusable_btn('/', lambda: btn_Click('/'), 4, 2)
reusable_btn('=', lambda: btn_Eval(), 4, 3)

root.title("Calculator Made By Sajjan")
root.mainloop()
