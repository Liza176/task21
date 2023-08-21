# from tkinter import*
# from tkinter import ttk
# tk = Tk()
# canvas = Canvas(tk,width = 400,height = 400)
# canvas.pack()
# canvas.create_polygon(10,10,10,60,50,35)
# btn = Button(text='Жми')
# btn.pack()

# def movetriangle(event):
#     if event.keysym.lower() == 'space':
#         canvas.move(1,0,-3)
#     if event.keysym.lower() == 's':
#         canvas.move(1,0,3)
#     if event.keysym.lower() == 'a':
#         canvas.move(1,-3,0)
#     if event.keysym.lower() == 'd':
#         canvas.move(1,3,0)

# canvas.bind_all('<KeyPress-space>',movetriangle)
# canvas.bind_all('<KeyPress-s>',movetriangle)
# canvas.bind_all('<KeyPress-a>',movetriangle)
# canvas.bind_all('<KeyPress-d>',movetriangle)

# tk.mainloop()


# from tkinter import*
# from tkinter import ttk
# tk = Tk()

# canvas = Canvas(tk,width = 400,height = 400)
# canvas.pack()
# count = 0

# def movetriangle(event):
#     if event.keysym.lower() == 'space':
#         global count
#         count += 1
#         btn['text'] = f'ты нажал {count} раз'     

# btn = ttk.Button( text='Нажми пробел')
# btn.pack()

# canvas.bind_all('<KeyPress-space>',movetriangle)

# tk.mainloop()
# print(count)

# from tkinter import*
# from tkinter import ttk

# tk = Tk()
# canvas = Canvas(tk,width = 400,height = 400)
# canvas.pack()

# def movetriangle():
#     canvas.move(1,0,-3)

# canvas.create_polygon(10,10,10,60,50,35)
# btn = ttk.Button( text='Нажми',command=movetriangle)
# btn.pack()

from tkinter import*
import time
tk = Tk()
canvas = Canvas(tk,width = 1000,height = 400)
canvas.pack()


n1 = canvas.create_rectangle(20,20,50,50,fill='#98F5FF')

n2 = canvas.create_rectangle(20,70,50,100,fill='#FF69B4')


def movetriangle(event):
    if event.keysym.lower() == 'q':
        canvas.move(1,3,0)

def movetriangle1(event):
    if event.keysym.lower() == 'a':
        canvas.move(1,3,0)


canvas.bind_all('<KeyPress-q>',movetriangle)

canvas.bind_all('<KeyPress-a>',movetriangle1)

tk.mainloop()