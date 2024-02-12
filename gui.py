import tkinter as tk
from tkinter import ttk

# Define
BUTTON = [
    ['', 'B', 'C'],
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['0', '.', '=']
]

class CaluGui(object):
    def __init__(self, app=None):
        self.calc_str = ('')

        app.title('M(kg)の値を入力してください')
        app.geometry('300x450')

        calc_frame = ttk.Frame(app, width=300, height=100)
        calc_frame.propagate(False)
        calc_frame.pack(side=tk.TOP, padx=10, pady=20)
        button_frame = ttk.Frame(app, width=300, height=400)
        button_frame.propagate(False)
        button_frame.pack(side=tk.BOTTOM)

        self.calc_var = tk.StringVar()
        self.ans_var = tk.StringVar()
        calc_label = tk.Label(calc_frame, textvariable=self.calc_var, font=("",10))
        ans_label = tk.Label(calc_frame, textvariable=self.ans_var, font=("",8))
        calc_label.pack(anchor=tk.E)
        ans_label.pack(anchor=tk.E)

        for y, row in enumerate(BUTTON, 1):
            for x, num in enumerate(row):
                button = tk.Button(button_frame, text=num, font=('', 15), width=6, height=3)
                button.grid(row=y, column=x)
                button.bind('<Button-1>', self.click_button)
    
    def click_button(self, event):
        check = event.widget['text']
        if check == '=':
            sr = 'to 2GM/C^2 is ' + str(eval(self.calc_str) * 2 * 6.674 / 8987551790000000000000000) + 'mm'
            self.ans_var.set(sr)
        elif check == 'C':
            self.calc_str = ''
            self.ans_var.set('')
        elif check == 'B':
            self.calc_str = self.calc_str[:-1]
        else:
            self.calc_str += check

        self.calc_var.set(self.calc_str)
    


def main():
    # Window Setting
    app = tk.Tk()
    # Window size non resizable
    app.resizable(width=False, height=False)
    CaluGui(app)
    # Display
    app.mainloop()

if __name__ == '__main__':
    main()
