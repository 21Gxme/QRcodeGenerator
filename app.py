from tkinter import *
import pyqrcode

from PIL import ImageTk, Image

class app:
    def __init__(self):
        self.root = Tk()
        self.root.title("QRCode Generator")
        self.root.geometry("300x500")
        self.root.resizable(0, 0)
        self.canvas = Canvas(self.root, width=600, height=700)
        self.canvas.pack()
        # label
        self.Label = Label(self.root, text="QRCode Generator", font=("Arial", 20))
        self.canvas.create_window(150, 50, window=self.Label)
        self.Label = Label(self.root, text="Enter the text", font=("Arial", 12))
        self.canvas.create_window(150, 100, window=self.Label)
        self.Label = Label(self.root, text="URL", font=("Arial", 12))
        self.canvas.create_window(150, 150, window=self.Label)
        # box
        self.name = Entry(self.root)
        self.canvas.create_window(150, 120, window=self.name)
        self.url = Entry(self.root)
        self.canvas.create_window(150, 170, window=self.url)
        # button
        self.button = Button(text="Generate", command=self.get_qr)
        self.canvas.create_window(150, 200, window=self.button)
        self.root.mainloop()

    def get_qr(self):
        link = self.url.get()
        text = self.name.get()
        file_name = text + ".png"
        pyqrcode.create(link).png(file_name, scale=5)
        image = ImageTk.PhotoImage(Image.open(file_name))
        image_label = Label(image=image)
        image_label.image = image
        self.canvas.create_window(150, 350, window=image_label)


app = app()
