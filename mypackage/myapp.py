"""Test application showing how to vendor Qt.py"""

from .vendor import Qt
from .vendor.Qt import QtWidgets


def run():
    """This runs my app"""

    print('Qt.py version: ' + Qt.__version__)
    print('Qt binding version: ' + Qt.__binding__ + ' ' +
          Qt.__binding_version__)


if __name__ == '__main__':
    run()
