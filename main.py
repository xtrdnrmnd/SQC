from tkinter import *
import random
import string
from tkinter.messagebox import showerror

maxNum = 30


class Symbols(object):
    len = 0

    def generate(self):
        len = random.randint(10, maxNum)
        seq = ""
        for symbol in range(len):
            if seq.__len__() <= len:
                num = random.choice(string.ascii_letters)
                kol = random.randint(0, (len - seq.__len__()))
                seq = seq + num * kol
            else:
                break
        return seq

    def defyNum(self, sequence, length):
        first = sequence[0]
        count = 1
        res = "Результат: "
        for i in range(length - 1):
            c = sequence[i + 1]
            if (c == first):
                count += 1
            else:
                res += "(" + str(count) + ")" + first
                count = 1
            first = c
        res += "(" + str(count) + ")" + first
        return res


def GUI():
    # Создание переменных для тестовых окон
    imput_str = StringVar()
    res = StringVar()

    lbl = Label(window, text="Ввести текст не более чем из 30 символов, в котором есть группы подряд идущих одинаковых "
                             "символов. Выполнить сжатие текста, текстом вида «(К)символ», где К –количество символов в "
                             "группе. Например, «ааааааааааа» заменяется на «(11)а».", wraplength=400)
    lbl.pack(expand='NO')

    sequence = Symbols()

    def generate():
        var = sequence.generate()
        imput_str.set(var)
        res.set(sequence.defyNum(var, var.__len__()))

    def validate(new_value):
        return new_value == "" or new_value.isalpha()

    def entry_set_call():
        text = imput_str.get()
        if len(text) > maxNum:
            imput_str.set(text[:-1])

    def clear():
        entry.delete(0, 'end')
        res.set("")

    def compress():
        if (imput_str.get() != ""):
            res.set(sequence.defyNum(imput_str.get(), len(imput_str.get())))
        else:
            showerror("showerror", "Поле не может быть пустым")

    vcmd = (window.register(validate), '%P')
    entry = Entry(window, width=50, textvariable=imput_str, validate='key', validatecommand=vcmd)
    entry.pack()
    imput_str.trace_variable("w", entry_set_call)

    compressBtn = Button(window, text="Сжать", command=compress)
    compressBtn.pack(expand='NO')
    genBtn = Button(window, text="Сгенерировать", command=generate)
    genBtn.pack(expand='NO')
    clBtn = Button(window, text="Очистить", command=clear)
    clBtn.pack(expand='NO')

    resLbl = Label(window, textvariable=res)
    resLbl.pack()


if __name__ == '__main__':
    # Создание окна графического интерфейса
    window = Tk()
    window.title("Практика 1")
    window.geometry("400x300")
    window.minsize(400, 300)

    GUI()

    window.mainloop()
