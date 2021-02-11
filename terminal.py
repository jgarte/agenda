# Console agenda - Copyright (c) 2021 Nicolas P. Rougier
# Released under the GNU General Public Licence version 3
import sys
import tty
import termios


class Terminal:
    """ Terminal in raw mode in order to track mouse movements. """
    
    def __init__(self):
        pass
    
    def write(self, text, position=None, flush=False):
        """ Write text at position and flush terminal if necessary. """
        
        if position:
            x, y = position
            sys.stdout.write("\033[%d;%dH" % (y, x))
        sys.stdout.write(text)
        if flush:
            sys.stdout.flush()

    def flush(self):
        """ Flush terminal. """
        sys.stdout.flush()
    
    def read(self, count=1):
        """ Read input. """
        
        return sys.stdin.read(count)

    def clear(self, position=None, flush=False):
        """ Clear screen (whole or from position) and flush if necessary. """
        
        if position:
            x, y = position
            sys.stdout.write("\033[%d;%dH " % (y, x))
            sys.stdout.write("\033[0m" + "\033[0J")  # clear from cursor to end
        else:
            sys.stdout.write("\033[0m" + "\033[2J")  # clear the whole creen
        if flush:
            sys.stdout.flush()
    
    def __enter__(self):
        """ Setup raw mode. """
        
        self.write("\0337")       # save current cursor position
        self.write("\033[?47h")   # save screen
        self.write("\033[?25l")   # make cursor invisible
        self.write("\033[?1003h") # enable mouse reporting
        self.write("\033[2J")     # clear whole screen
        self.flush()

        self.fd = sys.stdin.fileno()
        self.mode = termios.tcgetattr(self.fd)
        tty.setraw(self.fd)
        mode = termios.tcgetattr(self.fd)
        mode[3] |= termios.ISIG # Enable Ctrl-C
        termios.tcsetattr(self.fd, termios.TCSAFLUSH, mode)
        return self
    
    def __exit__(self, type, value, traceback):
        """ Restore terminal settings. """
        
        termios.tcsetattr(self.fd, termios.TCSADRAIN, self.mode)
        self.write("\x1b[?1003l") # disable mouse reporting
        self.write("\033[?25h")   # make cursor visible
        self.write("\033[?47l")   # restore screen
        self.write("\0338")       # restore current cursor position
        self.flush()


# ----------------------------------------------------------------------
if __name__ == "__main__":
    with Terminal() as terminal:
        terminal.write("Press 'q' to quit", (1,1), flush=True)
        while True:
            c = terminal.read()
            if c == "q":
                break
            elif c == "\033":
                c = terminal.read(2)
                if c == "[M":
                    control = terminal.read()
                    x = ord(terminal.read()) - 32
                    y = ord(terminal.read()) - 32
                    terminal.write("#", (x,y), flush=True)
