import tkinter as tk


def add_num_input(inp: int, inp_str: tk.StringVar, hit_equals: list) -> None:
    curr = inp_str.get()
    if hit_equals[0]:
        inp_str.set(str(inp))
        hit_equals[0] = False
    else:
        inp_str.set(curr + str(inp))


def add_operator_input(inp: str, inp_str: tk.StringVar, hit_equals: list) -> None:
    if hit_equals[0]:
        hit_equals[0] = False

    operators = ['*', '/', '-', '+']
    curr = inp_str.get()
    if curr.split()[-1] in operators:
        inp_str.set(curr[:-2] + " " + inp + " ")
    else:
        inp_str.set(curr + " " + inp + " ")


def equals_input(inp_str: tk.StringVar, hit_equals: list) -> None:
    hit_equals[0] = True

    curr = inp_str.get()
    split = curr.split()
    result = float(split[0])

    for i in range(1, len(split)):
        if split[i] == '*':
            result *= float(split[i + 1])
        elif split[i] == '/':
            result /= float(split[i + 1])
        elif split[i] == '-':
            result -= float(split[i + 1])
        elif split[i] == '+':
            result += float(split[i + 1])

    inp_str.set(str(result))


def main():
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("250x200")
    # root.resizable(False, False)

    hit_equals = [False]

    input_str = tk.StringVar()

    display = tk.Label(root, textvariable=input_str, bg='white', bd=2, fg='black')
    display.pack(pady=10, fill='both', expand=True)

    frame = tk.Frame(root)
    frame.pack(fill='both', expand=True)

    for i in range(5):
        frame.grid_rowconfigure(i, weight=1)
        frame.grid_columnconfigure(i, weight=1)

    button7 = tk.Button(frame, text='7', command=lambda: add_num_input(7, input_str, hit_equals))
    button8 = tk.Button(frame, text='8', command=lambda: add_num_input(8, input_str, hit_equals))
    button9 = tk.Button(frame, text='9', command=lambda: add_num_input(9, input_str, hit_equals))
    button4 = tk.Button(frame, text='4', command=lambda: add_num_input(4, input_str, hit_equals))
    button5 = tk.Button(frame, text='5', command=lambda: add_num_input(5, input_str, hit_equals))
    button6 = tk.Button(frame, text='6', command=lambda: add_num_input(6, input_str, hit_equals))
    button1 = tk.Button(frame, text='1', command=lambda: add_num_input(1, input_str, hit_equals))
    button2 = tk.Button(frame, text='2', command=lambda: add_num_input(2, input_str, hit_equals))
    button3 = tk.Button(frame, text='3', command=lambda: add_num_input(3, input_str, hit_equals))
    button0 = tk.Button(frame, text='0', command=lambda: add_num_input(0, input_str, hit_equals))

    multiply = tk.Button(frame, text='*', command=lambda: add_operator_input('*', input_str, hit_equals))
    divide = tk.Button(frame, text='/', command=lambda: add_operator_input('/', input_str, hit_equals))
    minus = tk.Button(frame, text='-', command=lambda: add_operator_input('-', input_str, hit_equals))
    plus = tk.Button(frame, text='+', command=lambda: add_operator_input('+', input_str, hit_equals))
    equals = tk.Button(frame, text='=', command=lambda: equals_input(input_str, hit_equals))

    clear = tk.Button(frame, text='C', command=lambda: input_str.set(""))

    button7.grid(row=1, column=0, padx=2, sticky='nsew')
    button8.grid(row=1, column=1, padx=2, sticky='nsew')
    button9.grid(row=1, column=2, padx=2, sticky='nsew')
    button4.grid(row=2, column=0, padx=2, sticky='nsew')
    button5.grid(row=2, column=1, padx=2, sticky='nsew')
    button6.grid(row=2, column=2, padx=2, sticky='nsew')
    button1.grid(row=3, column=0, padx=2, sticky='nsew')
    button2.grid(row=3, column=1, padx=2, sticky='nsew')
    button3.grid(row=3, column=2, padx=2, sticky='nsew')
    button0.grid(row=4, column=1, padx=2, sticky='nsew')

    multiply.grid(row=1, column=3, sticky='nsew')
    divide.grid(row=2, column=3, sticky='nsew')
    minus.grid(row=3, column=3, sticky='nsew')
    plus.grid(row=4, column=3, sticky='nsew')
    equals.grid(row=4, column=4, sticky='nsew')

    clear.grid(row=1, column=4, sticky='nsew')

    root.mainloop()


if __name__ == "__main__":
    main()
