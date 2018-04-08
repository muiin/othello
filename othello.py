#!/usr/bin/python
# -*- coding: utf-8 -*

"Programming exercises #1: othello"

class Piece:
        blank=0
        black=1
        white=2

class Othello:
    def __init__(self):
        self.cb = []
        
        for x in range(8):
            row = []
            for y in range(8):
                row.append(Piece.blank)
            self.cb.append(row)

        self.counter = [0, 0]
        self.active = 0
        
        self.reset()

    def reset(self):
        for x in range(8):
            for y in range(8):
                self.cb[x][y] = Piece.blank
    
        self.cb[3][3] = Piece.black
        self.cb[3][4] = Piece.white
        self.cb[4][3] = Piece.white
        self.cb[4][4] = Piece.black
    
        self.counter = [2, 2]
        self.active = 0


    def check(self, b, x, y, p, mx, my):
        t = False
    
        while True:
            x = x + mx
            y = y + my
            if x < 0 or x >= 8 or y < 0 or y >= 8:
                break
    
            if t == False:
                if b[x][y] == p or b[x][y] == Piece.blank:
                    return False
                else:
                    t = True
            else:
                if b[x][y] == p:
                    return True
                elif b[x][y] == Piece.blank:
                    return False
        return False
    
    def turn(self, x, y, p, mx, my):
    
        while True:
            x = x + mx
            y = y + my
    
            if x < 0 or x >= 8 or y < 0 or y >= 8:
                break
    
            if self.cb[x][y] == p:
                break 
            else:
                self.cb[x][y] = p
                self.counter[self.active] += 1
                self.counter[self.active^1] -=1
    
    
    def turn_pieces(self, x, y, p):
    
        if self.cb[x][y] != Piece.blank:
            return False
    
        turned = False
        if self.check(self.cb, x, y, p, -1, 0):  #up
            self.turn(x, y, p, -1, 0)
            turned = True
        if self.check(self.cb, x, y, p, 1, 0):   #down
            self.turn(x, y, p, 1, 0)
            turned = True
        if self.check(self.cb, x, y, p, 0, -1):  #left
            self.turn(x, y, p, 0, -1)
            turned = True
        if self.check(self.cb, x, y, p, 0, 1):   #right
            self.turn(x, y, p, 0, 1)
            turned = True
        if self.check(self.cb, x, y, p, -1, -1): #left up
            self.turn(x, y, p, -1, -1)
            turned = True
        if self.check(self.cb, x, y, p, 1, -1):  #left down
            self.turn(x, y, p, 1, -1)
            turned = True
        if self.check(self.cb, x, y, p, -1, 1):  #right up
            self.turn(x, y, p, -1, 1)
            turned = True
        if self.check(self.cb, x, y, p, 1, 1):   #right down
            self.turn(x, y, p, 1, 1)
            turned = True
    
        if turned:
            self.cb[x][y] = p
            self.counter[self.active] += 1
            self.active ^= 1
    
        return turned    
    
    def set(self, x, y):
        p = Piece.blank
        if self.active == 0:
            p = Piece.black
        else:
            p = Piece.white
    
        return self.turn_pieces(x, y, p)
    
    def get_cb(self):
        return self.cb


