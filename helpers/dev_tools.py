from termcolor import colored

dev_mode = False
colors = {
    "info": "magenta",
    "checkpoint": "green",
    "details": "blue"
}


def start_dev_mode():
    global dev_mode
    dev_mode = True
    dev_print("started devmode!", "info")


def dev_print(string, info_type=None, color=None):
    global dev_mode
    if not dev_mode:
        return 0
    if not info_type:
        info_type = "details"
    if not color:
        try:
            color = colors[info_type]
        except KeyError:
            color = "white"
    pretext = colored(info_type, color) + ' - '
    print(pretext, string)
