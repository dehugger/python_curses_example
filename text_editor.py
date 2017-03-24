import curses
from curses import wrapper
import time

class config(object):
    title_bar_height = 1
    title_bar_width = 100
    title_bar_color = 10 #blue
    main_display_height = 19
    main_display_width = 100
    main_window_line = 0 #variable for scrolling the main window, do not change
    input_window_height = 4
    input_window_width = 100
    input_window_carrot_color = 10
    input_window_line_color = 10

    username = 'ben'

def command_processor(command, write_window):
    if command == '/quit':
        exit()
        return True
    if command == '/whoami':
        message_display('I am ' + config.username, write_window)
        return True
    return False


def input_handler(input_window, write_window):
    user_input = ''
    while True:
        c = input_window.getch()
        if c == 10: #10 is the code for enter
            break
        else:
            user_input = user_input + chr(c)

    user_input = user_input.replace('\b', '')

    if command_processor(user_input, write_window) == False:
        message_display(user_input, write_window)
    else:
        pass
    input_window.clear()
    input_window.addstr(0, 0, "--------------------------------------------------------------------------------")
    input_window.addstr(1, 0, ">")
    input_window.refresh()

def message_display(message, write_window):
    split_count = 0
    if len(message) > config.main_display_width:
        split_number = len(message) / config.main_display_width
        split_number = int(round(split_number))
        while split_count <= split_number:
            split_one = split_count * config.main_display_width
            split_two = split_one + config.main_display_width
            write_line = message[split_one:split_two]
            write_window.addstr('\n' + write_line)
            split_count +=1
    else:
        write_window.addstr('\n' + message)
    if config.main_window_line >= (config.main_display_height - 2):
        write_window.refresh((config.main_window_line - ((config.main_display_height - 4) + split_count)), 0, 2, 0, config.main_display_height, config.main_display_width)
    else:
        write_window.refresh(0, 0, (config.title_bar_height + 1), 0, config.main_display_height, config.main_display_width)
    config.main_window_line += (split_count)

def main(stdscr):
    win_topbar = curses.newwin(config.title_bar_height, config.title_bar_width, 0, 0)
    win_main = curses.newpad(1000000, config.main_display_width)
    win_input = curses.newwin(config.input_window_height, config.input_window_width, (config.title_bar_height + config. main_display_height), 0)

    curses.start_color()
    curses.use_default_colors()
    for i in range(0, 15):
        curses.init_pair(i + 1, i, -1)

    win_topbar.addstr('My Cool Terminal App', curses.color_pair(config.title_bar_color))
    win_main.addstr('Type "/quit" to exit.')
    win_input.addstr(0, 0, "--------------------------------------------------------------------------------")
    win_input.addstr(1, 0, ">")

    win_topbar.refresh()
    win_main.refresh(0, 0, (config.title_bar_height + 1), 0, config.main_display_height, config.main_display_width)
    win_input.refresh()

    curses.echo()
    while True:
        input_handler(win_input, win_main)

wrapper(main)
