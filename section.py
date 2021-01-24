

class Section:
    """Adapts Section class returned by the ConfigParser::__getitem__()

    The section may contain several key:value pairs.
    """

    def __init__(self, name: str, section):
        """Initialize with section name and section adaptee

        :param name: Section name
        :param section: ConfigParser.section
        """
        self.section_name = name
        self._section_proxy = section

    def __getitem__(self, key: str) -> str:
        value = self._section_proxy.get(key)
        if value is None:
            msg = f"Missing key '{key}' in section '{self.section_name}'"
            raise NameError(msg)
        return value

    def format(self, key: str, **kwargs) -> str:
        """For the given section key, format corresponding value by substituting
        placeholders, written as {kwarg_key}, with kwarg_value.

        Example:
            section.format('title', year=2021)

        :param key: Name of the section key
        :param kwargs: text replacing a placeholder
        :raises NameError: if the section doesn't contain the placeholder
        """
        try:
            return self[key].format(**kwargs)
        except KeyError as err:
            msg = f"[Configuration] Missing placeholder {err.args}" \
                  f" in section '{self.section_name}'"
            raise NameError(msg)
