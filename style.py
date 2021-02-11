# Console agenda - Copyright (c) 2021 Nicolas P. Rougier
# Released under the GNU General Public Licence version 3

palettes = {
    "red":          [ "#ffebee", "#ffcdd2", "#ef9a9a", "#e57373", "#ef5350",
                      "#f44336", "#e53935", "#d32f2f", "#c62828", "#b71c1c" ],
    "pink":         [ "#fce4ec", "#f8bbd0", "#f48fb1", "#f06292", "#ec407a",
                      "#e91e63", "#d81b60", "#c2185b", "#ad1457", "#880e4f" ],
    "purple":       [ "#f3e5f5", "#e1bee7", "#ce93d8", "#ba68c8", "#ab47bc",
                      "#9c27b0", "#8e24aa", "#7b1fa2", "#6a1b9a", "#4a148c" ],
    "deep purple":  [ "#ede7f6", "#d1c4e9", "#b39ddb", "#9575cd", "#7e57c2",
                      "#673ab7", "#5e35b1", "#512da8", "#4527a0", "#311b92" ],
    "indigo":       [ "#e8eaf6", "#c5cae9", "#9fa8da", "#7986cb", "#5c6bc0",
                      "#3f51b5", "#3949ab", "#303f9f", "#283593", "#1a237e" ],
    "blue":         [ "#e3f2fd", "#bbdefb", "#90caf9", "#64b5f6", "#42a5f5",
                      "#2196f3", "#1e88e5", "#1976d2", "#1565c0", "#0d47a1" ],
    "light blue":   [ "#e1f5fe", "#b3e5fc", "#81d4fa", "#4fc3f7", "#29b6f6",
                      "#03a9f4", "#039be5", "#0288d1", "#0277bd", "#01579b" ],
    "cyan":         [ "#e0f7fa", "#b2ebf2", "#80deea", "#4dd0e1", "#26c6da",
                      "#00bcd4", "#00acc1", "#0097a7", "#00838f", "#006064" ],
    "teal":         [ "#e0f2f1", "#b2dfdb", "#80cbc4", "#4db6ac", "#26a69a",
                      "#009688", "#00897b", "#00796b", "#00695c", "#004d40" ],
    "green":        [ "#e8f5e9", "#c8e6c9", "#a5d6a7", "#81c784", "#66bb6a",
                      "#4caf50", "#43a047", "#388e3c", "#2e7d32", "#1b5e20" ],
    "light green":  [ "#f1f8e9", "#dcedc8", "#c5e1a5", "#aed581", "#9ccc65",
                      "#8bc34a", "#7cb342", "#689f38", "#558b2f", "#33691e" ],
    "lime":         [ "#f9fbe7", "#f0f4c3", "#e6ee9c", "#dce775", "#d4e157",
                      "#cddc39", "#c0ca33", "#afb42b", "#9e9d24", "#827717" ],
    "yellow":       [ "#fffde7", "#fff9c4", "#fff59d", "#fff176", "#ffee58",
                      "#ffeb3b", "#fdd835", "#fbc02d", "#f9a825", "#f57f17" ],
    "amber":        [ "#fff8e1", "#ffecb3", "#ffe082", "#ffd54f", "#ffca28",
                      "#ffc107", "#ffb300", "#ffa000", "#ff8f00", "#ff6f00" ],
    "orange":       [ "#fff3e0", "#ffe0b2", "#ffcc80", "#ffb74d", "#ffa726",
                      "#ff9800", "#fb8c00", "#f57c00", "#ef6c00", "#e65100" ],
    "deep orange":  [ "#fbe9e7", "#ffccbc", "#ffab91", "#ff8a65", "#ff7043",
                      "#ff5722", "#f4511e", "#e64a19", "#d84315", "#bf360c" ],
    "brown":        [ "#efebe9", "#d7ccc8", "#bcaaa4", "#a1887f", "#8d6e63",
                      "#795548", "#6d4c41", "#5d4037", "#4e342e", "#3e2723" ],
    "grey":         [ "#fafafa", "#f5f5f5", "#eeeeee", "#e0e0e0", "#bdbdbd",
                      "#9e9e9e", "#757575", "#616161", "#424242", "#212121" ],
    "blue grey":    [ "#eceff1", "#cfd8dc", "#b0bec5", "#90a4ae", "#78909c",
                      "#607d8b", "#546e7a", "#455a64", "#37474f", "#263238" ] }

def COLORPAIR(palette="deep orange", level=0):
    level = min(max(0, level), 9)
    color = palettes[palette][level].lstrip("#")
    R, G, B = int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16)
    L = R*0.299 + G*0.587 + B*0.114
    s = "\033[48;2;%d;%d;%dm" % (R,G,B)
    if L > 150:
        return s + "\033[38;2;%d;%d;%dm" % (0,0,0)
    else:
        return s + "\033[38;2;%d;%d;%dm" % (255,255,255)

