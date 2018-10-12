from mlcli import __version__

from cleo import Application
from cleo.inputs import ArgvInput
from cleo.outputs import ConsoleOutput
from cleo.outputs import Output

from .commands import InfoCommand


def main():
    application = Application("mlcli", __version__)
    application.add(InfoCommand())
    application.run(ArgvInput(), ConsoleOutput())