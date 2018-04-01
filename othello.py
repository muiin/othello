#!/usr/bin/python
# -*- coding: utf-8 -*


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

def run():
    
    print 'Welcome to othello!'

    while True:
        cmd = raw_input('Enter cmd: ')
        if cmd == 'q':
            break

        elif cmd == 'p':
            show_blank_cb()

        else:
            print 'usage:'
            print '   p - print checkerboard. '
            print '   q - quit. '



if __name__ == '__main__':
    run()

