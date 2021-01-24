from .filehandler import SettingsFilehandler
from .section import Section


class SettingsManager:

    def __init__(self):
        self._filehandler = SettingsFilehandler()

    def read(self, filename: str = None):
        self._filehandler.read(filename)

    def get_section(self, section_name: str) -> Section:
        return self._filehandler[section_name]
