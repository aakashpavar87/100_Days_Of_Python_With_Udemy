import curses
import time
from curses import wrapper
import random


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome To Python Typing Test!", curses.color_pair(1))
    stdscr.addstr("\nType any key to begin !!!!!", curses.color_pair(2))
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr, target_text, current_text, wpm=0):
    stdscr.addstr(target_text)
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    for i,char in enumerate(current_text):
        correct_char = target_text[i]
        if char != correct_char:
            stdscr.addstr(0, i, char, curses.color_pair(2))
        else:
            stdscr.addstr(0, i, char, curses.color_pair(1))


def wpm_test(stdscr):
    current_text = []
    
    with open("lines.txt", "r") as f:
        target_text = random.choice(f.readlines()).strip()

    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)
    
    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text)/(time_elapsed/60)) / 5)
        
        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()
        
        if target_text == "".join(current_text):
            stdscr.nodelay(False)
            break
        
        try:
            key = stdscr.getkey()
        except:
            continue
        
        if ord(key) == 27:
            break

        if key in ["\b", "KEY_BACKSPACE", "\x7f"]:
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)


def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(3, 0, "You completed the test successfully type any key to continue...")
        key = stdscr.getkey()
        if ord(key) == 27:
            break

wrapper(main)
