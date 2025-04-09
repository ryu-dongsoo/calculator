import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        # 결과 표시창
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        self.create_widgets()
        
    def create_widgets(self):
        # 결과 표시창
        result_entry = ttk.Entry(
            self.root, 
            textvariable=self.result_var, 
            justify="right",
            font=("Arial", 20)
        )
        result_entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        
        # 버튼 텍스트
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', '±', '%', '√'
        ]
        
        # 버튼 생성
        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            ttk.Button(
                self.root, 
                text=button,
                command=cmd
            ).grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # 그리드 가중치 설정
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
    
    def click(self, key):
        if key == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        elif key == 'C':
            self.result_var.set("0")
        elif key == '±':
            try:
                value = float(self.result_var.get())
                self.result_var.set(-value)
            except:
                self.result_var.set("Error")
        elif key == '%':
            try:
                value = float(self.result_var.get())
                self.result_var.set(value / 100)
            except:
                self.result_var.set("Error")
        elif key == '√':
            try:
                value = float(self.result_var.get())
                if value >= 0:
                    self.result_var.set(math.sqrt(value))
                else:
                    self.result_var.set("Error")
            except:
                self.result_var.set("Error")
        else:
            if self.result_var.get() == "0" or self.result_var.get() == "Error":
                self.result_var.set(key)
            else:
                self.result_var.set(self.result_var.get() + key)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop() 