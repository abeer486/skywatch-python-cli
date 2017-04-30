"""
skywatch

Usage:
  skywatch -d | data
  skywatch -v | values
  skywatch -h | --help
  skywatch hello
  skywatch --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  skywatch hello

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/abeer486/skywatch-python-cli

"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():
    """Main CLI entrypoint"""
    import skywatch.commands
    options = docopt(__doc__, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items(): 
        if hasattr(skywatch.commands, k) and v:
            module = getattr(skywatch.commands, k)
            skywatch.commands = getmembers(module, isclass)
            command = [command[1] for command in skywatch.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
