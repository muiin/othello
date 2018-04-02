#!/usr/bin/python
# -*- coding: utf-8 -*

"Programming exercises #1: othello"

"pieces character: ○ ●   "
cb = [
       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
     ]


black = '*'
white = 'o'
pieces = [black, white]

cur_turn = 0


def show_blank_cb():

    print '  0 1 2 3 4 5 6 7'
    print ' ┌─┬─┬─┬─┬─┬─┬─┬─┐'
    print '0│ │ │ │ │ │ │ │ │'
    print ' ├─┼─┼─┼─┼─┼─┼─┼─┤'
    print '1│ │ │ │ │ │ │ │ │'
    print ' ├─┼─┼─┼─┼─┼─┼─┼─┤'
    print '2│ │ │ │ │ │ │ │ │'
    print ' ├─┼─┼─┼─┼─┼─┼─┼─┤'
    print '3│ │ │ │ │ │ │ │ │'
    print ' ├─┼─┼─┼─┼─┼─┼─┼─┤'
    print '4│ │ │ │ │ │ │ │ │'
    print ' ├─┼─┼─┼─┼─┼─┼─┼─┤'
    print '5│ │ │ │ │ │ │ │ │'
    print ' ├─┼─┼─┼─┼─┼─┼─┼─┤'
    print '6│ │ │ │ │ │ │ │ │'
    print ' ├─┼─┼─┼─┼─┼─┼─┼─┤'
    print '7│ │ │ │ │ │ │ │ │'
    print ' └─┴─┴─┴─┴─┴─┴─┴─┘'

def print_cb():

    print '  0 1 2 3 4 5 6 7'
    print ' ┌─┬─┬─┬─┬─┬─┬─┬─┐'
    print '0│%c│%c│%c│%c│%c│%c│%c│%c│' % (cb[0][0], cb[0][1], cb[0][2], cb[0][3], cb[0][4], cb[0][5], cb[0][6], cb[0][7])
    print ' ├─┼─┼─┼─┼─┼─┼─┼─┤'                                                                                      
    print '1│%c│%c│%c│%c│%c│%c│%c│%c│' % (cb[1][0], cb[1][1], cb[1][2], cb[1][3], cb[1][4], cb[1][5], cb[1][6], cb[1][7])
    print ' ├─┼─┼─┼─┼─┼─┼─┼─┤'                                                                                      
    print '2│%c│%c│%c│%c│%c│%c│%c│%c│' % (cb[2][0], cb[2][1], cb[2][2], cb[2][3], cb[2][4], cb[2][5], cb[2][6], cb[2][7])
    print ' ├─┼─┼─┼─┼─┼─┼─┼─┤'                                                                                      
    print '3│%c│%c│%c│%c│%c│%c│%c│%c│' % (cb[3][0], cb[3][1], cb[3][2], cb[3][3], cb[3][4], cb[3][5], cb[3][6], cb[3][7])
    print ' ├─┼─┼─┼─┼─┼─┼─┼─┤'                                                                                      
    print '4│%c│%c│%c│%c│%c│%c│%c│%c│' % (cb[4][0], cb[4][1], cb[4][2], cb[4][3], cb[4][4], cb[4][5], cb[4][6], cb[4][7])
    print ' ├─┼─┼─┼─┼─┼─┼─┼─┤'                                                                                      
    print '5│%c│%c│%c│%c│%c│%c│%c│%c│' % (cb[5][0], cb[5][1], cb[5][2], cb[5][3], cb[5][4], cb[5][5], cb[5][6], cb[5][7])
    print ' ├─┼─┼─┼─┼─┼─┼─┼─┤'                                                                                      
    print '6│%c│%c│%c│%c│%c│%c│%c│%c│' % (cb[6][0], cb[6][1], cb[6][2], cb[6][3], cb[6][4], cb[6][5], cb[6][6], cb[6][7])
    print ' ├─┼─┼─┼─┼─┼─┼─┼─┤'                                                                                      
    print '7│%c│%c│%c│%c│%c│%c│%c│%c│' % (cb[7][0], cb[7][1], cb[7][2], cb[7][3], cb[7][4], cb[7][5], cb[7][6], cb[7][7])
    print ' └─┴─┴─┴─┴─┴─┴─┴─┘'

    print ''
    print 'turn: %s' % (pieces[cur_turn])


def set_pieces(x, y, p):

    global cur_turn

    if x >= 0 and x <= 7 and y >= 0 and y <= 7:
        cb[x][y] = p
        cur_turn ^= 1
        print_cb()
        return True
    else:
        return False

def run():
    
    print 'Welcome to othello!'

    while True:
        cmd = raw_input('Enter cmd: ')
        if cmd == 'q':
            break

        elif cmd == 'p':
            print_cb()

        elif len(cmd) >= 5 and cmd[0] == 's':
            x = int(cmd.split(' ')[1])
            y = int(cmd.split(' ')[2])
            print 'set x:%d, y:%d' % (x, y)
            
            if set_pieces(x, y, pieces[cur_turn]) == False:
                print 'wrong place'

        else:
            print 'usage:'
            print '   p - print checkerboard. '
            print '   s - put pieces on checker board. '
            print '       s <x> <y>'
            print '   q - quit. '



if __name__ == '__main__':
    run()

