from gooey.gui.components.widgets import core
from gooey.gui.components.widgets.bases import TextContainer, BaseChooser


__ALL__ = [
    'FileChooser',
    'MultiFileChooser',
    'FileSaver',
    'DirChooser',
    'MultiDirChooser',
    'DateChooser'
]

class FileChooser(BaseChooser):
    # todo: allow wildcard from argparse
    widget_class = core.FileChooser


class MultiFileChooser(BaseChooser):
    # todo: allow wildcard from argparse
    widget_class = core.MultiFileChooser

    def formatOutput(self, metatdata, value):
        return formatters.multiFileChooser(metatdata, value)


class FileSaver(BaseChooser):
    # todo: allow wildcard
    widget_class = core.FileSaver


class DirChooser(BaseChooser):
    # todo: allow wildcard
    widget_class = core.DirChooser

class MultiDirChooser(BaseChooser):
    # todo: allow wildcard
    widget_class = core.MultiDirChooser


class DateChooser(BaseChooser):
    # todo: allow wildcard
    widget_class = core.DateChooser
