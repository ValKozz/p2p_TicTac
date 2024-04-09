import customtkinter as ctk
from PIL import Image, ImageTk

ctk.set_appearance_mode("Dark")

class Window(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title('TicTacToe')
        self.geometry("400x550")
        self.resizable(False, False)
        self.init_ui()
        

    def init_ui(self):

        # Main GUI frame
        self.ui_frame = ctk.CTkFrame(self, height=520, width=320)
        self.ui_frame.pack(side='top', expand=True, fill='both', pady=15)
        # Canvas
        self.canvas = ctk.CTkCanvas(self.ui_frame, bg='#2b2b2b', bd=0, highlightbackground='#2b2b2b')
        self.canvas.pack(expand=True, padx=15, pady=15, fill='y')
        self.loadImages()

        # Buttons
        self.give_up = ctk.CTkButton(self.ui_frame, text='Give up', command=self.quit)
        self.give_up.pack(padx=15, pady=15)

        #Grid 
        row =0
        column=0

        for i in range(9):
            id = 'pos' + str(i + 1)
            self.makeGridButton(row, column, id)
            if column < 2:
                column += 1
            else:
                column = 0
                row += 1


    def makeGridButton(self, row, column, id):
        button = ctk.CTkButton(self.canvas, text='', width=80, height=80, image=self.empty, fg_color='transparent', command=lambda: self.test(id))
        button.grid(row=row, column=column, padx=15, pady=15)
          
    def loadImages(self):
        self.base = Image.open('assets/base.png').rotate(16)
        self.base = ImageTk.PhotoImage(file='assets/base.png')

        self.red = ImageTk.PhotoImage(Image.open('assets/red.png'))
        self.blu = ImageTk.PhotoImage(Image.open('assets/blu.png'))
        self.empty = ImageTk.PhotoImage(Image.open('assets/empty.png'))


    def quit(self):
        return super().quit()

    def test(self, num):
        print(f'You pressed {num}')

win = Window()
win.mainloop()