class Filter(object):
    """
    A helper class to resolve Bayfordbury filter names and prevent string inconsistencies.

    Usage:
    >>> red_filter = Filter("red")

    >>> Filter.filters_list
    Returns a list of strings with allowed filter names.

    >>> Filter.is_allowed(name)
    Arguments:
        name <string> : string representation of the filter
    Returns <boolean> : is it one of the filters used at Bayfordbury
    """

    filters_list = [
            "clear", 
            "i", "r", "v", "b",
            "halpha", "sii", "oiii", "465nm"
        ]

    def __init__(self, name):            
        self.name = self._from_string(name)


    def _from_string(self, name):
        if not Filter.is_allowed(name):
            raise ValueError("Unknown filter name <{}>. Use one of these: {}".format(name, self.filters_list))
        
        return self._normalise_filter_name(name)
    
    @staticmethod
    def is_allowed(name):
        if Filter._normalise_filter_name(name) in Filter.filters_list:
            return True

        return False


    @staticmethod
    def _normalise_filter_name(name):
        """
        Attempts to fix inconsistent filter names, e.g. red/Red/R -> r

        Arguments:
            name <string> : string representation of the filter
        Returns <string> : normalised filter name
        """
        name = name.strip().lower()

        name = name.replace("infrared", "i")
        name = name.replace("ir", "i")

        name = name.replace("red", "r")

        name = name.replace("green", "v")
        name = name.replace("g", "v")

        name = name.replace("blue", "b")

        name = name.replace("-", "")
        name = name.replace(" ", "")

        return name