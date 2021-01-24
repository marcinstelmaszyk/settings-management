from configparser import ConfigParser, ExtendedInterpolation
from .section import Section


class SettingsFilehandler:
    """A handler of the configuration file

    Each configuration file consists of sections, each of which contains
    keys with values:
        [SectionName]
        key: value

    The handler allows to retrieve a specific SectionName as a SectionAdapter,
    using get_section() method.
    """

    def __init__(self):
        """Initialize a config parser with Extended Interpolation.

        The Extended Interpolation first preprocesses values prior to
        returning them from get_section() method.
        """
        self._parser = ConfigParser(interpolation=ExtendedInterpolation())

    def __getitem__(self, section_name: str) -> Section:
        """Convenience operator [], to get a config section by name."""
        return self.get_section(section_name)

    def has_section(self, section_name: str) -> bool:
        """Check whether the section with the given name exists."""
        return self._parser.has_section(section_name)

    def get_section(self, section_name: str) -> Section:
        """Retrieve a section by its name.

        :param section_name: The name of the section
        :return: Object of SectionAdapter
        :raises NameError: if the configuration section doesn't exist
        """
        if not self.has_section(section_name):
            msg = f"Configuration section '{section_name}' doesn't exist."
            raise NameError(msg)
        return Section(section_name, self._parser[section_name])

    def read(self, filename: str) -> None:
        """Read the configuration file.

        :param filename: Name of the configuration file
        :raises OSError: if the file can't be opened
        """
        if filename is None:
            msg = f"Missing configuration filename"
            raise NameError(msg)

        result = self._parser.read(filename)
        if not result:
            msg = f"Could not open {filename}"
            raise OSError(msg)
