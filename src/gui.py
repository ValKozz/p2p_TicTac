import customtkinter as ctk
from PIL import Image, ImageTk

class Window(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title('TicTacToe')
        self.geometry("400x510")
        self.resizable(False, False)
        self.init_ui()

    def init_ui(self):

        # Main GUI frame
        self.ui_frame = ctk.CTkFrame(self)
        self.ui_frame.pack(side='top', expand=True, fill='both', padx=15, pady=15)
        # Canvas
        self.canvas = ctk.CTkCanvas(self.ui_frame, bg='#242424')
        self.canvas.pack(expand=True, padx=15, pady=15, fill='y',)
        self.loadImages()
        # Buttons
        self.give_up = ctk.CTkButton(self.ui_frame, text='Give up')
        self.give_up.pack(padx=15, pady=15)



    def loadImages(self):
        self.base = Image.open('assets/base.png').rotate(16)
        self.base = ImageTk.PhotoImage(file='assets/base.png')

        self.canvas.create_image((10, -40), image=self.base, anchor='nw')
        self.canvas.update()

        self.red = ImageTk.PhotoImage(Image.open('assets/red.png'))
        self.blu = ImageTk.PhotoImage(Image.open('assets/blu.png'))


win = Window()
win.mainloop()