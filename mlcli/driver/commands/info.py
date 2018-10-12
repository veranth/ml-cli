from cleo import Command
from cleo import Output
from os import environ

from mlcli import _ROOT


class InfoCommand(Command):
    """
    Displays configuration for current project and mlcli.

    info
    """

    def handle(self):
        current_venv = environ.get("VIRTUAL_ENV")

        self.line(
            """<info>mlcli and project information</>\n"""
        )
        if Output.VERBOSITY_VERBOSE <= self.output.get_verbosity():
            pass

        if current_venv:
            self.line("Active virtual environment: <info>{}</>".format(current_venv))
        else:
            self.line("Virtual environment not activated")
        self.line("mlcli install directory: <info>{}</>".format(_ROOT))

