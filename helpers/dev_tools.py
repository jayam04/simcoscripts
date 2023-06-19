from termcolor import colored

dev_mode = False
color = {
    "info": "magenta",
    "checkpoint": "green",
    "details": "blue"
}


def start_dev_mode():
    global dev_mode
    dev_mode = True
    dev_print("started devmode!", "info")


def dev_print(string, info_type=None):
    global dev_mode
    if not dev_mode:
        return 0
    pretext = ""
    if type:
        pretext = colored(info_type, color[info_type]) + ' - '
    print(pretext, string)
