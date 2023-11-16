from tkinter import *
from tkinter import filedialog
from tkinter.font import Font
import os
from PIL import Image, ImageTk, ImageFilter


def add_button(target, x, y, text, function):
    button = Button(target, text=text, height=3, width=10, command=function)
    button.place(x=x, y=y)
    return button


class App:
    def __init__(self):
        self.i = 1
        self.window = Tk()
        self.background_width = 600
        self.background_height = 800
        self.half_width = int(self.background_height / 2)
        self.half_height = int(self.background_height / 2)
        custom_font = Font(family='Helvetica', size=10)
        self.entry = Entry(self.window)
        self.k = [None] * 10
        self.frame = self.assemble()
        self.frame.pack(side='top')
        convert_buttom = Button(self.window, text='convert', font=custom_font, command=self.convert).pack(side='bottom')

        self.window.mainloop()

    def convert(self):
        self.frame.destroy()
        self.frame = self.assemble()
        self.frame.pack(side='top')
        self.window.update()

    def assemble(self):
        frame = Frame(self.window, width=self.background_width, height=self.background_height)

        def calc(event):
            if self.k[self.i] is None:
                self.k[self.i] = self.entry.get()
            tmp.config(text=self.k[self.i])   # 입력 받은 텍스트으로 업데이트

        if self.i == 4:     # i에 따라 출력해주는 부분
            tmp = Label(frame, text=self.k[1])
        else:
            tmp = Label(frame, text=self.k[self.i + 1])

        if self.k[self.i + 1] is None:
            self.entry.bind("<Return>", calc)

        message2 = Label(frame, text=self.message(self.i), justify=LEFT)

        if self.i == 1: # 경로는 사용자경로이므로 다른 환경에서는 오류가 발생할 수 있다.
            image = Image.open(r'/Users/wonyong/PycharmProjects/pythonProject3/Major_PG2/231108/image1.png')
            image = image.resize((self.half_width, self.half_height), Image.ANTIALIAS)
            self.i = 2
        elif self.i == 2:
            image = Image.open(r'/Users/wonyong/PycharmProjects/pythonProject3/Major_PG2/231108/image2.png')
            image = image.resize((self.half_width, self.half_height), Image.ANTIALIAS)
            self.i = 3
        elif self.i == 3:
            image = Image.open(r'/Users/wonyong/PycharmProjects/pythonProject3/Major_PG2/231108/image3.png')
            image = image.resize((self.half_width, self.half_height), Image.ANTIALIAS)
            self.i = 4
        else:
            image = Image.open(r'/Users/wonyong/PycharmProjects/pythonProject3/Major_PG2/231108/image4.png')
            image = image.resize((self.half_width, self.half_height), Image.ANTIALIAS)
            self.i = 1

        if self.k[self.i] is None:  # entry 보여지고 숨겨지는 부분
            self.entry.pack(side='top')
            self.entry.delete(0, 15)       # 넘어갈때 마다 버퍼 초기화
        else:
            self.entry.pack_forget()

        tkimage = ImageTk.PhotoImage(image=image)
        image = Label(frame, image=tkimage)
        image.image = tkimage
        tmp.pack(side='top')    # 저장되어 있는 것 출력
        message2.pack(side='left')
        image.pack(side='right')
        return frame

    def message(self, i):
        if i == 1:
            return """
            동해 물과 백두산이 마르고 닳도록
            하느님이 보우하사 우리나라 만세.
            무궁화 삼천리 화려 강산
            대한 사람, 대한으로 길이 보전하세.
            """
        elif i == 2:
            return """
            남산 위에 저 소나무, 철갑을 두른 듯
            바람 서리 불변함은 우리 기상일세.
            무궁화 삼천리 화려 강산
            대한 사람, 대한으로 길이 보전하세.       
            """
        elif i == 3:
            return """
            가을 하늘 공활 한데 높고 구름 없이 
            밝은 달은 우리 가슴 일편단심일세
            무궁화 삼천리 화려강산 
            대한 사람, 대한으로 길이보전하세      
            """
        else:
            return """
            이 기상과 이 맘으로 충성을 다하여
            괴로우나 즐거우나 나라사랑하세
            무궁화 삼천리 화려강산 
            대한 사람, 대한으로 길이보전하세      
            """


if __name__ == '__main__':
    App()
