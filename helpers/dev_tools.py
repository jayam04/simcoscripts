from termcolor import colored

dev_mode = False
colors = {
    "INFO": "magenta",  # TODO: deprecate this
    "CHECKPOINT": "green",
    "DETAILS": "blue",  # TODO: deprecate this
    "ERROR": "red",
    "WARNING": "yellow",
    "LOG": "blue",
    "DEBUG": "red",
}


def start_dev_mode():
    global dev_mode
    dev_mode = True
    dev_print("started devmode!", "LOG")


def dev_print(string, info_type=None, color=None):
    global dev_mode
    if not dev_mode:
        return 0
    if not info_type:
        info_type = "LOG"
    info_type = info_type.upper()
    if not color:
        try:
            color = colors[info_type.upper()]
        except KeyError:
            color = "white"
    pretext = colored(f"{info_type[:10]:>10}", color) + ' - '
    print(pretext, string)
