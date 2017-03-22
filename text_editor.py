import curses
from curses import wrapper
import time

def input_handler(input_window, write_window):
    user_input = input_window.getstr(1,2).decode(encoding='utf-8')
    if user_input == '/quit':
        exit()
    input_window.clear()
    input_window.addstr(0, 0, "-------------------------------------------------------")
    input_window.addstr(1, 0, ">")
    write_window.addstr('\n' + user_input)
    write_window.refresh()
    input_window.refresh()

def main(stdscr):
    win_topbar = curses.newwin(1, 80, 0, 0)
    win_main = curses.newwin(17, 80, 2, 0)
    win_input = curses.newwin(2, 80, 19, 0)

    curses.start_color()
    curses.use_default_colors()
    for i in range(0, 15):
        curses.init_pair(i + 1, i, -1)

    win_topbar.addstr('My Cool Terminal App', curses.color_pair(10))
    win_main.addstr('Type "/quit" to exit.')
    win_input.addstr(0, 0, "-------------------------------------------------------")
    win_input.addstr(1, 0, ">")

    win_topbar.refresh()
    win_main.refresh()
    win_input.refresh()

    curses.echo()
    while True:
        input_handler(win_input, win_main)

wrapper(main)
