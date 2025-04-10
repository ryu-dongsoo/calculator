# tkinter 모듈을 사용하여 GUI 계산기 구현
import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    # 계산기 클래스 초기화
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")  # 창 제목 설정
        self.root.geometry("300x400")  # 창 크기 설정
        self.root.resizable(False, False)  # 창 크기 조절 비활성화
        
        # 계산 결과를 저장할 변수 초기화
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        self.create_widgets()  # 위젯 생성 메서드 호출
        
    # 계산기 UI 위젯 생성
    def create_widgets(self):
        # 결과를 표시할 엔트리 위젯 생성
        result_entry = ttk.Entry(
            self.root, 
            textvariable=self.result_var, 
            justify="right",  # 텍스트 오른쪽 정렬
            font=("Arial", 20)  # 폰트 설정
        )
        result_entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        
        # 계산기 버튼 레이아웃 정의
        buttons = [
            '7', '8', '9', '/',  # 첫 번째 줄
            '4', '5', '6', '*',  # 두 번째 줄
            '1', '2', '3', '-',  # 세 번째 줄
            '0', '.', '=', '+',  # 네 번째 줄
            'C', '±', '%', '√'   # 다섯 번째 줄
        ]
        
        # 버튼 생성 및 배치
        row = 1
        col = 0
        for button in buttons:
            # 각 버튼에 대한 클릭 이벤트 핸들러 생성
            cmd = lambda x=button: self.click(x)
            ttk.Button(
                self.root, 
                text=button,
                command=cmd
            ).grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
            col += 1
            if col > 3:  # 한 줄에 4개의 버튼이 찼으면 다음 줄로 이동
                col = 0
                row += 1
        
        # 그리드 레이아웃의 행과 열 가중치 설정
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
    
    # 버튼 클릭 이벤트 처리
    def click(self, key):
        if key == '=':  # 계산 실행
            try:
                result = eval(self.result_var.get())  # 수식 계산
                self.result_var.set(result)
            except:
                self.result_var.set("Error")  # 계산 오류 발생 시
        elif key == 'C':  # 초기화
            self.result_var.set("0")
        elif key == '±':  # 부호 변경
            try:
                value = float(self.result_var.get())
                self.result_var.set(-value)
            except:
                self.result_var.set("Error")
        elif key == '%':  # 퍼센트 계산
            try:
                value = float(self.result_var.get())
                self.result_var.set(value / 100)
            except:
                self.result_var.set("Error")
        elif key == '√':  # 제곱근 계산
            try:
                value = float(self.result_var.get())
                if value >= 0:
                    self.result_var.set(math.sqrt(value))
                else:
                    self.result_var.set("Error")  # 음수의 제곱근은 오류
            except:
                self.result_var.set("Error")
        else:  # 숫자나 연산자 입력
            if self.result_var.get() == "0" or self.result_var.get() == "Error":
                self.result_var.set(key)  # 첫 번째 입력
            else:
                self.result_var.set(self.result_var.get() + key)  # 기존 값에 추가

# 프로그램 시작점
if __name__ == "__main__":
    root = tk.Tk()  # Tkinter 루트 윈도우 생성
    app = Calculator(root)  # 계산기 애플리케이션 인스턴스 생성
    root.mainloop()  # 이벤트 루프 시작 