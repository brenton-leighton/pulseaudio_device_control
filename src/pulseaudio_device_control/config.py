import os
import configparser
import ast
import sys

next_sink_ignore = []
next_source_ignore = []


# Remove first or last character(s) if they are quotes
def remove_quotes(s):
    if len(s) <= 1:
        return s

    if (s[0] == '\'' and s[-1] == '\'') or (s[0] == '\"' and s[-1] == '\"'):
        s = s[1:-1]

    return s


def load():
    config_file_path = os.path.expanduser('~/.config/pulseaudio_device_control/config.ini')

    # Return if there's no user config file
    if not os.path.exists(config_file_path):
        return

    # Load config file
    _config = configparser.ConfigParser()
    _config.read(config_file_path)

    global next_sink_ignore, next_source_ignore

    if "next" in _config:
        if "sink_ignore" in _config["next"]:
            list_string = _config["next"]["sink_ignore"]

            try:
                next_sink_ignore = ast.literal_eval(list_string)
            except ValueError:
                print('Unable to create sink_ignore list from string:', file=sys.stderr)
                print('    ' + list_string, file=sys.stderr)

        if "source_ignore" in _config["next"]:
            list_string = _config["next"]["source_ignore"]

            try:
                next_source_ignore = ast.literal_eval(list_string)
            except ValueError:
                print('Unable to create source_ignore list from string:', file=sys.stderr)
                print('    ' + list_string, file=sys.stderr)
