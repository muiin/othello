#!/usr/bin/python
# -*- coding: utf-8 -*

#import Tkinter
from Tkinter import *
from othello import Othello
from othello import Piece

cb = []
tx = []

def refresh(othello):
    for x in range(8):
        for y in range(8):
            b = cb[x][y]
            t = tx[x][y]
            p = othello.get_cb()[x][y]
            if p == Piece.blank:
                t.set(' ')
            elif p == Piece.black:
                t.set('*')
                b['bg'] = 'black'
                b['state'] = 'disabled'
            else:
                t.set('o')
                b['bg'] = 'white'
                b['state'] = 'disabled'

def onClick(othello, x, y):
    def wrapper(o=othello, x_=x, y_=y):
        print '%d, %d' % (x, y)
        othello.set(x, y)
        refresh(o)
    return wrapper


def main():
    othello = Othello()
    
    top = Tk()
    top.title('othello')
    
    for x in range(8):
        cols_t = []
        cols_b = []
        for y in range(8):
            t = StringVar()
            b = Button(top, 
                       textvariable=t, 
                       font=24,
                       bg='blue',
                       width=5, 
                       height=2, 
                       borderwidth=1, 
                       relief=SOLID, 
                       command=onClick(othello, x, y))
            b.grid(row=x, column=y, sticky=NSEW)
            cols_t.append(t)
            cols_b.append(b)
        cb.append(cols_b)
        tx.append(cols_t)

    refresh(othello)

    mainloop()

if __name__ == '__main__':
    main()