NONE = DEFAULT   = "\033[0m"
   
WEIGHT_BOLD      = "\033[1m"
WEIGHT_REGULAR   = "\033[10m"
WEIGHT_LIGHT     = "\033[2m"

SLANT_NORMAL     = "\033[23m"
SLANT_ITALIC     = "\033[3m"

EFFECT_UNDERLINE = "\033[4m"
EFFECT_BLINK     = "\033[5m"
EFFECT_REVERSE   = "\033[7m"
EFFECT_STRIKE    = "\033[9m"

FG_BLACK   = "\033[30m"
FG_RED     = "\033[31m"
FG_GREEN   = "\033[32m"
FG_YELLOW  = "\033[33m"
FG_BLUE    = "\033[34m"
FG_MAGENTA = "\033[35m"
FG_CYAN    = "\033[36m"
FG_WHITE   = "\033[37m"
def FG(R,G,B):
    return "\033[38;2;%d;%d;%dm" % (R,G,B)

BG_BLACK   = "\033[40m"
BG_RED     = "\033[41m"
BG_GREEN   = "\033[42m"
BG_YELLOW  = "\033[43m"
BG_BLUE    = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN    = "\033[46m"
BG_WHITE   = "\033[47m"
def BG(R,G,B):
    return "\033[48;2;%d;%d;%dm" % (R,G,B)


class DefaultStyle:

    none           = NONE
    
    month          = DEFAULT + WEIGHT_BOLD + FG_WHITE + BG_BLACK
    active_month   = DEFAULT + WEIGHT_BOLD + FG_WHITE + BG_BLACK
    today          = DEFAULT + WEIGHT_BOLD + FG(255,255,255) + BG(0,0,0)
    weekday_name   = DEFAULT + WEIGHT_BOLD + FG_BLACK
    weekend_name   = DEFAULT + WEIGHT_LIGHT + FG_BLACK
    weekday        = DEFAULT
    weekend        = DEFAULT + WEIGHT_LIGHT

    default        = ""
    highlight      = COLORPAIR("yellow", 3)
    vacant         = DEFAULT + WEIGHT_LIGHT
    special        = ""
    
    levels         = [DEFAULT + COLORPAIR("deep purple", i) for i in range(10)]

    event_header   = DEFAULT + WEIGHT_BOLD + FG(0,0,0)
    event_past     = DEFAULT + WEIGHT_LIGHT
    event_today    = DEFAULT + FG_BLACK + WEIGHT_BOLD 
    event_future   = DEFAULT
    event_special  = FG_RED


    
# ----------------------------------------------------------------------
if __name__ == "__main__":

    H = FG_BLACK + WEIGHT_BOLD
    
    print(H + "Colors (from https://material.io):", end=DEFAULT)
    print()
    print()
    for name in palettes.keys():
        print("%12s: " % name, end="")
        for i in range(10):
            print( COLORPAIR(name, i) + "%2d\033[38;5;7m▕" % i, end=DEFAULT)
        print()
    print()

    print (H + "Font weights:", end=DEFAULT)
    print (WEIGHT_BOLD    + " BOLD",    end=DEFAULT)
    print (WEIGHT_REGULAR + " REGULAR", end=DEFAULT)
    print (WEIGHT_LIGHT   + " LIGHT",   end=DEFAULT)
    print()

    print (H + "Font slants: ", end=DEFAULT)
    print (" " + SLANT_NORMAL + "NORMAL", end=DEFAULT)
    print (" " + SLANT_ITALIC + "ITALIC", end=DEFAULT)
    print()

    print (H + "Font effects:", end=DEFAULT)
    print (" " + EFFECT_REVERSE   + "REVERSE",   end=DEFAULT)
    print (" " + EFFECT_UNDERLINE + "UNDERLINE", end=DEFAULT)
    print (" " + EFFECT_STRIKE    + "STRIKE",    end=DEFAULT)
    print (" " + EFFECT_BLINK     + "BLINK",     end=DEFAULT)
    print()
    
    print(H + "Markers sets:", end=DEFAULT)
    print()
    print("  MARKERS_NONE:     |%s|" % MARKERS_NONE)
    print("  MARKERS_NUMERIC:  |%s|" % MARKERS_NUMERIC)
    print("  MARKERS_DOTS:     |%s|" % MARKERS_DOTS)
    print("  MARKERS_FULLDOTS: |%s|" % MARKERS_FULLDOTS)
    print()
